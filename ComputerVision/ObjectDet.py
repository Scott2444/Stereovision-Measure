"""
This file contains the wrapper class of the Object Detection ML Model.

The model is pretrained from OpenMMLabs which can be found here: https://github.com/open-mmlab/mmdetection

The process of downloading and preparing the model to be run locally can be found here: https://mmdetection.readthedocs.io/en/latest/get_started.html

Author: Scott Haakenson
Email: haakens3@msu.edu
"""

from mmdet.apis import init_detector, inference_detector
import os
import numpy as np  # Used for typing hints
from typing import Literal  # Used for typing hints
from mmdet.structures.det_data_sample import DetDataSample, InstanceData  # Used for typing hints

config_file = os.path.join("ComputerVision", "rtmdet_tiny_8xb32-300e_coco.py")
checkpoint_file = os.path.join("ComputerVision", "rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth")

class ObjectDet:
    def __init__(self, device: Literal["cpu", "cuda:0"] = "cpu"):
        """
        :param device: Index of the camera in device manager (0 indexed)
        :type device: int
        :return: None
        :rtype: None
        """
        self.model = init_detector(config_file, checkpoint_file, device=device)
    def predict(self, frame: np.ndarray) -> InstanceData:
        """
        Run the frame through the object detection model

        :param device: Index of the camera in device manager (0 indexed)
        :type device: int
        :return: Scores, Bounding Boxes, and Labels predicted from the model
        :rtype: InstanceData
        """
        results = inference_detector(self.model, frame)
        print(results)
        return results.pred_instances