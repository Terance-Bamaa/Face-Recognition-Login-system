🧑‍💻 Face Recognition Login System using Python & OpenCV
This is a simple GUI-based face recognition login system built with Python, OpenCV, Tkinter, and the face_recognition library. It allows users to register their face and log in by scanning their face through a webcam.

📌 Features
👤 User Registration with facial capture


🔒 Face-based Login with verification using stored images


🎥 Real-time webcam preview using OpenCV


📝 Logging system that records login time for each user


🖥️ Built with Tkinter GUI



📁 Project Structure
project/
│
├── main.py               # Main app script
├── util.py               # Helper functions for UI components
├── db/                   # Stores registered user face images
├── log.txt               # Logs of successful logins
├── .tmp.jpg              # Temp image used during login


⚙️ Requirements
Python 3.6+


OpenCV (cv2)


face_recognition


Pillow


Tkinter (usually comes with Python)


A webcam


📦 Install Dependencies
pip install opencv-python face_recognition pillow

💡 Note: Installing face_recognition requires dlib and CMake. On Windows, use:
pip install cmake
pip install dlib
pip install face_recognition


▶️ How It Works
🔑 Login
Press Login.


Webcam captures your face.


If a match is found in the ./db folder, login succeeds.


Your name and timestamp are written to log.txt.


🧍 Register New User
Press Register new User.


Enter your name.


Your image is captured and saved in ./db.


You can now log in with your face.



🛠️ Notes
The application uses subprocess to call the face_recognition CLI.


Make sure the CLI is installed and available in your system path.

Screenshots
<img width="901" height="414" alt="image" src="https://github.com/user-attachments/assets/d68e5183-b953-4e5b-b5bd-87a3e9c735bb" />



📄 License
This project is for educational purposes only. You may reuse and modify it freely.
