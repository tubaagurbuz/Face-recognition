from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime


# Ensure the Attendance directory exists
if not os.path.exists('Attendance'):
    os.makedirs('Attendance')

video = cv2.VideoCapture(0)
# Set the resolution of the camera
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Load labels and face data
with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)

with open('data/face_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

print('Shape of Faces matrix --> ', FACES.shape)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

COL_NAMES = ['NAME', 'TIME']
messages = {}  # Store messages and their timestamps for each person
MESSAGE_DURATION = 5  # Duration in seconds

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)

        predicted_label = output[0]

        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")

        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 255, 50), 2)

        # Put text within the rectangle
        text = f"{predicted_label}\n{timestamp}"
        for i, line in enumerate(text.split('\n')):
            cv2.putText(frame, line, (x, y + h + 20 + i * 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        attendance = [str(predicted_label), str(timestamp)]

        if predicted_label != "unknown":
            messages[predicted_label] = time.time()

            if exist:
                with open("Attendance/Attendance_" + date + ".csv", "a", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(attendance)
            else:
                with open("Attendance/Attendance_" + date + ".csv", "w", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    writer.writerow(attendance)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)

    if k == ord('q') or cv2.getWindowProperty('Frame', cv2.WND_PROP_VISIBLE) < 1:
        break

video.release()
cv2.destroyAllWindows()