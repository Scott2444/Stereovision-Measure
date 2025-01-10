"""
This file is where all calculations are performed. Reference the root directory's README.md for documentation.

Author: Scott Haakenson
Email: haakens3@msu.edu
"""

from typing import Tuple, Literal  # Used for typing hints
from mmdet.structures.det_data_sample import InstanceData  # Used for typing hints
from math import tan, radians

import globals

class ObjectCalculations:
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

    def _calculate_ortho_angle(self, pixelX: int) -> float:
        """
        This calculates the angle of a point from the center line of the camera. 
        From the POV of camera, left is a positive angle, right is negative angle.
        Refer to README.md -> Software -> Stereoscopic Vision -> Stereoscopic Vision Math

        :param pixelX: X coordinate of a point
        :type pixelX: int
        :return: Angle of the point relative to the centerline of the camera in degrees
        :rtype: float
        """
        degreesPerPixel = globals.CAMERA_FOV / self._frameWidth
        centerPixel = self._frameWidth // 2
        degreesFromCenter = (centerPixel - pixelX) * degreesPerPixel
        return degreesFromCenter
    
    def _calculate_interior_angle(self, pixelX: int, position: Literal["Left", "Right"]) -> float:
        """
        This calculates the interior angle of triangle formed between the point and the two cameras
        This is the angle between Camera -> Point and Camera -> Camera.
        0 degrees is facing inwards at the opposite camera, 90 degrees is at the centerline of the camera.
        Refer to README.md -> Software -> Stereoscopic Vision -> Stereoscopic Vision Math

        :param pixelX: X coordinate of a point
        :type pixelX: int
        :param position: Left camera or right camera
        :type position: String
        :return: Interior angle of the triangle formed between the point and the two cameras in degrees
        :rtype: float
        """
        if position == "Left":
            return 90 + self._calculate_ortho_angle(pixelX)
        else:
            return 90 - self._calculate_ortho_angle(pixelX)
        
    def _calculate_point_distance(self, leftCamPixelX: int, rightCamPixelX: int) -> float:
        """
        This calculates the orthogonal distance of a point from the camera mount in mm.
        Refer to README.md -> Software -> Stereoscopic Vision -> Stereoscopic Vision Math

        :param leftCamPixelX: X coordinate on the left camera
        :type leftCamPixelX: int
        :param rightCamPixelX: X coordinate on the right camera
        :type rightCamPixelX: int
        :return: Orthgonal distance of the point in mm
        :rtype: float
        """
        leftInteriorAngle = self._calculate_interior_angle(leftCamPixelX, "Left")
        rightInteriorAngle = self._calculate_interior_angle(rightCamPixelX, "Right")

        if leftInteriorAngle + rightInteriorAngle >= 180.0:
            raise ArithmeticError("Cannot calculate a point's distance. Angles diverage and do not form a triangle.")

        orthoDist = globals.CAMERA_DISTANCE / ((1 / tan(radians(leftInteriorAngle))) + (1 / tan(radians(rightInteriorAngle))))
        return orthoDist
    
    def _calculate_point_offset(self, leftCamPixelX: int, rightCamPixelX: int, *, useLeftCam: bool = False) -> float:
        """
        This calculates distance the point is from the right camera's center line.
        Left of center is positive, Right of center is negative
        Refer to README.md -> Software -> Stereoscopic Vision -> Stereoscopic Vision Math

        :param leftCamPixelX: X coordinate on the left camera
        :type leftCamPixelX: int
        :param rightCamPixelX: X coordinate on the right camera
        :type rightCamPixelX: int
        :param useLeftCam: Calculate offset from left camera's center line
        :type useLeftCam: bool
        :return: Offset of a point from right center in mm
        :rtype: float
        """
        orthoDist = self._calculate_point_distance(leftCamPixelX, rightCamPixelX)
        degreesFromCenter = self._calculate_ortho_angle(rightCamPixelX)
        if useLeftCam:
            degreesFromCenter = self._calculate_ortho_angle(leftCamPixelX)
        offset = orthoDist / ((1 / tan(radians(degreesFromCenter))) + (1 / tan(radians(90))))
        return offset