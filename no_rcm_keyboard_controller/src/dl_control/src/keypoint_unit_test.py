#!/usr/bin/env python3
from __future__ import print_function, division
import torch
import numpy as np
import torch.nn as nn

import cv2
import os
from pathlib import Path

import torchvision.transforms.functional as TF
from torchvision import models
import warnings; warnings.simplefilter('ignore')

import math
import time

import sys
sys.path.append('/home/peiyao/peiyao/record_images/src/record_images/src')
from image_conversion_without_using_ros import image_to_numpy
import matplotlib.pyplot as plt
import os
from ultralytics import YOLO
from torchvision.models import resnet18
from torchvision.transforms import Compose, Resize, ToTensor, Normalize

from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
# from no_rcm_key_publisher_msgs.msg import no_rcm_key_publisher_msgs
import shutil
from matplotlib import pyplot as plt
from PIL import Image
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


x = None
y = None
z = None
rx = None
ry = None
rz = None
rw = None

camera_image = None
user_defined_target_point = None
b_scan_raw = None




#just for test


# # Example paths (replace with your actual file paths)

# b_scan_raw_path = '/home/peiyao/data/b_scans_1720991255.83/b_scans_1092.jpg'

# # # # # Load images using OpenCV
# # # # # camera_image = cv2.imread(camera_image_path)
# b_scan_raw = cv2.imread(b_scan_raw_path)
# print(b_scan_raw.shape)

# # height, width, channels = b_scan_raw.shape
# # print(f"Image shape: {height} x {width} x {channels}")

# # # Determine the depth of the image (data type of array)
# # depth = b_scan_raw.dtype
# # print(f"Image depth: {depth}")


# Camera network (Detectron2)
cfg = get_cfg()
cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
cfg.merge_from_file(model_zoo.get_config_file("COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 64
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  # only one class (needle tip)
cfg.MODEL.ROI_KEYPOINT_HEAD.NUM_KEYPOINTS = 1
cfg.MODEL.WEIGHTS = "//home/peiyao/peiyao/DL_control_depend_yi/model_final.pth"
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.DATASETS.TEST = ("needle_tip_val", )
predictor = DefaultPredictor(cfg)



# B-scan contact network
model_contact = resnet18(weights=None)
num_features = model_contact.fc.in_features
model_contact.fc = torch.nn.Linear(num_features, 2)
checkpoint_contact = torch.load('/home/peiyao/peiyao/DL_control_depend_yi/resnet_contact_classifier.pth')
model_contact.load_state_dict(checkpoint_contact)
# model_contact = model_contact.eval()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model_contact = model_contact.to(device).eval()
transform_contact = Compose([
    Resize((224, 224)),
    ToTensor(),
    Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])



#puncture model
weights_path = '/home/peiyao/peiyao/DL_control_depend_yi/best_no_aug_8l.pt'  # Update with the actual path to your model weights
model = YOLO(weights_path)


# ## test for navigation
# camera_image_dir = '/home/peiyao/data/camera_image_1722633156.26'
# camera_images = []

# start_index = 316
# end_index = 2356
# counter = 0

# tip_x = 0
# tip_y = 0

# for img_idx in range(start_index, end_index+1):
#     img_path = f'{camera_image_dir}{img_idx}.jpg'
#     camera_image = cv2.imread(img_path)



#     input_image_np = camera_image
#     input_image_np_rgb = cv2.cvtColor(input_image_np, cv2.COLOR_BGR2RGB)
#     # plt.imshow(input_image_np_rgb)
#     # plt.show()
#     input_image = cv2.resize(input_image_np , (512, 512)) 

#     start_time = time.time()

#     outputs = predictor(input_image)
#     instances = outputs["instances"].to("cpu")
#     keypoints = instances.pred_keypoints if instances.has("pred_keypoints") else None
#     scores = instances.scores if instances.has("scores") else None
#     if keypoints.numel() != 0:
#         if keypoints is not None and scores is not None:
#             counter += 1
#             max_score_idx = np.argmax(scores.numpy())
#             print(keypoints[max_score_idx])
#             tip_x=keypoints[max_score_idx][0,0].item()
#             tip_y = keypoints[max_score_idx][0,1].item()
#             print("tip_x:", tip_x)
#             print("tip_y", tip_y)
#             print("Inference time:", time.time() - start_time)
#     else:
#         print("no keypoint detected")
        
#     # # Visualize the results
#     v = Visualizer(input_image[:, :, ::-1],
#                 metadata=MetadataCatalog.get("needle_tip_val"),
#                 scale=1.2)
#     v = v.draw_instance_predictions(outputs["instances"].to("cpu"))

# #Display the image with predictions

#     cv2.arrowedLine(input_image, (int(tip_x),int(tip_y)), (20,20), color=(255,0,0),thickness=12, tipLength=0.2)

#     cv2.imshow('inference result',input_image)

#     key = cv2.waitKey(1)

#     # Check if the user pressed 'q' to quit
#     if key == ord('q'):
#         break
# print(counter)
# cv2.destroyWindow('inference result')



## test for contact

# count=0
# images_dir ='/home/peiyao/data/b_scans_1722633449.74'
# # List all files in the directory
# image_files = [os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.png')]

# # Run inference on each image
# for image_path in image_files:
#     # Load and transform the image
#     image = Image.open(image_path).convert('RGB')
#     input_tensor = transform_contact(image).to(device)

#     # Add batch dimension
#     input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension

#     # Forward pass: predict the label
#     with torch.no_grad():
#         output = model_contact(input_batch)
#         prediction = output.argmax(dim=1).item()
#         probabilities = torch.softmax(output, dim=1) 
#         confidence_score = torch.max(probabilities).item()
#     if prediction == 1:
#         count +=1

#     # Print the filename and predicted label
#     filename = os.path.basename(image_path)
#     print(f'File: {filename}, Predicted label: {prediction}')
#     print(probabilities)
#     print(confidence_score)



# print(count)

# puncture test
def process_b_scan(image_path, device):
    # Load the image in grayscale
    b_scan = cv2.imread(image_path)

    if b_scan is None:
        print(f"Error: Unable to load image from {image_path}")
        return None, None

    # Resize the image
    b_scan = cv2.resize(b_scan, (640, 640))
    # Convert to tensor
    b_scan_tensor = TF.to_tensor(b_scan)  # C x H x W
    b_scan_tensor = b_scan_tensor.unsqueeze(0).float().to(device)  # N x C x H x W

    # Save the processed image temporarily for detect.py
    temp_image_path = "temp_b_scan_1.jpg"
    cv2.imwrite(temp_image_path, b_scan)

    return b_scan_tensor, temp_image_path

punc_dir ='/home/peiyao/data/b_scans_1722642246.59'

image_files = [os.path.join(punc_dir, f) for f in os.listdir(punc_dir) if f.endswith('.jpg') or f.endswith('.png')]
image_files = image_files[2709:2800]
error = 0
for image_path in image_files:
    processed_b_scan, temp_image_path = process_b_scan(image_path, device)
    results = model.predict(source=temp_image_path,conf=0.01)

    # # Visualization function
    # def visualize_predictions(image_path, results):
    #     image = cv2.imread(image_path)
    #     for result in results:
    #         for box in result.boxes:
    #             x1, y1, x2, y2 = [int(coord) for coord in box.xyxy[0]]  # Extract coordinates correctly
    #             class_id = int(box.cls.item())
    #             confidence = box.conf.item()
    #             label = f"Class {class_id}: {confidence:.2f}"
    #             cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #             cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
    #     plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #     plt.show()

    # visualize_predictions(temp_image_path, results)
    highest_confidence = -1
    highest_confidence_class_id = None

    # Extract class ID with the highest confidence score
    for result in results:

        for box in result.boxes:

            confidence = box.conf.item()
            highest_confidence_class_id = int(box.cls.item())
            print('1')
            if confidence > highest_confidence:
                highest_confidence = confidence
                highest_confidence_class_id = int(box.cls.item())
    if highest_confidence_class_id == None:
        error +=1

# List all files in the directory
# image_files = [os.path.join(punc_dir, f) for f in os.listdir(punc_dir) if f.endswith('.jpg') or f.endswith('.png')]
# error = 0
# # Run inference on each image
# for image_path in image_files:
#     processed_b_scan, temp_image_path = process_b_scan(image_path, device)
#     # Run inference on the resized image
#     results = model.predict(source=temp_image_path)

#     # Initialize variables to keep track of the highest confidence bounding box
#     highest_confidence = -1
#     highest_confidence_class_id = None

#     # Extract class ID with the highest confidence score
#     for result in results:
#         for box in result.boxes:
#             confidence = box.conf.item()
#             if confidence > highest_confidence:
#                 highest_confidence = confidence
#                 highest_confidence_class_id = int(box.cls.item())
    
    
#     filename = os.path.basename(image_path)
#     print(f'File: {filename}, Predicted label: {highest_confidence_class_id}')
#     if highest_confidence_class_id ==None:
#         error+=1

# print(error)        


















# result_image_path = "/home/peiyao/peiyao/DL_control_depend_yi/b_scans_puncture_{}.jpg".format(0)
# # print(b_scan.shape[2])
# # cv2.imwrite(result_image_path, b_scan)
# processed_b_scan, temp_image_path = process_b_scan(result_image_path, device)
# # print(temp_image_path)
# run_yolov5_inference(yolov5_dir, weights_path, result_image_path)
# print("run")
# latest_results_dir = get_latest_results_dir(yolov5_dir)
# results_file_path = latest_results_dir / 'labels' / 'b_scans_puncture_0.txt'
# if results_file_path.exists():
#     class_id, confidence = extract_class_ids_and_confidence(results_file_path)
#     print("confidence",confidence)
#     print("Detected class IDs:", class_id)
# # # ##just for test




# Ensure b_scan_raw_cv is a numpy array
  














# # Function to get the latest results directory
# def get_latest_results_dir(yolov5_dir, base_dir='runs/detect'):
#     full_base_dir = Path(yolov5_dir) / base_dir
#     dirs = [d for d in full_base_dir.iterdir() if d.is_dir()]
#     latest_dir = max(dirs, key=os.path.getmtime)
#     return latest_dir

# # # Function to extract class IDs from the results file
# # def extract_class_ids(results_file_path):
# #     class_ids = []
# #     with open(results_file_path, 'r') as file:
# #         for line in file:
# #             class_id = int(line.split()[0])
# #             class_ids.append(class_id)
# #     return class_ids
# # Function to extract class IDs and confidence from the results file
# def extract_class_ids_and_confidence(results_file_path):
#     class_ids = []
#     confidences = []
#     highest_confidence = -1.0
#     corresponding_class_id = -1
#     with open(results_file_path, 'r') as file:
#         for line in file:
#             data = line.split()
#             if len(data) >= 6:  # Check if the line has the expected format
#                 class_ids.append(int(data[0]))
#                 confidences.append(float(data[-1]))  # Extracting confidence (index 4 in default YOLOv5 format)

#             else:
#                 print(f"Warning: Line '{line.strip()}' does not have enough elements for parsing.")


#     for i in range(len(confidences)):
#         confidence = confidences[i]
#         class_id = class_ids[i]

#         if confidence > highest_confidence:
#             highest_confidence = confidence
#             corresponding_class_id = class_id

#     return corresponding_class_id, highest_confidence
# Function to process the B-scan image


# def process_b_scan(image_path, device):
#     # Load the image in grayscale
#     b_scan = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#     if b_scan is None:
#         print(f"Error: Unable to load image from {image_path}")
#         return None, None

#     # Resize the image
#     b_scan = cv2.resize(b_scan, (640, 640))
#     # Convert to tensor
#     b_scan_tensor = TF.to_tensor(b_scan)  # C x H x W
#     b_scan_tensor = b_scan_tensor.unsqueeze(0).float().to(device)  # N x C x H x W

#     # Save the processed image temporarily for detect.py
#     temp_image_path = "temp_b_scan_1.jpg"
#     cv2.imwrite(temp_image_path, b_scan)

#     return b_scan_tensor, temp_image_path

# # Function to run YOLOv5 inference
# def run_yolov5_inference(yolov5_dir, weights_path, image_path):
#     detect_script = os.path.join(yolov5_dir, 'detect.py')
#     os.system(f'python {detect_script} --weights {weights_path} --source {image_path} --conf 0.1 --iou 0.1 --save-txt --save-conf')



# yolov5_dir = "/home/peiyao/peiyao/DL_control_depend_yi/yolov5"  # Update with the absolute path to your YOLOv5 directory
# weights_path = '/home/peiyao/peiyao/DL_control_depend_yi/best.pt'  # Path to your YOLOv5 weights file




# image = Image.open(b_scan_raw_path).convert('RGB')


# # Apply the transformation
# input_tensor = transform_contact(image).to(device)

# # Add batch dimension
# input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension

# # Forward pass: predict the label
# with torch.no_grad():  # No need to compute gradients
#     output = model_contact(input_batch)
#     prediction = output.argmax(dim=1) 
#     probabilities = torch.softmax(output, dim=1) 
#     confidence_score = torch.max(probabilities).item() # Assuming output is logits or scores

# print(f'Predicted label: {prediction.item()}')
# print("confi",confidence_score)



# np_arr = np.frombuffer(data.data, np.uint8)
# cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

# # Convert OpenCV image to PIL image
# pil_image = PILImage.fromarray(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB))

# # Apply the transformation
# input_tensor = transform(pil_image)

# # Add batch dimension
# input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension

# # Forward pass: predict the label
# with torch.no_grad():  # No need to compute gradients
#     output = model(input_batch)
#     prediction = output.argmax(dim=1)  # Assuming output is logits or scores

# print(f'Predicted label: {prediction.item()}')



# print("image shown here")


# input_image = image_to_numpy(camera_image)
# input_image = cv2.resize(input_image , (512, 512)) 
# plt.imshow(input_image)
# plt.show()
# outputs = predictor(input_image)
# instances = outputs["instances"].to("cpu")
# keypoints = instances.pred_keypoints if instances.has("pred_keypoints") else None
# print("looking for keypoints")
# print(keypoints)
#b_scan = image_to_numpy(b_scan_raw)