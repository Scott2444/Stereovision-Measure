from mmdet.apis import init_detector, inference_detector
from mmengine.visualization import Visualizer
import mmcv
from typing import Literal
import os

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
    def predict(self, frame):
        """
        Run the frame through the object detection model

        :param device: Index of the camera in device manager (0 indexed)
        :type device: int
        :return: Scores, Bounding Boxes, and Labels predicted from the model
        :rtype: InstanceData
        """
        print("Beginning inference")
        results = inference_detector(self.model, frame)
        print(results)
        return results.pred_instances