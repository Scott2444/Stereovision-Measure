"""
This file contains the wrapper class of OpenCV's camera functionality.

Author: Scott Haakenson
Email: haakens3@msu.edu
"""

import cv2 as cv
import numpy as np
from typing import Literal

class Camera:
    def __init__(self, index: int, position: Literal["Left", "Right"], *, display = True) -> None:
        """
        :param index: Index of the camera in device manager (0 indexed)
        :type index: int
        :param position: Left camera or right camera
        :type position: String
        :param display: Display captured frames in a window
        :type display: bool
        :return: None
        :rtype: None
        """
        self.cam = cv.VideoCapture(index)
        self.__position = position
        success, frame = self.cam.read()
        self.display = display
        if success and self.display:
            cv.imshow(f"{self.__position} Camera", frame)
        if not success:
            raise RuntimeError(f"Failed to grab frame from {self.__position} Cam, try to reconnect")
        return None
    
    def getFrame(self) -> np.ndarray:
        """
        Capture the current camera image, return it, and display it
        :return: Frame from the camera
        :rtype: np.ndarray
        """
        success, frame = self.cam.read()
        if success and self.display:
            cv.imshow(f"{self.__position} Camera", frame)
        if not success:
            raise RuntimeError(f"Failed to grab frame from {self.__position} Cam, try to reconnect")
        return frame
    
    def __del__(self) -> None:
        self.cam.release()
        cv.destroyWindow(f"{self.__position} Camera")
        return None