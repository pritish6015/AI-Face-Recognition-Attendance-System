# 🎯 Enterprise AI Face Recognition Attendance System

## 📌 Project Overview

The **Enterprise AI Face Recognition Attendance System** is a modern AI-powered attendance management platform built using Python, OpenCV, Streamlit, SQLite, and Machine Learning.

The system automatically detects and recognizes faces through a webcam and marks attendance in real time. It includes:

* 🔐 Role-Based Authentication
* 👨‍💼 Admin Dashboard
* 👨‍🎓 User Dashboard
* 📊 Attendance Analytics
* 📈 Interactive Charts & Reports
* 🤖 AI Face Recognition
* 🗂 Attendance Monitoring
* 🧾 CSV Export Reports
* 🔑 Secure Login System

This project is designed for:

* Schools
* Colleges
* Offices
* Organizations
* AI/ML Portfolio Projects
* Final Year Projects
* Enterprise Attendance Monitoring

---

# 🚀 Key Features

## 🔐 Authentication System

### Admin Login

Admin has complete system access.

### User Login

Users can only view their personal attendance records.

### Password Security

Passwords are securely stored using:

* `bcrypt` hashing

---

# 👨‍💼 Admin Dashboard Features

The admin dashboard provides complete monitoring and management capabilities.

## ✅ User Management

Admin can:

* Create users
* Delete users
* Generate credentials
* Register faces
* Retrain AI model automatically

---

## 📊 Attendance Analytics

Admin can view:

* Total users
* Total attendance
* Present today
* Daily trends
* Monthly trends
* Yearly trends
* Attendance statistics
* Attendance distribution charts

---

## 📈 Interactive Charts

The system includes:

* Line charts
* Pie charts
* Attendance trend graphs
* Attendance distribution analysis

Built using:

* Plotly

---

## 🧾 Reports & Export

Admin can:

* Filter attendance
* Export attendance reports
* Download CSV files

Filters available:

* Today
* Monthly
* Yearly
* All Records

---

## 🎥 Live Attendance Monitoring

Admin can:

* Start camera
* Monitor face detection
* View real-time attendance marking

---

# 👨‍🎓 User Dashboard Features

Each user receives:

* Unique ID
* Username
* Password

Example IDs:

```text
EMP-001
STU-001
```

---

## User Dashboard Includes

Users can:

* Login securely
* View personal profile
* View attendance history
* View attendance charts
* Monitor personal attendance records

Users CANNOT:

* Edit data
* Delete records
* Access admin controls
* View other users' data

---

# 🤖 AI Face Recognition System

The project uses:

* OpenCV
* Haar Cascade
* LBPH Face Recognizer

---

## Face Recognition Workflow

```text
Face Capture
      ↓
Dataset Generation
      ↓
Model Training
      ↓
Real-Time Recognition
      ↓
Attendance Marking
```

---

## Face Detection

Uses:

```python
haarcascade_frontalface_default.xml
```

for real-time face detection.

---

## Face Recognition

Uses:

```python
LBPHFaceRecognizer
```

Advantages:

* Fast recognition
* Lightweight
* Offline support
* CPU-friendly
* Easy deployment

---

# 🗄 Database Structure

The project uses:

* SQLite Database

Database File:

```text
attendance.db
```

---

## Database Tables

### users

Stores:

* Unique ID
* Username
* Password
* Role
* Department
* Full Name

---

### attendance

Stores:

* Attendance records
* Check-in time
* Date
* Status

---

### login_logs

Stores:

* User login history
* Login timestamps

---

# 🧱 Project Architecture

```text
project/
│
├── app.py
├── requirements.txt
│
├── database/
│     └── database.py
│
├── auth/
│     ├── auth_utils.py
│     └── login.py
│
├── admin/
│     ├── dashboard.py
│     ├── analytics.py
│     ├── users.py
│     └── reports.py
│
├── user/
│     ├── dashboard.py
│     └── attendance.py
│
├── recognition/
│     ├── add_face.py
│     ├── train_model.py
│     └── recognize.py
│
├── models/
│     ├── trainer.yml
│     └── labels.pkl
│
├── dataset/
├── attendance.db
└── assets/
```

---

# 🛠 Technologies Used

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Main programming language    |
| OpenCV     | Face detection & recognition |
| Streamlit  | Web dashboard UI             |
| SQLite     | Database management          |
| Plotly     | Interactive charts           |
| NumPy      | Numerical operations         |
| Pandas     | Data analysis                |
| bcrypt     | Password hashing             |

---

# 📚 Python Libraries Used

## Core Libraries

```python
streamlit
opencv-contrib-python
numpy
pandas
plotly
bcrypt
sqlite3
pickle
```

---

# ⚙ Installation Guide

## Step 1: Clone Project

```bash
git clone <https://github.com/pritish6015/AI-Face-Recognition-Attendance-System.git>
```

---

## Step 2: Open Project Folder

```bash
cd project
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Start Streamlit Application

```bash
streamlit run app.py
```

---

# 🔑 Default Admin Credentials

```text
Username: admin
Password: admin123
```

⚠ Change the password after first login.

---

# 📸 How Attendance Works

## Step 1

Admin creates user.

---

## Step 2

Face images are captured through webcam.

---

## Step 3

AI model is trained automatically.

---

## Step 4

Camera detects faces in real time.

---

## Step 5

Recognized user attendance is marked.

---

# 📊 Analytics Features

The system supports:

* Daily attendance analytics
* Monthly attendance trends
* Yearly attendance reports
* Attendance monitoring
* Attendance visualization
* Attendance statistics

---

# 🔒 Security Features

## Included

* Password hashing
* Role-based authentication
* Session management
* User access restriction

---

## Future Security Upgrades

Possible improvements:

* JWT Authentication
* Face Anti-Spoofing
* Multi-factor Authentication
* Email OTP Verification
* Liveness Detection

---

# 📁 Generated Files

## AI Model Files

```text
models/trainer.yml
models/labels.pkl
```

---

## Dataset Storage

```text
dataset/EMP-001/
dataset/STU-001/
```

---

# 📌 Future Enhancements

Future upgrades possible:

* DeepFace / FaceNet Integration
* Cloud Database
* PostgreSQL/MySQL Support
* Mobile Application
* Email Notifications
* Attendance Heatmaps
* Department Analytics
* PDF Report Export
* REST API Backend
* Docker Deployment
* Cloud Hosting

---

# 🎯 Project Advantages

## Advantages

* Real-time attendance system
* AI-powered recognition
* Secure login system
* Enterprise dashboard
* Interactive analytics
* Automated attendance marking
* Easy deployment
* Offline support
* Lightweight architecture

---

# ⚠ Current Limitations

## Current Version Limitations

* Basic LBPH recognition
* No anti-spoofing
* SQLite for local deployment only
* Webcam dependency

---

# 🧠 Learning Outcomes

This project demonstrates:

* Computer Vision
* Machine Learning
* Face Recognition
* Database Management
* Authentication Systems
* Dashboard Development
* Data Analytics
* Streamlit Development
* Python Backend Development

---

# 📷 Screens Included (Optional)

You can add screenshots here:

```text
Login Page Screenshot
Admin Dashboard Screenshot
User Dashboard Screenshot
Analytics Screenshot
Attendance Recognition Screenshot
```

---

# 🤝 Contribution

Contributions are welcome.

You can improve:

* UI/UX
* AI Accuracy
* Security
* Performance
* Deployment

---

# 📄 License

This project is developed for educational and professional learning purposes.

---

# 👨‍💻 Developer

Developed using:

* Python
* OpenCV
* Streamlit
* SQLite
* Plotly

---

# ⭐ Final Summary

The Enterprise AI Face Recognition Attendance System is a modern AI-powered attendance platform designed for organizations, institutions, and enterprises.

It combines:

* Artificial Intelligence
* Face Recognition
* Authentication
* Analytics
* Dashboard Monitoring
* Attendance Automation

into a complete real-world attendance management solution.
