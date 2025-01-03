"""
Main entry for the stereovision software.
"""

import cv2 as cv
from Cameras.Camera import Camera


# The index of the appropriate camera in the Device Manager
CAMERAS_INDEX = {"left": 1, 
                 "right": 0}

leftCamera = Camera(CAMERAS_INDEX["left"], "Left", display=True)
rightCamera = Camera(CAMERAS_INDEX["right"], "Right", display=True)

while True:
    # Press 'c' to capture
    if cv.waitKey(1) == ord('c'):
        leftCamera.getFrame()
        rightCamera.getFrame()

    # Press 'q' to exit the loop
    if cv.waitKey(1) == ord('q'):
        break

