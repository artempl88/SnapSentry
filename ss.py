import sys
import time
import os
import smtplib
import keyboard
import cv2
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def start_webcam():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Failed to open webcam")
        sys.exit()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("webcam_recording.avi", fourcc, 20.0, (640,480))
    start_time = datetime.now()
    prev_frame = None
    timer = 0
    recording = False

    keyboard.add_hotkey('ctrl+alt+q', stop_webcam)

    while True:
        ret, frame = camera.read()
        if not ret:
            break
        if recording:
            out.write(frame)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if prev_frame is None:
            prev_frame = frame_gray
            continue
        delta_frame = cv2.absdiff(prev_frame, frame_gray)
        thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
        cnts = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        movement = False
        for c in cnts:
            if cv2.contourArea(c) < 5000:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            movement = True
        if movement:
            timer = 0
            if not recording:
                recording = True
                start_time = datetime.now()
                print("Started recording...")
            if recording:
                out.write(frame)
        else:
            timer += 1
            if timer == 100:  # 5 minutes
                end_time = datetime.now()
                print("No movement for 5 minutes, stopped recording: ", end_time)
                recording = False
                break
        prev_frame = frame_gray
        if cv2.waitKey(1) & 0xFF == ord('q'):
            end_time = datetime.now()
            print("Recording stopped: ", end_time)
            recording = False
            break
    
    keyboard.remove_hotkey('ctrl+alt+q')
    camera.release()
    out.release()
    cv2.destroyAllWindows()
    send_email()

def stop_webcam():
    end_time = datetime.now()
    print("Recording stopped: ", end_time)
    keyboard.remove_hotkey('ctrl+alt+q')
    sys.exit()

def send_email():
    from_email = "YOUR_EMAIL_HERE"
    from_password = "YOUR_PASSWORD_HERE"
    to_email = "MAIL_TO_HERE"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Motion detected!"

    with open("webcam_recording.avi", "rb") as f:
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload((f).read())

    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename="webcam_recording.avi")
    msg.attach(attachment)

    s = smtplib.SMTP('YOUR_SMTP_HERE', 587)
    s.starttls()
    s.login(from_email, from_password)
    s.sendmail(from_email, to_email, msg.as_string())
    s.quit()
    print("Email sent!")

if __name__ == "__main__":
    start_webcam()    
