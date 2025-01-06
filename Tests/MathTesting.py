"""
This file is for the testing suite of the Calculations classes of this project.

Author: Scott Haakenson
Email: haakens3@msu.edu
"""
import sys
import os

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from Calculations import ObjectLength
from mmdet.structures.det_data_sample import InstanceData
import globals

class PixelAngleFromCenter(unittest.TestCase):
    def test_absoluteLeft(self):
        calculations = ObjectLength(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = globals.CAMERA_FOV / 2  # Left is positive
        self.assertAlmostEqual(calculations._calculate_angle(0), target, delta=0.0001)
        
    def test_absoluteRight(self):
        calculations = ObjectLength(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = -1 * globals.CAMERA_FOV / 2  # Right is negative
        self.assertAlmostEqual(calculations._calculate_angle(calculations._frameWidth), target, delta=0.0001)

    def test_center(self):
        calculations = ObjectLength(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 0.0
        self.assertAlmostEqual(calculations._calculate_angle(calculations._frameWidth // 2), target, delta=0.0001)


print("Starting Test Cases")
unittest.main()