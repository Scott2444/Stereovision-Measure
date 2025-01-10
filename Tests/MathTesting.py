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
from Calculations import ObjectCalculations
from mmdet.structures.det_data_sample import InstanceData
import globals


# Testing ObjectCalculations._calculate_ortho_angle()
class PixelAngleFromCenter(unittest.TestCase):
    def test_absoluteLeft(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = globals.CAMERA_FOV / 2  # Left is positive
        self.assertAlmostEqual(calculations._calculate_ortho_angle(0), target, delta=0.0001)
        
    def test_absoluteRight(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = -1 * globals.CAMERA_FOV / 2  # Right is negative
        self.assertAlmostEqual(calculations._calculate_ortho_angle(calculations._frameWidth), target, delta=0.0001)

    def test_center(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 0.0
        self.assertAlmostEqual(calculations._calculate_ortho_angle(calculations._frameWidth // 2), target, delta=0.0001)

# Testing ObjectCalculations._calculate_interior_angle()
class PixelAngleInterior(unittest.TestCase):
    def test_absoluteLeft_leftCam(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 90.0 + globals.CAMERA_FOV / 2
        self.assertAlmostEqual(calculations._calculate_interior_angle(0, "Left"), target, delta=0.0001)
        
    def test_absoluteRight_leftCam(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 90.0 - globals.CAMERA_FOV / 2
        self.assertAlmostEqual(calculations._calculate_interior_angle(calculations._frameWidth, "Left"), target, delta=0.0001)

    def test_center_leftCam(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 90.0
        self.assertAlmostEqual(calculations._calculate_interior_angle(calculations._frameWidth / 2, "Left"), target, delta=0.0001)

    def test_absoluteLeft_rightCam(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 90.0 - globals.CAMERA_FOV / 2
        self.assertAlmostEqual(calculations._calculate_interior_angle(0, "Right"), target, delta=0.0001)
        
    def test_absoluteRight_rightCam(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 90.0 + globals.CAMERA_FOV / 2
        self.assertAlmostEqual(calculations._calculate_interior_angle(calculations._frameWidth, "Right"), target, delta=0.0001)

    def test_center_rightCam(self):
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 90.0
        self.assertAlmostEqual(calculations._calculate_interior_angle(calculations._frameWidth / 2, "Right"), target, delta=0.0001)

# Testing ObjectCalculations._calculate_point_distance()
class PixelOrthoDist(unittest.TestCase):
    def test_isoceles_triangle(self):
        # Both cameras make 80° interior angle
        # An 80° is a 540 pixels on the left side, 100 pixels on the right side
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 545.85 #  in mm
        self.assertAlmostEqual(calculations._calculate_point_distance(540, 100), target, delta=1)

    def test_scalene_triangle(self):
        # Left camera makes 85° interior angle, right camera makes 80° interior angle
        # 430 pixels on the left side, 100 pixels on the right side
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 729.67 #  in mm
        self.assertAlmostEqual(calculations._calculate_point_distance(430, 100), target, delta=1)
    
    def test_obtuse_triangle(self):
        # Left camera makes 95° interior angle, right camera makes 80 interior angle
        # 210 pixels on the right side, 100 pixels on the left side
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 2166.86 #  in mm
        self.assertAlmostEqual(calculations._calculate_point_distance(210, 100), target, delta=1)

    def test_error_handling(self):
        # Points will never converge
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        self.assertRaises(ArithmeticError, calculations._calculate_point_distance, 100, 210)

# Testing ObjectCalculations._calculate_point_offset()
class PixelOffsetDist(unittest.TestCase):
    def test_isoceles_triangle(self):
        # Both cameras make 80° interior angle
        # An 80° is a 540 pixels on the right side, 100 pixels on the left side
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = globals.CAMERA_DISTANCE / 2 #  in mm
        self.assertAlmostEqual(calculations._calculate_point_offset(540, 100), target, delta=0.01)
    
    def test_isoceles_triangle_negative(self):
        # Both cameras make 80° interior angle
        # An 80° is a 540 pixels on the right side, 100 pixels on the left side
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = - 1 * globals.CAMERA_DISTANCE / 2 #  in mm
        self.assertAlmostEqual(calculations._calculate_point_offset(540, 100, useLeftCam=True), target, delta=0.01)

    def test_scalene_triangle(self):
        # Left camera makes 85° interior angle, right camera makes 80° interior angle
        # 430 pixels on the left side, 100 pixels on the right side
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 128.67 #  in mm
        self.assertAlmostEqual(calculations._calculate_point_offset(430, 100), target, delta=0.01)
    
    def test_obtuse_triangle(self):
        # Left camera makes 95° interior angle, right camera makes 80° interior angle
        # 210 pixels on the right side, 100 pixels on the left side
        calculations = ObjectCalculations(leftPredicitons=InstanceData(), rightPredictions=InstanceData(), frameWidth=640)
        target = 382.08 #  in mm
        self.assertAlmostEqual(calculations._calculate_point_offset(210, 100), target, delta=1)

unittest.main()