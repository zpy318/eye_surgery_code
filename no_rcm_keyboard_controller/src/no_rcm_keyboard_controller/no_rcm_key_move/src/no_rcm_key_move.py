#!/usr/bin/env python3
from __future__ import print_function
import numpy as np
import cv2 
import os 
import time 
from datetime import datetime
from PIL import Image 
import shutil # to be able to delete entire directories
import csv 
import rospy 
from geometry_msgs.msg import Vector3, Transform
from scipy.spatial.transform import Rotation as R
from std_msgs.msg import Float64MultiArray
import roslib
import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import matplotlib.pyplot as plt
from no_rcm_key_publisher_msgs.msg import no_rcm_key_publisher_msgs
import math

x = None
y = None
z = None
rx = None
ry = None
rz = None
rw = None
# # for camera recording
# ddp_results = None
# # for clicking goal points and publishing over ros
# indicator_x = None
# network_output = None
# rcm_point = None

move_left_flag = False
move_right_flag = False
move_up_flag = False
move_down_flag = False
move_upward_flag = False
move_downward_flag = False
move_forward_flag = False
move_backward_flag = False
move_angle_insertion_flag = False
move_angle_retraction_flag = False
large_gain_flag = False
small_gain_flag = False
small_push_flag = False

class move:
  def __init__(self):
    self.key_sub = rospy.Subscriber("/no_rcm_key_input", no_rcm_key_publisher_msgs, self.get_key_input)
    self.tool_tip_position_sub = rospy.Subscriber("/eye_robot/FrameEE", Transform, self.get_tool_tip_position)

  def get_key_input(self, data):
    global move_left_flag
    global move_right_flag
    global move_up_flag
    global move_down_flag
    global move_upward_flag
    global move_downward_flag
    global move_forward_flag
    global move_backward_flag
    global move_angle_insertion_flag
    global move_angle_retraction_flag
    global large_gain_flag
    global small_gain_flag
    global small_push_flag


    move_left_flag = data.move_left
    move_right_flag = data.move_right
    move_up_flag = data.move_up
    move_down_flag = data.move_down
    move_upward_flag = data.move_upward
    move_downward_flag = data.move_downward
    move_forward_flag = data.move_forward
    move_backward_flag = data.move_backward
    move_angle_insertion_flag = data.move_angle_insertion
    move_angle_retraction_flag = data.move_angle_retraction
    large_gain_flag = data.large_gain
    small_gain_flag = data.small_gain
    small_push_flag = data.small_push

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

# class ddp_tracking:

#   def __init__(self):
#     self.ddp_results_sub = rospy.Subscriber("/ddp_output", ddp_output_msgs, self.get_ddp_results)
#     self.indicator_sub = rospy.Subscriber("/CNN/DesiredTipPosition",  Vector3, self.get_indicator)
#     self.tool_tip_position_sub = rospy.Subscriber("/eye_robot/FrameEE", Transform, self.get_tool_tip_position)
#     self.network_output_sub = rospy.Subscriber("/network_output", Vector3, self.get_network_output)
#     self.rcm_point_sub = rospy.Subscriber("/ddp_input", ddp_input_msgs, self.get_rcm_point)

#   def get_ddp_results(self, data):
#     global ddp_results
#     ddp_results = data.ddp_traj
#     # usb_image = bridge.imgmsg_to_cv2(data, desired_encoding = 'passthrough')

#   def get_indicator(self, data):
#     global indicator_x
#     indicator_x = data.x
  
#   def get_tool_tip_position(self, data):
#     global x
#     global y
#     global z
#     global rx
#     global ry
#     global rz
#     global rw

#     x = data.translation.x
#     y = data.translation.y
#     z = data.translation.z
#     rx = data.rotation.x
#     ry = data.rotation.y
#     rz = data.rotation.z
#     rw = data.rotation.w
  
#   def get_network_output(self, data):
#     global network_output
#     network_output = data
  
#   def get_rcm_point(self, data):
#     global rcm_point
#     rcm_point = data.rcm_point

# for publishing the clicked goal position
def create_publisher():
  """
      Usage:
        publisher = create_publisher()
        publisher.publish(desired_position[0], desired_position[1], desired_position[2])
  """
  pub_tip_vel = rospy.Publisher('/eyerobot2/desiredTipVelocities', Vector3, queue_size = 3)
  pub_tip_vel_angular = rospy.Publisher('/eyerobot2/desiredTipVelocitiesAngular', Vector3, queue_size = 3)
  return pub_tip_vel, pub_tip_vel_angular

if __name__ == '__main__':
  move()
  pub_tip_vel, pub_tip_vel_angular = create_publisher()
  rospy.init_node('move', anonymous=True)
  rate = rospy.Rate(100) # 100hz
  kp_linear_vel = 2 # used to be 1.5 01/26/2023
  kp_angular_vel = 3 # 1.0, 2, 0.005, 1.5, 0.015
  insertion_angle = 45 * math.pi / 180 # set the tool-tip bended angle default 20
  forward_step_size = 0.3
  linear_vel = 0.1
  # top_k = 10
  # desired_index = 1
  diff_angle_thresh = 0.1 * math.pi / 180

  current_quat = np.array((rx, ry, rz, rw))
  r_current = R.from_quat(current_quat)
  # active rotation matrix from original vector to current vector
  rotation_matrix_current = r_current.as_matrix()
  vector_cur = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
  # print("vector_cur = ", vector_cur)
  xy_sqrt = math.sqrt(vector_cur[0]**2 + vector_cur[1]**2)
  # for certain degree bended tool, define the value above
  vector_desired = np.array((vector_cur[0] * math.sin(insertion_angle) / xy_sqrt, vector_cur[1] * math.sin(insertion_angle) / xy_sqrt, -math.cos(insertion_angle)))
  # ref:https://math.stackexchange.com/questions/180418/calculate-rotation-matrix-to-align-vector-a-to-vector-b-in-3d
  # to calculate the desired rotation matrix of insertion
  vector_cross = np.cross(vector_cur, vector_desired)
  # s = np.linalg.norm(vector_cross)
  c = np.dot(vector_cur, vector_desired)
  v_matrix = np.array([[0, -vector_cross[2], vector_cross[1]], [vector_cross[2], 0, -vector_cross[0]], [-vector_cross[1], vector_cross[0], 0]])
  rotation_matirx_error = np.identity(3) + v_matrix + np.matmul(v_matrix, v_matrix) / (1 + c)
  r_error = R.from_matrix(rotation_matirx_error)
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
      # for certain degree bended tool, define the value above
      vector_desired = np.array((vector_cur[0] * math.sin(insertion_angle) / xy_sqrt, vector_cur[1] * math.sin(insertion_angle) / xy_sqrt, -math.cos(insertion_angle)))
      # ref:https://math.stackexchange.com/questions/180418/calculate-rotation-matrix-to-align-vector-a-to-vector-b-in-3d
      # to calculate the desired rotation matrix of insertion
      vector_cross = np.cross(vector_cur, vector_desired)
      # s = np.linalg.norm(vector_cross)
      c = np.dot(vector_cur, vector_desired)
      v_matrix = np.array([[0, -vector_cross[2], vector_cross[1]], [vector_cross[2], 0, -vector_cross[0]], [-vector_cross[1], vector_cross[0], 0]])
      rotation_matirx_error = np.identity(3) + v_matrix + np.matmul(v_matrix, v_matrix) / (1 + c)
      r_error = R.from_matrix(rotation_matirx_error)
      error_rotation_vector = r_error.as_rotvec()
      unit_error_rotation_vector = error_rotation_vector / np.linalg.norm(error_rotation_vector)
      print("Angular ERROR: ", np.linalg.norm(error_rotation_vector))
      # publish the velocities
      pub_tip_vel_angular.publish(angular_vel[0], angular_vel[1], angular_vel[2])

  pub_tip_vel.publish(0, 0, 0)
  pub_tip_vel_angular.publish(0, 0, 0)

  print("You can control the robot now!")
  
  while not rospy.is_shutdown():
    # if (indicator_x == 1 and ddp_results != None and network_output != None):
    if (large_gain_flag):
      kp_linear_vel = 8 # 0.5, 1, 0.01, 0.6, 0.03
      kp_angular_vel = 6.5 # 1.0, 2, 0.005, 1.5, 0.015
      linear_vel = 0.1
    elif (small_gain_flag):
      kp_linear_vel = 2 # usded to be 1 01/26/2023
      kp_angular_vel = 3 # 1.0, 2, 0.005, 1.5, 0.015
      linear_vel = 0.1
    if (move_left_flag):
      send_linear_velocity = kp_linear_vel * linear_vel
      pub_tip_vel.publish(0, send_linear_velocity, 0)
      move_left_flag = False
      rate.sleep()
    elif (move_right_flag):
      send_linear_velocity = kp_linear_vel * linear_vel
      pub_tip_vel.publish(0, -send_linear_velocity, 0)
      move_right_flag = False
      rate.sleep()
    elif (move_up_flag):
      send_linear_velocity = kp_linear_vel * linear_vel
      pub_tip_vel.publish(send_linear_velocity, 0, 0)
      move_up_flag = False
      rate.sleep()
    elif (move_down_flag):
      send_linear_velocity = kp_linear_vel * linear_vel
      pub_tip_vel.publish(-send_linear_velocity, 0, 0)
      move_down_flag = False
      rate.sleep()
    elif (move_upward_flag):
      send_linear_velocity = kp_linear_vel * linear_vel
      pub_tip_vel.publish(0, 0, send_linear_velocity)
      move_upward_flag = False
      rate.sleep()
    elif (move_downward_flag):
      send_linear_velocity = kp_linear_vel * linear_vel
      pub_tip_vel.publish(0, 0, -send_linear_velocity)
      move_downward_flag = False
      rate.sleep()
    elif (move_forward_flag):
      current_quat = np.array((rx, ry, rz, rw))
      r_current = R.from_quat(current_quat)
      rotation_matrix_current = r_current.as_matrix()
      moving_direction = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
      send_linear_velocity = moving_direction * kp_linear_vel * linear_vel
      pub_tip_vel.publish(send_linear_velocity[0], send_linear_velocity[1], send_linear_velocity[2])
      move_forward_flag = False
      rate.sleep()
    elif (move_backward_flag):
      current_quat = np.array((rx, ry, rz, rw))
      r_current = R.from_quat(current_quat)
      rotation_matrix_current = r_current.as_matrix()
      moving_direction = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
      send_linear_velocity = moving_direction * kp_linear_vel * linear_vel
      pub_tip_vel.publish(-send_linear_velocity[0], -send_linear_velocity[1], -send_linear_velocity[2])
      move_backward_flag = False
      rate.sleep()
    elif (move_angle_insertion_flag):
      current_quat = np.array((rx, ry, rz, rw))
      r_current = R.from_quat(current_quat)
      rotation_matrix_current = r_current.as_matrix()
      moving_direction = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
      send_linear_velocity = moving_direction * kp_linear_vel * linear_vel
      pub_tip_vel.publish(send_linear_velocity[0], send_linear_velocity[1], send_linear_velocity[2])
      move_angle_insertion_flag = False
      rate.sleep()
    elif (move_angle_retraction_flag):
      current_quat = np.array((rx, ry, rz, rw))
      r_current = R.from_quat(current_quat)
      rotation_matrix_current = r_current.as_matrix()
      moving_direction = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
      send_linear_velocity = moving_direction * kp_linear_vel * linear_vel
      pub_tip_vel.publish(-send_linear_velocity[0], -send_linear_velocity[1], -send_linear_velocity[2])
      move_angle_retraction_flag = False
      rate.sleep()
    elif (small_push_flag):
      kp_linear_vel = 18 # 0.5, 1, 0.01, 0.6, 0.03
      linear_vel = 0.3
      current_quat = np.array((rx, ry, rz, rw))
      r_current = R.from_quat(current_quat)
      rotation_matrix_current = r_current.as_matrix()
      moving_direction = np.matmul(rotation_matrix_current, np.array((0, 0, -1)))
      send_linear_velocity = moving_direction * kp_linear_vel * linear_vel
      pub_tip_vel.publish(send_linear_velocity[0], send_linear_velocity[1], send_linear_velocity[2])
      small_push_flag = False
      kp_linear_vel = 2 # usded to be 1 01/26/2023
      linear_vel = 0.1
      rate.sleep()
    else:
      pub_tip_vel.publish(0, 0, 0)
      pub_tip_vel_angular.publish(0, 0, 0)
      rate.sleep()
