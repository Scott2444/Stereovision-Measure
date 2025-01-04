from mmdet.apis import init_detector, inference_detector
from mmengine.visualization import Visualizer
import mmcv

image_path = 'demo/demo.jpg'

# Init and run the model
config_file = 'rtmdet_tiny_8xb32-300e_coco.py'
checkpoint_file = 'rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth'
model = init_detector(config_file, checkpoint_file, device='cpu')  # or device='cuda:0'
result = inference_detector(model, image_path)


# Print the results
# print(result)
predictions = result.pred_instances
print(predictions)
# print(predictions.bboxes.size())
# print(predictions.scores.size())

# Display the results on the original image
image = mmcv.imread(image_path,
                    channel_order='rgb')
visualizer = Visualizer(image=image)
# single bbox formatted as [xyxy]
visualizer.draw_bboxes(predictions.bboxes[:3])  # Only use top three results
visualizer.show()