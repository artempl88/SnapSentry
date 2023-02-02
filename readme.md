# SnapSentry
<p align="center">
<img src="https://github.com/artempl88/SnapSentry/blob/main/SnapSentry_logo.png">
</p>
SnapSentry is a script designed to help you keep your property secure if you don't have the money to install an expensive video surveillance system. It uses your webcam to capture images and detect any unauthorized activity.

## Features
Real-time motion detection
Email alerts with snapshots of the detected activity
Easy installation and setup
Compatible with most webcams
Detects unauthorized activity using your webcam
Captures images for evidence
Sends notifications of any suspicious activity

## System Requirements
Windows, Mac, or Linux operating system
A webcam connected to your computer
Python 3 installed on your computer

## Installation and Setup
To install SnapSentry, you will need to have the following dependencies installed on your system:

Python 3
OpenCV

Once you have these dependencies installed, you can clone the repository and run the script using the following steps:

1. Clone the repository:
```git clone https://github.com/artempl88/snapsentry.git```

2. Change into the project directory:
```cd webcam-thief-catcher```

3. Install the required packages by the command ```pip install <required package>```:
- sys
- time
- os
- smtplib
- keyboard
- cv2 (OpenCV)
- email
- datetime

4. Update the email configuration in the script to receive email alerts.

5. Run the script with the command ```python ss.py``` or ```python3 ss.py``` depending on your version of Python.

6. Your webcam will start monitoring for any unauthorized activity and send an email alert with a snapshot of the detected activity.

## Limitations
The script may not detect all movements accurately, especially in low-light conditions.
The script may not be able to send email alerts if your email provider blocks the use of unsecured SMTP servers.

## Support
For any questions or concerns, please open an issue in the repository or send an email to the provided email address. We will do our best to assist you.
