#!/usr/bin/env python3
from __future__ import print_function, division
import torch
import numpy as np
import torch.nn as nn
import cv2
import os
from pathlib import Path
# from cv_bridge import CvBridge
import torchvision.transforms.functional as TF
from torchvision import models
import warnings; warnings.simplefilter('ignore')
from geometry_msgs.msg import Vector3, Transform
from sensor_msgs.msg import Image as ROSImage
import rospy
import math
import time
from scipy.spatial.transform import Rotation as R
from geometry_msgs.msg import Twist, Vector3
import sys
sys.path.append('/home/peiyao/peiyao/record_images/src/record_images/src')
from image_conversion_without_using_ros import image_to_numpy
import matplotlib.pyplot as plt
import os
from ultralytics import YOLO
from torchvision.models import resnet18
from torchvision.transforms import Compose, Resize, ToTensor, Normalize
from PIL import Image as PILImage
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
# from no_rcm_key_publisher_msgs.msg import no_rcm_key_publisher_msgs
import copy




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



class subscribe_image_and_goal:

    def __init__(self):
        self.camera_img_sub = rospy.Subscriber("/decklink/camera/image_raw", ROSImage, self.get_camera_image)
        self.clicked_goal_sub = rospy.Subscriber("/click_goal", Vector3, self.get_target_point)
        # FrameEE: tip position and angular value of robot
        # self.key_sub = rospy.Subscriber("/no_rcm_key_input", no_rcm_key_publisher_msgs, self.get_key_input)
        self.tool_tip_position_sub = rospy.Subscriber("/eye_robot/FrameEE", Transform, self.get_tool_tip_position)
        self.b_scan_sub = rospy.Subscriber("/b_scan", ROSImage, self.get_b_scan)

    def get_camera_image(self, data):
        global camera_image
        # bridge = CvBridge()
        # camera_image = bridge.imgmsg_to_cv2(data, "bgr8")
        camera_image = data

    def get_b_scan(self, data):
        global b_scan_raw
        b_scan_raw = data

    def get_target_point(self, data):
        global user_defined_target_point
        user_defined_target_point = data
        print("select code, print clicked goal: ", user_defined_target_point)

    def get_tool_tip_position(self, data):
        global x
        global y
        global z
        global rx
        global ry
        global rz
        global rw
        x = data.translation.x
        y = data.translation.y
        z = data.translation.z
        rx = data.rotation.x
        ry = data.rotation.y
        rz = data.rotation.z
        rw = data.rotation.w



def create_publisher():
  """
      Usage:
        publisher = create_publisher()
        publisher.publish(desired_position[0], desired_position[1], desired_position[2])
  """
  pub_tip_vel = rospy.Publisher('/eyerobot2/desiredTipVelocities', Vector3, queue_size = 3)
  pub_tip_vel_angular = rospy.Publisher('/eyerobot2/desiredTipVelocitiesAngular', Vector3, queue_size = 3)
  return pub_tip_vel,pub_tip_vel_angular


subscribe_image_and_goal()
pub_tip_vel, pub_tip_vel_angular = create_publisher()
rospy.init_node('move', anonymous=True)
rate = rospy.Rate(100) # 100hz




#keyboard control
# Move needle to desired position 
kp_linear_vel = 2
kp_angular_vel = 3
insertion_angle = 20 * math.pi / 180
linear_vel = 0.1
diff_angle_thresh = 0.1 * math.pi / 180

current_quat = np.array((rx, ry, rz, rw))
r_current = R.from_quat(current_quat)
rotation_matrix_current = r_current.as_matrix()
vector_cur = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
xy_sqrt = math.sqrt(vector_cur[0]**2 + vector_cur[1]**2)
vector_desired = np.array((vector_cur[0] * math.sin(insertion_angle) / xy_sqrt, vector_cur[1] * math.sin(insertion_angle) / xy_sqrt, -math.cos(insertion_angle)))
vector_cross = np.cross(vector_cur, vector_desired)
c = np.dot(vector_cur, vector_desired)
v_matrix = np.array([[0, -vector_cross[2], vector_cross[1]], [vector_cross[2], 0, -vector_cross[0]], [-vector_cross[1], vector_cross[0], 0]])
rotation_matrix_error = np.identity(3) + v_matrix + np.matmul(v_matrix, v_matrix) / (1 + c)
r_error = R.from_matrix(rotation_matrix_error)
error_rotation_vector = r_error.as_rotvec()
unit_error_rotation_vector = error_rotation_vector / np.linalg.norm(error_rotation_vector)

linear_vel_gain = 0.08
angular_vel_gain = 0.08

while (np.linalg.norm(error_rotation_vector) >= 0.03):
    angular_vel = unit_error_rotation_vector * angular_vel_gain
    current_quat = np.array((rx, ry, rz, rw))
    r_current = R.from_quat(current_quat)
    rotation_matrix_current = r_current.as_matrix()
    vector_cur = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
    xy_sqrt = math.sqrt(vector_cur[0]**2 + vector_cur[1]**2)
    vector_desired = np.array((vector_cur[0] * math.sin(insertion_angle) / xy_sqrt, vector_cur[1] * math.sin(insertion_angle) / xy_sqrt, -math.cos(insertion_angle)))
    vector_cross = np.cross(vector_cur, vector_desired)
    c = np.dot(vector_cur, vector_desired)
    v_matrix = np.array([[0, -vector_cross[2], vector_cross[1]], [vector_cross[2], 0, -vector_cross[0]], [-vector_cross[1], vector_cross[0], 0]])
    rotation_matrix_error = np.identity(3) + v_matrix + np.matmul(v_matrix, v_matrix) / (1 + c)
    r_error = R.from_matrix(rotation_matrix_error)
    error_rotation_vector = r_error.as_rotvec()
    unit_error_rotation_vector = error_rotation_vector / np.linalg.norm(error_rotation_vector)
    print("Angular ERROR: ", np.linalg.norm(error_rotation_vector))
    pub_tip_vel_angular.publish(angular_vel[0], angular_vel[1], angular_vel[2])
    rate.sleep()

pub_tip_vel.publish(0, 0, 0)
pub_tip_vel_angular.publish(0, 0, 0)
print("You can control the robot now!")


# Camera network (Detectron2)
cfg = get_cfg()
cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
cfg.merge_from_file(model_zoo.get_config_file("COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 64
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  # only one class (needle tip)
cfg.MODEL.ROI_KEYPOINT_HEAD.NUM_KEYPOINTS = 1
cfg.MODEL.WEIGHTS = "//home/peiyao/peiyao/DL_control_depend_yi/model_final_larger_bbox.pth"
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


## puncture

weights_path = '/home/peiyao/peiyao/DL_control_depend_yi/best_no_aug_8l.pt'  # Update with the actual path to your model weights
model = YOLO(weights_path)


def ros_imgmsg_to_cv2(image_msg):
    # b scan is 64FC1: 64 bit depth with floating point and single channel

    dtype = np.dtype("float64")  # Adjust dtype as per your image format
    data = np.fromstring(image_msg.data, dtype=dtype)
    image_np = data.reshape((image_msg.height, image_msg.width))

    # encoding = image_msg.encoding

    # Normalize to 0-1
    image_np_normalized = (image_np - np.min(image_np)) / (np.max(image_np) - np.min(image_np))
    
    # Scale to 0-255 and convert to uint8
    image_uint8 = (image_np_normalized * 255).astype(np.uint8)
    
    return image_uint8

   


sz = 20
# gain value
pub_tip_vel, pub_tip_vel_angular = create_publisher()
rospy.init_node('move', anonymous=True)
rate = rospy.Rate(100) # 100hz
kp_linear_vel = 2 # used to be 1.5 01/26/2023
# set up insertion angle from the no_rcm_keyboard_controller
#kp_angular_vel = 3 # 1.0, 2, 0.005, 1.5, 0.015
downward_linear_vel = 2
#downward_angular_vel = 3
downward_flag = False
#move_angle = 0 * math.pi / 180 # set the tool-tip bended angle default 20
forward_step_size = 0.3
linear_vel = 0.1
# top_k = 10
# desired_index = 1
### change it each time!
linear_vel_gain = 0.08
pub_tip_vel.publish(0, 0, 0)
time_keeper = []



print("Start navigation!")
start = time.time()

from matplotlib import pyplot as plt


argmax_output_contact = 0
target_point = None
pub_tip_vel.publish(Vector3(0,0,0))
while not rospy.is_shutdown():
    # fig.canvas.draw()
    # fig.canvas.flush_events()
    # plt.show()
    # plt.pause(0.01)
    # ax.cla() 


    if user_defined_target_point is None and target_point is None:
        print("Click goal not received")
        rate.sleep()
        continue

    elif user_defined_target_point is not None:
        target_point = [user_defined_target_point.x, user_defined_target_point.y]

    elif user_defined_target_point is None and target_point is not None:
        pass
    


    if b_scan_raw is not None:
        # Contact detection

        np_arr = np.frombuffer(b_scan_raw.data, dtype=np.float64)  # Assuming 64-bit floating point
        cv_image = np_arr.reshape((b_scan_raw.height, b_scan_raw.width)).astype(np.float32)

        # Normalize the float image to uint8 range (0-255)
        cv_image_uint8 = cv2.normalize(cv_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        # Convert single-channel image to RGB
        cv_image_rgb = cv2.cvtColor(cv_image_uint8, cv2.COLOR_GRAY2RGB)

        # Convert OpenCV image to PIL image
        pil_image = PILImage.fromarray(cv_image_rgb)

        # Apply the transformation
        input_tensor = transform_contact(pil_image)

        # Add batch dimension if necessary
        input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension if needed
        

        # Navigation inference
        # Convert ROS Image message to numpy array (RGB8)
        img_np = np.frombuffer(camera_image.data, dtype=np.uint8).reshape(camera_image.height, camera_image.width, -1)

        # Resize the image to 512x512
        resized_image = cv2.resize(img_np, (512, 512))

        # Convert RGB image to BGR (OpenCV uses BGR by default)
        input_image= cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR)

        # # Display or process the resized BGR image as needed
        # cv2.imshow('Resized BGR Image', resized_image_bgr)
        # cv2.waitKey(0)  # Wait indefinitely for a key press
        # cv2.destroyAllWindows()

        # input_image_np = np.array(image_to_numpy(camera_image))
        # #input_image_np = camera_image 
        # print(camera_image.encoding)
        # print(input_image_np.shape())
        # input_image = cv2.resize(camera_image , (512, 512)) 
   
        if argmax_output_contact == 0:


            #input_image = camera_image   
            outputs = predictor(input_image)
            instances = outputs["instances"].to("cpu")
            keypoints = instances.pred_keypoints if instances.has("pred_keypoints") else None
            scores = instances.scores if instances.has("scores") else None
            # print("looking for keypoints")
            # print(keypoints)

        
            if keypoints.numel() == 0:
                print("No Keypoint detected, continuing...")
                random_needle_vel = linear_vel * np.random.randn(2)
                pub_tip_vel.publish(Vector3(random_needle_vel[0], random_needle_vel[1], 0))
                # print("moving the needle in a random velocity", random_needle_vel)
                cv2.imshow('inference result', input_image)
                key = cv2.waitKey(1)
                rate.sleep()
                continue
            elif keypoints is not None and scores is not None:
                max_score_idx = np.argmax(scores.numpy())
                print(keypoints[max_score_idx])
                tip_x=keypoints[max_score_idx][0,0].item()
                tip_y = keypoints[max_score_idx][0,1].item()
                print("tip_x:", tip_x)
                print("tip_y", tip_y)

                # target_x, target_y = user_defined_target_point.x, user_defined_target_point.y

                # Calculate the movement vector from tip to target
                vector_x = target_point[0] - tip_x
                vector_y = target_point[1] - tip_y
                angle = np.arctan2(vector_y, vector_x)
                

                # Overay the vector on the image
                arrow_start = (tip_x, tip_y)
                arrow_direction = (vector_x, vector_y)
                # ax.arrow(*arrow_start, *arrow_direction, color='blue', width=2, head_width=12)


                # negative sign is for aligning the axes of camera and robot
                horizontal_linear_vel_x = -1*kp_linear_vel * linear_vel * np.cos(angle)
                horizontal_linear_vel_y = -1*kp_linear_vel * linear_vel * np.sin(angle)

                distance_to_target = np.hypot(vector_x, vector_y)

                if distance_to_target < 5:
                    # downward_flag = True
                    print("final_tip_x:", tip_x)
                    print("final_tip_y", tip_y)
                    kp_linear_vel = 0.3

                    # switch the direction to align the axes
                    pub_tip_vel.publish(
                        Vector3(0,0, -downward_linear_vel * linear_vel)
                    )
                    time.sleep(3)
                    pub_tip_vel.publish(Vector3(0,0,0))
                    input("ready for B-scan image...")
                    # pub_tip_vel.publish(Vector3(0,0,0))
                    with torch.no_grad():
                        input_batch = input_batch.to(device)  # No need to compute gradients
                        output = model_contact(input_batch)
                        argmax_output_contact = output.argmax(dim=1).item()
                        probabilities = torch.softmax(output, dim=1) 
                        confidence_score = torch.max(probabilities).item()
                    print("argmax_output_contact = ", argmax_output_contact)
                    print("confidence_score",confidence_score)
                    # if confidence_score <= 0.75:
                    #     argmax_output_contact = 0

                    
                else:
                    # switch the direction to align the axes

                    pub_tip_vel.publish(
                        Vector3(horizontal_linear_vel_y, horizontal_linear_vel_x, 0)
                    )
                
                # rate.sleep()
            showed_image = copy.deepcopy(input_image)
            cv2.arrowedLine(showed_image, (int(tip_x), int(tip_y)), (int(target_point[0]), int(target_point[1])), color=(255,0,0),thickness=8, tipLength=0.2)
            cv2.imshow('inference result', showed_image)

            key = cv2.waitKey(1)
            
        else:
            pub_tip_vel.publish(Vector3(0,0,0))
            break

  
    else:
        pub_tip_vel.publish(Vector3(0,0,0))
    
    rate.sleep()


pub_tip_vel.publish(Vector3(0,0,0))
start_puncture = time.time()
nav_duration = start_puncture - start
print("The navigation duration is: ", nav_duration)
time_keeper.append(nav_duration)


while not rospy.is_shutdown():
    print("Start puncture step.")
    input("Press Enter to start puncturing...")
    # puncture
    kp_linear_vel = 18 # 18
    linear_vel = 0.3
    # send_linear_velocity = kp_linear_vel * linear_vel
    current_position = np.array((x, y, z))
    time.sleep(0.1)
    current_quat = np.array((rx, ry, rz, rw))
    r_current = R.from_quat(current_quat)
    rotation_matrix_current = r_current.as_matrix()
    moving_direction = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
    send_linear_velocity = moving_direction * kp_linear_vel * linear_vel
    pub_tip_vel.publish(send_linear_velocity[0], send_linear_velocity[1], send_linear_velocity[2])
    time.sleep(0.1)
    pub_tip_vel.publish(Vector3(0, 0, 0))
    pub_tip_vel_angular.publish(Vector3(0, 0, 0))
    time.sleep(0.3)
    # input("Press Enter to start reracting the tool...")
    # pub_tip_vel.publish(0, 0, 0)
    # pub_tip_vel_angular.publish(0, 0, 0)
    # target_point = np.array((x, y, z)) + (current_position - np.array((x, y, z))) * 4 / 5
    target_distance = np.linalg.norm((current_position - np.array((x, y, z))) * 4 / 5)
    puncture_position = np.array((x, y, z))
    # slightly retract the tool
    while(True):
        # find appropriate linear vel
        kp_linear_vel = 2 # used to be 1.5 01/26/2023
        kp_angular_vel = 3 # 1.0, 2, 0.005, 1.5, 0.015
        current_position = np.array((x, y, z))
        # comment out 05/23/2024
        # current_quat = np.array((rx, ry, rz, rw))
        # r_current = R.from_quat(current_quat)
        # rotation_matrix_current = r_current.as_matrix()
        moving_direction = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
        send_linear_velocity = moving_direction * kp_linear_vel * linear_vel
        pub_tip_vel.publish(-send_linear_velocity[0], -send_linear_velocity[1], -send_linear_velocity[2])
        time.sleep(0.03)
        pub_tip_vel.publish(Vector3(0,0,0))
        # difference to final goal
        diff_to_final_goal = np.linalg.norm(current_position - puncture_position) - target_distance
        print("target_distance = ", target_distance)
        print("np.linalg.norm(current_position - puncture_position) = ", np.linalg.norm(current_position - puncture_position))
        print("diff_to_final_goal", diff_to_final_goal)
        # time.sleep(0.002)

        # if np.linalg.norm(error_rotation_vector) < 0.03:
        #     # print("We reached our angular goal!")
        #     # print("Final angular error: ", np.linalg.norm(error_rotation_vector))
        #     pub_tip_vel_angular.publish(0, 0, 0)
        #     # angular_vel_gain = 0

        if diff_to_final_goal < 0.003:
            # print("WE REACHED OUR FINAL GOAL!")
            # print("FINAL ERROR: ", diff_to_final_goal)
            # pub_tip_vel.publish(0, 0, 0)
            break
    pub_tip_vel.publish(Vector3(0, 0, 0))
    pub_tip_vel_angular.publish(Vector3(0, 0, 0))
    # puncture network inference
    if b_scan_raw is None:
        print("No b_scan_raw image!!")
    else :
        
        input("Press Enter to start puncture detection...")
        b_scan = ros_imgmsg_to_cv2(b_scan_raw)
        # print("Type of b_scan_raw_cv:", type(b_scan_raw_cv))

        b_scan = cv2.resize(b_scan, (640, 640))
       
        # b_scan  = b_scan[:, :, :3]

        # Convert to tensor
        b_scan_tensor = torch.tensor(b_scan).float().unsqueeze(0).unsqueeze(0).to(device)  # Add batch and channel dimensions

        # Save the processed image temporarily for detect.py
        temp_image_path = "temp_b_scan.jpg"
        cv2.imwrite(temp_image_path, b_scan)
        

        # Run inference on the resized image
        results = model.predict(source=temp_image_path,conf=0.01)

        # Initialize variables to keep track of the highest confidence bounding box
        highest_confidence = -1
        highest_confidence_class_id = None

        # Extract class ID with the highest confidence score
        for result in results:
            for box in result.boxes:
                confidence = box.conf.item()
                if confidence > highest_confidence:
                    highest_confidence = confidence
                    highest_confidence_class_id = int(box.cls.item())
        # Run YOLOv5 inference on the processed image
        # run_yolov5_inference(yolov5_dir, weights_path, temp_image_path)

        # # Get the latest results directory
        # latest_results_dir = get_latest_results_dir(yolov5_dir)
        # results_file_path = latest_results_dir / 'labels' / 'b_scans_puncture_0.txt'

        # if results_file_path.exists():
        #     class_ids, confidences = extract_class_ids_and_confidence(results_file_path)
        #     print("Detected class IDs:", class_ids)
        #     print("Confidences:", confidences)
        # b_scan = image_to_numpy(b_scan_raw)
        # #b_scan = b_scan_raw
        # result_image_path = "/home/peiyao/peiyao/DL_control_depend_yi/b_scans_puncture_{}.jpg".format(0)
        # cv2.imwrite(result_image_path, b_scan)

        # processed_b_scan, temp_image_path = process_b_scan(result_image_path, device)
        # run_yolov5_inference(yolov5_dir, weights_path, temp_image_path)
        # print("run")
        # latest_results_dir = get_latest_results_dir(yolov5_dir)
        # results_file_path = latest_results_dir / 'labels' / 'temp_b_scan.txt'

        # if results_file_path.exists():
        #     class_ids = extract_class_ids(results_file_path)
        #     print("Detected class IDs:", class_ids)
        print(highest_confidence_class_id)
        print(highest_confidence)
        if  highest_confidence_class_id == 0:
            continue   
        # elif highest_confidence < 0.3:# 0.6-0.75 suitable??
        #     continue
        elif highest_confidence_class_id == 1:
            break
        else:
            print("No detection results found.")
            continue

# # cv2.destroyWindow('inference result')


print("Start infusion step.")
pub_tip_vel.publish(-send_linear_velocity[0], -send_linear_velocity[1], -send_linear_velocity[2])
time.sleep(0.03)
pub_tip_vel.publish(Vector3(0,0,0))
input("Press Enter to start infusion step...")
start_infusion = time.time()
punc_duration = start_infusion - start_puncture
print("The puncture duration is: ", punc_duration)
time_keeper.append(punc_duration)
while not rospy.is_shutdown():
    justify_contact = input("Need justification for infusion (y/n): ").lower()
    
    if justify_contact == 'y':
        pub_tip_vel.publish(0, 0,  downward_linear_vel * linear_vel)
        time.sleep(0.05)
        pub_tip_vel.publish(Vector3(0,0,0))
    elif justify_contact == 'n':
        pub_tip_vel.publish(Vector3(0,0,0))
        break  # Exit the loop if input is 'n'

input("Press Enter to tool retraction step...")
start_retraction = time.time()
infusion_duration = start_retraction - start_infusion
print("The infusion duration is: ", infusion_duration)
time_keeper.append(infusion_duration)
puncture_position = np.array((x, y, z))

# retract the tool
while not rospy.is_shutdown():
    current_position = np.array((x, y, z))
    current_quat = np.array((rx, ry, rz, rw))
    r_current = R.from_quat(current_quat)
    rotation_matrix_current = r_current.as_matrix()
    moving_direction = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
    send_linear_velocity = moving_direction * kp_linear_vel * linear_vel
    pub_tip_vel.publish(-send_linear_velocity[0], -send_linear_velocity[1], -send_linear_velocity[2])
    diff_to_final_goal = np.linalg.norm(current_position - puncture_position)
    if diff_to_final_goal > 0.8:
        pub_tip_vel.publish(0, 0, 0)
        break

end = time.time()
retraction_duration = end - start_retraction
print("The retraction duration is: ", retraction_duration)
time_keeper.append(retraction_duration)
# # time_keeper = np.array(time_keeper)
#np.savetxt("./data/network_test/test{:02f}.csv".format(time.time()), time_keeper, delimiter=",")
save_dir = "/home/peiyao/peiyao/no_rcm_keyboard_controller/src/dl_control/src/csvfile"
os.makedirs(save_dir, exist_ok=True)
file_path = "{}test_{:.6f}.csv".format(save_dir, time.time())
np.savetxt(file_path, time_keeper, delimiter=",")
print(f"CSV file saved at: {file_path}")


print("We are done.")
pub_tip_vel.publish(0, 0, 0)
pub_tip_vel_angular.publish(0, 0, 0)