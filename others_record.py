#!/usr/bin/env python
import time
import numpy as np
import rospy
from geometry_msgs.msg import Vector3, Transform
from std_msgs.msg import Float64MultiArray # for publishing and subscribing
from threading import Thread

x = None
y = None
z = None
pos_vel_x = 0
pos_vel_y = 0
pos_vel_z = 0
rot_vel_x = 0
rot_vel_y = 0
rot_vel_z = 0
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

def callback_3(data):
    global force_x
    global force_y
    global force_z
    global torque_x
    global torque_y
    global torque_z
    array = data.data
    force_x = array[0]
    force_y = array[1]
    force_z = array[2]
    torque_x = array[3]
    torque_y = array[4]
    torque_z = array[5]

def get_pos_vel(data):
    global pos_vel_x
    global pos_vel_y
    global pos_vel_z
    pos_vel_x = data.x 
    pos_vel_y = data.y 
    pos_vel_z = data.z 

def get_rot_vel(data):
    global rot_vel_x
    global rot_vel_y
    global rot_vel_z
    rot_vel_x = data.x 
    rot_vel_y = data.y 
    rot_vel_z = data.z 

rospy.init_node("TipVelocityPublisher", anonymous = True)
rospy.Subscriber("/eye_robot/FrameEE", Transform, callback_1)
rospy.Subscriber("/CNN/HandleForce", Float64MultiArray, callback_3)
rospy.Subscriber("/eyerobot2/desiredTipVelocities", Vector3, get_pos_vel)
rospy.Subscriber("/eyerobot2/desiredTipVelocitiesAngular", Vector3, get_rot_vel)
count = 0
records = []
time_after_loop = time.time()
min_time_to_save = 0.05
input("Press Enter to start recording velocities and etc...")
while not rospy.is_shutdown():
    time_before_loop = time.time()
    if time_before_loop - time_after_loop >= min_time_to_save:
        real_frequency = 1 / (time_before_loop - time_after_loop)
        print(real_frequency)
        # main programm
        time_after_loop = time.time()
        cur_record = [x, y, z, rx, ry, rz ,rw, pos_vel_x, pos_vel_y, pos_vel_z, rot_vel_x, rot_vel_y, rot_vel_z, force_x, force_y, force_z, torque_x, torque_y, torque_z]
        # print(cur_record)
        records.append(cur_record)

# records = np.array(records)
print(records)
np.savetxt("./results/records{:02d}.csv".format(count), records, delimiter=",")