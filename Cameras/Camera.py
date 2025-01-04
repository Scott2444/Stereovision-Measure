import cv2 as cv
from typing import Literal

class Camera:
    def __init__(self, index: int, position: Literal["Left", "Right"], *, display = True) -> None:
        """
        :param index: Index of the camera in device manager (0 indexed)
        :type index: int
        :param position: Left camera or right camera
        :type position: String
        :return: None
        :rtype: None
        """
        self.cam = cv.VideoCapture(index)
        self.__position = position
        _, frame = self.cam.read()
        self.window = cv.imshow(f"{self.__position} Camera", frame)
    def getFrame(self):
        """
        Capture the current camera image, return it, and display it
        :return: None
        :rtype: None
        """
        _, frame = self.cam.read()
        self.window = cv.imshow(f"{self.__position} Camera", frame)
        return frame
    
    def __del__(self):
        self.cam.release()
        cv.destroyWindow(f"{self.__position} Camera")