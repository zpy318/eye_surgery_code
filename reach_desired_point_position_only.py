#!/usr/bin/env python
# for gcop-python stuff
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.spatial.transform import Rotation as R
import time
# for ros stuff
import rospy
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
# target_point = np.array((x, y, z)) + ((-0.5, -0.0, -0.0))
# target_point = np.array((-2.28447416, -57.99561663, -28.51265524)) 
# target_point = np.array((-4.1165775, -57.0598715, -26.9345085))
# target_point = np.array((-2.83351358, -58.3268894, -28.47970237)) 
# target_point = np.array((3,ddd -164.852, 5))
target_point = np.array((31.91, -98.09, -51.59))
# [ 0.43025822]1
#  [ 0.01547986]
#  [-0.03705085]
# ((0.17291922, 0.01442417, 0.0497782))
#########################################
# CHOOSE TARGET POINT ALONG THE TOOL
#########################################
# insertion_distance = -0.5
# r = R.from_quat(current_quat)
# rotation_matrix = r.as_dcm()
# unit_orientation = np.matmul(rotation_matrix, np.array((0, 0, 1)))
# target_point = np.array((x, y, z)) + insertion_distance * unit_orientation

linear_vel_gain = 0.3

while not rospy.is_shutdown():
    # find appropriate linear vel
    current_point = np.array((x,y,z))
    diff_xyz = target_point - current_point
    diff_xyz_norm = diff_xyz / np.linalg.norm(diff_xyz)
    linear_vel = diff_xyz_norm * linear_vel_gain
    # print("sne")

    # publish the velocities
    pub_tip_vel.publish(linear_vel[0], linear_vel[1], linear_vel[2])

    # difference to final goal
    diff_to_final_goal = np.linalg.norm(current_point - target_point)
    time.sleep(0.002)

    if diff_to_final_goal < 0.005:
        print("WE REACHED OUR FINAL GOAL!")
        print("FINAL ERROR: ", diff_to_final_goal)
        pub_tip_vel.publish(0, 0, 0)
        break
