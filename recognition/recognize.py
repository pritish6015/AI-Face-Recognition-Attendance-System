import cv2
import pickle
import sqlite3
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("models/trainer.yml")

with open("models/labels.pkl", "rb") as f:
    labels = pickle.load(f)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)


conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()


def mark_attendance(unique_id):
    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "SELECT * FROM attendance WHERE unique_id=? AND date=?",
        (unique_id, today)
    )
    result = cursor.fetchone()

    if result:
        return

    cursor.execute(
        "SELECT full_name FROM users WHERE unique_id=?",
        (unique_id,)
    )

    user = cursor.fetchone()

    if user:
        full_name = user[0]

        cursor.execute(
            """
            INSERT INTO attendance
            (unique_id, full_name, date, check_in, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                unique_id,
                full_name,
                today,
                datetime.now().strftime("%H:%M:%S"),
                "Present"
            )
        )

        conn.commit()
        print("Attendance Marked Successfully")
        cap.release()
        cv2.destroyAllWindows()
        conn.close()
        exit()


while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        face = cv2.resize(face, (200, 200))

        id, confidence = recognizer.predict(face)

        if confidence < 60:
            unique_id = labels[id]

            today = datetime.now().strftime("%Y-%m-%d")

            cursor.execute(
                "SELECT * FROM attendance WHERE unique_id=? AND date=?",
                (unique_id, today)
            )

            already_marked = cursor.fetchone()

            if already_marked:
                text = f"{unique_id} - Already Marked"
                color = (0, 255, 255)

            else:
                mark_attendance(unique_id)

                text = f"{unique_id} - Attendance Marked"
                color = (0, 255, 0)

            # Draw rectangle and text
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

            cv2.putText(
                frame,
                text,
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            # Show message on screen
            cv2.imshow("AI Attendance System", frame)

            # Wait for 2 seconds
            cv2.waitKey(2000)

            # Close camera automatically
            cap.release()
            cv2.destroyAllWindows()
            conn.close()

            exit()
        else:
            color = (0, 0, 255)
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.putText(
            frame,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

    cv2.imshow("AI Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
conn.close()