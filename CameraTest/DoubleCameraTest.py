"""
This script will test if OpenCV is able to capture frames from both cameras.

It is good practice to run this script before running main.py for the first time.

Author: Scott Haakenson
Email: haakens3@msu.edu
"""

import cv2 as cv

# Open the default camera
leftCam = cv.VideoCapture(1)
rightCam = cv.VideoCapture(0)

# Get the default frame width and height
frame_width = int(rightCam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(rightCam.get(cv.CAP_PROP_FRAME_HEIGHT))

print(f"Width: {frame_width} px")
print(f"Height: {frame_height} px")

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
# out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    # Capture a frame and display it
    success, leftFrame = leftCam.read()
    if success:
        cv.imshow('Left Camera', leftFrame)
    else:
        raise RuntimeError("Failed to grab frame from left cam, try to reattach camera")

    success, rightFrame = rightCam.read()
    if success:
        cv.imshow('Right Camera', rightFrame)
    else:
        raise RuntimeError("Failed to grab frame from right cam, try to reattach camera")

    # Press 'q' to exit the loop
    if cv.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
leftCam.release()
rightCam.release()
# out.release()
cv.destroyAllWindows()