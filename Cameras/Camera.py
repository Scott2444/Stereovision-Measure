import cv2 as cv
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
        _, frame = self.cam.read()
        cv.imshow(f"{self.__position} Camera", frame)
    def getFrame(self):
        """
        Capture the current camera image, return it, and display it
        :return: Frame from the camera
        :rtype: MatLike
        """
        _, frame = self.cam.read()
        cv.imshow(f"{self.__position} Camera", frame)
        return frame
    
    def __del__(self):
        self.cam.release()
        cv.destroyWindow(f"{self.__position} Camera")