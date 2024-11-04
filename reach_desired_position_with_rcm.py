#!/usr/bin/env python
# for gcop-python stuff
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.spatial.transform import Rotation as R
from pytransform3d.trajectories import plot_trajectory
import time
import math
# for ros stuff
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray # for publishing and subscribing
from geometry_msgs.msg import Vector3, Transform

# populated  by call_backs
x = None
y = None
z = None
rx = None
ry = None
rz = None
rw = None
force_x = None
force_y = None
force_z = None
torque_x = None
torque_y = None
torque_z = None

# for recording the ee transform
def callback_1(data):
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

# def callback_3(data):
#     global force_x
#     global force_y
#     global force_z
#     global torque_x
#     global torque_y
#     global torque_z
#     array = data.data
#     force_x = array[0]
#     force_y = array[1]
#     force_z = array[2]
#     torque_x = array[3]
#     torque_y = array[4]
#     torque_z = array[5]

# def get_sphere_points(rcm_point, tool_tip, angle_range):

#     moved_tip = tool_tip - rcm_point
#     r = np.sqrt(np.sum(moved_tip**2)) + 1e-20

#     current_s = np.arctan2(moved_tip[1], moved_tip[0])
#     current_t = np.arccos(moved_tip[2]/r)

#     print("current_s: ", current_s*180/np.pi)
#     print(r)


#     points = []
    
#     angles = []

#     angle_range = angle_range * np.pi / 180

#     # for s in np.linspace(current_s - angle_range, current_s + angle_range, 15):
#     for t in np.linspace(current_t - angle_range, current_t + angle_range, 10):
#         s = current_s
#         x = r * np.cos(s) * np.sin(t)
#         y = r * np.sin(s) * np.sin(t)
#         z = r * np.cos(t)

#         real_tip = [x, y, z] + rcm_point
#         angles.append([t, s])
#         points.append(real_tip)

    
#     x = r * np.cos(current_s) * np.sin(current_t)
#     y = r * np.sin(current_s) * np.sin(current_t)
#     z = r * np.cos(current_t)
#     real_tip = [x, y, z] + rcm_point
#     angles.append([current_t, current_s])
#     points.append(real_tip)

#     points = np.array(points)
#     angles = np.array(angles)

#     np.savetxt("./rcm_angle_data.csv", angles, delimiter=",")
#     np.savetxt("./rcm_tip_data.csv", points, delimiter=",")

#     return points, r


# create ros publisher
pub_tip_vel = rospy.Publisher('/eyerobot2/desiredTipVelocities', Vector3, queue_size = 10)
pub_tip_vel_angular = rospy.Publisher('/eyerobot2/desiredTipVelocitiesAngular', Vector3, queue_size = 10)
rospy.init_node("TipVelocityPublisher", anonymous = True)
# create subscriber 
rospy.Subscriber("/eye_robot/FrameEE", Transform, callback_1)
time.sleep(0.5)

# get initial state
initial_point = np.array((x, y, z))
current_quat = np.array((rx, ry, rz, rw))
#########################################
# CHOOSE TARGET POINT AND ANGLE
#########################################
# target_point = np.array((x, y, z)) + ((0, 0, 0.4))
# target_point = np.array((-2.28447416, -57.99561663, -28.51265524)) 
# target_point = np.array((-4.1165775, -57.0598715, -26.9345085))
# target_point = np.array((-2.83351358, -58.3268894, -28.47970237)) 
# target_point = np.array((-2.2987663, -58.61353104, -28.51159779))
# target_point = np.array((-2.82750584, -57.22350235, -28.47929948))
# [ 0.43025822]
#  [ 0.01547986]
#  [-0.03705085]
# ((0.17291922, 0.01442417, 0.0497782))
#########################################
# CHOOSE TARGET POINT ALONG THE TOOL
#########################################
# insertion_distance = 1
# r = R.from_quat(current_quat)
# rotation_matrix = r.as_dcm()
# unit_orientation = np.matmul(rotation_matrix, np.array((0, 0, 1)))
# target_point = np.array((x, y, z)) + insertion_distance * unit_orientation

#########################################
# NAVIGATE TO THE DESIRED POINT WITH RCM CONSTRAINT
#########################################
# set manually

# tooltip_point = np.asarray((30.005, -71.567, -38.076))
rcm_point = np.array((2.483, -91.633, 3.444))
target_point = np.asarray((10, -92, -5))
# target_point = np.asarray((21.409, -82.412, -46.145))

# assert(False)

rcm_to_target_point = rcm_point - target_point
dx = rcm_to_target_point[0]
dy = rcm_to_target_point[1]
dz = rcm_to_target_point[2]
magnitude = np.sqrt(dx**2 + dy**2 + dz**2)
theta_y = np.arctan2(dx, dz)
theta_x = np.arcsin(-dy / magnitude)
desired_euler_angle = np.array((theta_x, theta_y, 0))
r_rcm_to_target = R.from_euler("xyz", desired_euler_angle)
rotation_matrix_rcm_to_target = r_rcm_to_target.as_dcm()
r_current = R.from_quat(current_quat)
rotation_matrix_current = r_current.as_dcm()
error_angular_rotation_matrix = np.matmul(rotation_matrix_rcm_to_target, np.transpose(rotation_matrix_current))
# error_angular_rotation_matrix = np.matmul(np.transpose(rotation_matrix_current), rotation_matrix_rcm_to_target)
r_error = R.from_dcm(error_angular_rotation_matrix)
error_rotation_vector = r_error.as_rotvec()
unit_error_rotation_vector = error_rotation_vector / np.linalg.norm(error_rotation_vector)

# linear_vel_gain = 0.080
# angular_vel_gain = 0.08

# while (np.linalg.norm(error_rotation_vector) >= 0.03):
#     angular_vel = unit_error_rotation_vector * angular_vel_gain
#     current_quat = np.array((rx, ry, rz, rw))
#     r_current = R.from_quat(current_quat)
#     rotation_matrix_current = r_current.as_dcm()
#     error_angular_rotation_matrix = np.matmul(rotation_matrix_rcm_to_target, np.transpose(rotation_matrix_current))
#     r_error = R.from_dcm(error_angular_rotation_matrix)
#     error_rotation_vector = r_error.as_rotvec()
#     unit_error_rotation_vector = error_rotation_vector / np.linalg.norm(error_rotation_vector)
#     print("Angular ERROR: ", np.linalg.norm(error_rotation_vector))
#     # publish the velocities
#     pub_tip_vel_angular.publish(angular_vel[0], angular_vel[1], angular_vel[2])

pub_tip_vel.publish(0, 0, 0)
pub_tip_vel_angular.publish(0, 0, 0)

linear_vel_gain = 0.080
angular_vel_gain = 0.01

while(True):
    # find appropriate linear vel
    current_point = np.array((x,y,z))
    diff_xyz = target_point - current_point
    if (np.linalg.norm(diff_xyz) > 3):
        linear_vel_gain = 0.3
        # angular_vel_gain = 0.01
    else:
        # linear_vel_gain = 0.080
        angular_vel_gain = 0.01
    diff_xyz_norm = diff_xyz / np.linalg.norm(diff_xyz)
    linear_vel = diff_xyz_norm * linear_vel_gain
    angular_vel = unit_error_rotation_vector * angular_vel_gain

    current_quat = np.array((rx, ry, rz, rw))
    r_current = R.from_quat(current_quat)
    rotation_matrix_current = r_current.as_dcm()
    error_angular_rotation_matrix = np.matmul(rotation_matrix_rcm_to_target, np.transpose(rotation_matrix_current))
    r_error = R.from_dcm(error_angular_rotation_matrix)
    error_rotation_vector = r_error.as_rotvec()
    unit_error_rotation_vector = error_rotation_vector / np.linalg.norm(error_rotation_vector)
    print("Angular ERROR: ", np.linalg.norm(error_rotation_vector))
    # publish the velocities
    pub_tip_vel.publish(linear_vel[0], linear_vel[1], linear_vel[2])
    pub_tip_vel_angular.publish(angular_vel[0], angular_vel[1], angular_vel[2])

    # difference to final goal
    diff_to_final_goal = np.linalg.norm(current_point - target_point)
    time.sleep(0.002)

    if np.linalg.norm(error_rotation_vector) < 0.03:
        print("We reached our angular goal!")
        print("Final angular error: ", np.linalg.norm(error_rotation_vector))
        pub_tip_vel_angular.publish(0, 0, 0)
        # angular_vel_gain = 0

    if diff_to_final_goal < 0.003:
        print("WE REACHED OUR FINAL GOAL!")
        print("FINAL ERROR: ", diff_to_final_goal)
        pub_tip_vel.publish(0, 0, 0)
        break
pub_tip_vel.publish(0, 0, 0)
pub_tip_vel_angular.publish(0, 0, 0)