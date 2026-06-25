import cv2
import os
import numpy as np
import pickle

DATASET_PATH = "dataset"
MODEL_PATH = "models/trainer.yml"
LABEL_PATH = "models/labels.pkl"

faces = []
labels = []
label_map = {}

current_id = 0

for person in os.listdir(DATASET_PATH):
    person_path = os.path.join(DATASET_PATH, person)

    if not os.path.isdir(person_path):
        continue

    label_map[current_id] = person

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        img = cv2.imread(img_path, 0)

        if img is None:
            continue

        faces.append(img)
        labels.append(current_id)

    current_id += 1

labels = np.array(labels)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, labels)

recognizer.save(MODEL_PATH)

with open(LABEL_PATH, "wb") as f:
    pickle.dump(label_map, f)

print("Model Training Complete")