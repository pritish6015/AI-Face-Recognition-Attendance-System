# 🎯 Enterprise AI Face Recognition Attendance System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Recognition-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue.svg)
![License](https://img.shields.io/badge/License-Educational-orange.svg)

---

# 📌 Project Overview

The **Enterprise AI Face Recognition Attendance System** is a modern AI-powered attendance management platform built using Python, OpenCV, Streamlit, SQLite, and Machine Learning.

The system automatically detects and recognizes faces through a webcam and marks attendance in real time.

### Key Modules

✅ AI Face Recognition

✅ Attendance Automation

✅ Role-Based Authentication

✅ Admin Dashboard

✅ User Dashboard

✅ Analytics & Reporting

✅ CSV Export

✅ Secure Login System

---

# 📸 Attendance Marking Workflow

The attendance process follows a complete AI-powered workflow from face detection to database storage.

![Attendance Process](Submission%20Document/ATTENDANCE%20MARKING%20PROCESS.png)

---

# 🚀 Key Features

## 🔐 Authentication System

### Admin Login

Admin has complete system access.

### User Login

Users can only access their own attendance records.

### Password Security

Passwords are securely stored using:

```python
bcrypt
```

---

# 👨‍💼 Admin Dashboard

Admin Dashboard provides complete monitoring and management.

### User Management

- Create Users
- Delete Users
- Register Faces
- Generate Credentials
- Retrain Recognition Model

### Attendance Analytics

- Daily Attendance
- Monthly Trends
- Yearly Trends
- Present Today
- Total Attendance
- Attendance Statistics

### Interactive Charts

Built using Plotly:

- Line Charts
- Pie Charts
- Trend Analysis
- Distribution Reports

### Reports & Export

- CSV Export
- Filter by Date
- Monthly Reports
- Yearly Reports
- Full Attendance Reports

### Live Monitoring

- Real-time Face Detection
- Attendance Tracking
- Camera Monitoring

---

# 👨‍🎓 User Dashboard

Every user receives:

```text
EMP-001
STU-001
```

### User Features

- Secure Login
- Attendance History
- Personal Analytics
- Profile Information
- Attendance Charts

### Restrictions

Users cannot:

- Access Admin Panel
- Modify Attendance
- Delete Records
- View Other Users

---

# 🤖 AI Face Recognition System

### Technologies Used

- OpenCV
- Haar Cascade Classifier
- LBPH Face Recognizer

### Recognition Workflow

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

### Face Detection

```python
haarcascade_frontalface_default.xml
```

### Face Recognition

```python
LBPHFaceRecognizer
```

### Advantages

- Fast Recognition
- Lightweight
- Offline Support
- CPU Friendly
- Easy Deployment

---

# 🧱 System Architecture

The application follows a layered enterprise architecture.

![Project Architecture](Submission%20Document/project%20arc.png)

### Architecture Layers

### Presentation Layer

- Streamlit UI
- Login System
- Dashboard
- Reports

### Application Layer

- Authentication Module
- Attendance Processing
- Analytics Engine
- Report Generator

### AI Recognition Layer

- OpenCV
- Haar Cascade
- Face Recognition Engine

### Database Layer

- SQLite
- User Records
- Attendance Logs

---

# 📁 Project File Structure

The project is organized into modular folders for scalability and maintenance.

![Project File Structure](Submission%20Document/PROJECT%20FILE%20STRUCTURE.png)

---

# 🗄 Database Structure

The application uses SQLite for attendance storage and management.

![Database Structure](Submission%20Document/Database%20structuer.png)

### Tables

#### users

Stores:

- User Information
- Credentials
- Roles
- Departments

#### attendance

Stores:

- Attendance Records
- Date
- Check-in Time
- Status

#### login_logs

Stores:

- Login History
- Login Timestamps

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| OpenCV | Face Detection & Recognition |
| Streamlit | Dashboard Interface |
| SQLite | Database |
| Plotly | Analytics |
| NumPy | Numerical Operations |
| Pandas | Data Analysis |
| bcrypt | Password Security |

---

# 📚 Python Libraries

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

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/pritish6015/AI-Face-Recognition-Attendance-System.git
```

## Open Project

```bash
cd AI-Face-Recognition-Attendance-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Application

```bash
streamlit run app.py
```

---

# 🔑 Default Admin Credentials

```text
Username : admin
Password : admin123
```

⚠ Change the password after first login.

---

# 📊 Analytics Features

The system supports:

- Daily Analytics
- Monthly Reports
- Yearly Reports
- Attendance Trends
- Attendance Statistics
- Attendance Monitoring
- Attendance Visualization

---

# 🔒 Security Features

The platform includes enterprise-grade security mechanisms.

![Security Features](Submission%20Document/SECURITY%20FEATURES.png)

### Security Modules

- Password Hashing
- Role-Based Authentication
- Session Management
- Duplicate Attendance Prevention
- Secure Database Storage
- Input Validation

---

# 🚀 Future Enhancement Architecture

Future versions are designed for scalability and enterprise deployment.

![Future Enhancement](Submission%20Document/FUTURE%20ENHANCEMENT.png)

### Planned Enhancements

- DeepFace Integration
- FaceNet Recognition
- Mobile Application
- Cloud Database
- QR Attendance Backup
- CCTV Integration
- Email Notifications
- Department Analytics
- PDF Reports
- REST APIs
- Docker Deployment
- Cloud Hosting

---

# 📂 Generated Files

### AI Models

```text
models/trainer.yml
models/labels.pkl
```

### Dataset Storage

```text
dataset/EMP-001/
dataset/STU-001/
```

---

# 📷 Project Screenshots

## Attendance Workflow

![Attendance Process](Submission%20Document/ATTENDANCE%20MARKING%20PROCESS.png)

## Architecture

![Architecture](Submission%20Document/project%20arc.png)

## Database Structure

![Database](Submission%20Document/Database%20structuer.png)

## Security Features

![Security](Submission%20Document/SECURITY%20FEATURES.png)

## Future Enhancements

![Future](Submission%20Document/FUTURE%20ENHANCEMENT.png)

## Project Structure

![Structure](Submission%20Document/PROJECT%20FILE%20STRUCTURE.png)

---

# 🎯 Advantages

✅ Real-Time Attendance

✅ AI-Based Recognition

✅ Automated Attendance Marking

✅ Interactive Dashboard

✅ Analytics & Reports

✅ Secure Authentication

✅ Lightweight Architecture

✅ Offline Support

✅ Easy Deployment

---

# ⚠ Current Limitations

- Basic LBPH Recognition
- No Face Anti-Spoofing
- SQLite Local Deployment
- Webcam Dependency

---

# 🧠 Learning Outcomes

This project demonstrates:

- Computer Vision
- Machine Learning
- Face Recognition
- Authentication Systems
- Database Design
- Dashboard Development
- Analytics & Reporting
- Streamlit Development

---

# 🤝 Contribution

Contributions are welcome.

Areas for improvement:

- UI/UX Enhancements
- Security Improvements
- AI Accuracy
- Cloud Deployment
- API Development

---

# 📄 License

This project is developed for educational and professional learning purposes.

---

# 👨‍💻 Developer

**Pritish Ghosh**

Developed using:

- Python
- OpenCV
- Streamlit
- SQLite
- Plotly

---

# ⭐ Final Summary

The Enterprise AI Face Recognition Attendance System is a complete AI-powered attendance management solution that combines:

- Artificial Intelligence
- Face Recognition
- Attendance Automation
- Secure Authentication
- Analytics
- Dashboard Monitoring

into a real-world enterprise-ready attendance platform.

⭐ If you found this project useful, consider starring the repository.
