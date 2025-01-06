"""
This file is where all calculations are performed. Reference the root directory's README.md for documentation.

Author: Scott Haakenson
Email: haakens3@msu.edu
"""

from typing import Tuple  # Used for typing hints
from mmdet.structures.det_data_sample import InstanceData  # Used for typing hints

import globals

class ObjectLength:
    def __init__(self, *, leftPredicitons: InstanceData, rightPredictions: InstanceData, frameWidth: int) -> None:
        """
        :param leftPredicitons: Left camera's predictions
        :type leftPredicitons: InstanceData
        :param rightPredictions: Right camera's predictions
        :type rightPredictions: InstanceData
        :return: None
        :rtype: None
        """
        self._leftPredictions = leftPredicitons
        self._rightPredictions = rightPredictions
        self._frameWidth = frameWidth
        pass

    def calculateLength(self, index: int) -> float:
        pass

    def _calculate_angle(self, pixelX: int) -> float:
        """
        This calculates the angle of a point from the center line of the camera. 
        From the POV of camera, left is a positive angle, right is negative angle.
        Refer to README.md -> Software -> Stereoscopic Vision -> Stereoscopic Vision Math

        :param pixelX: X coordinate of a point
        :type pixelX: int
        :return: None
        :rtype: None
        
        """
        degreesPerPixel = globals.CAMERA_FOV / self._frameWidth
        centerPixel = self._frameWidth // 2
        degreesFromCenter = (centerPixel - pixelX) * degreesPerPixel
        return degreesFromCenter