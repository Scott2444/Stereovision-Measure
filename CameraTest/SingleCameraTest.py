"""
This script will test if a single camera is interacting with OpenCV. This file is deprecated as DoubleCameraTest.py does the same thing, but with both cameras at once.

Author: Scott Haakenson
Email: haakens3@msu.edu
"""

import cv2 as cv

# Open the default camera
cam = cv.VideoCapture(0)

# Get the default frame width and height
frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'mp4v')
# out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    # out.write(frame)

    # Display the captured frame
    cv.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
# out.release()
cv.destroyAllWindows()