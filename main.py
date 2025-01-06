"""
Main entry for the stereovision software.
"""

import cv2 as cv
from Cameras.Camera import Camera
from ComputerVision.ObjectDet import ObjectDet
from mmengine.visualization import Visualizer


# The index of the appropriate camera in the Device Manager
CAMERAS_INDEX = {"left": 1, 
                 "right": 0}

# ------------------------------------------------------------------

leftCamera = Camera(CAMERAS_INDEX["left"], "Left", display=True)
rightCamera = Camera(CAMERAS_INDEX["right"], "Right", display=True)

# Get the default frame width and height
frame_width = int(rightCamera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(rightCamera.get(cv.CAP_PROP_FRAME_HEIGHT))

model = ObjectDet()

while True:
    # Press 'c' to capture
    if cv.waitKey(1) == ord('c'):
        leftFrame = leftCamera.getFrame()
        rightFrame = rightCamera.getFrame()
        predictions = model.predict(leftFrame)

        # Frames are np.ndarray type

        # Visualize - TEMPORARY
        visualizer = Visualizer(image=leftFrame)
        # single bbox formatted as [xyxy]
        visualizer.draw_bboxes(predictions.bboxes[:3])  # Only use top three results
        visualizer.show()

    # Press 'q' to exit the loop
    if cv.waitKey(1) == ord('q'):
        break

