#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import numpy as np
import time
import os

def get_b_scan(imgmsg):
    # b scan is 64FC1: 64 bit depth with floating point and single channel

    dtype = np.dtype("float64")  # Adjust dtype as per your image format
    data = np.fromstring(imgmsg.data, dtype=dtype)
    image_np = data.reshape((imgmsg.height, imgmsg.width))
    encoding = imgmsg.encoding

    # Normalize to 0-1
    image_np_normalized = (image_np - np.min(image_np)) / (np.max(image_np) - np.min(image_np))
    
    # Scale to 0-255 and convert to uint8
    image_np_uint8 = (image_np_normalized * 255).astype(np.uint8)

    # print(image_np_uint8[10,10])  
    # print(encoding)  

if __name__ == "__main__":
    start = time.time()
    # rospy.init_node('test_bscan', anonymous=True)
    # rate = rospy.Rate(100) # 100hz

    # rospy.Subscriber("/b_scan", Image, get_b_scan)

    time_keeper = []

    time_keeper.append(0)
    
    end = time.time()

    time_keeper.append(end - start)


    save_dir = "./data/network_test/"
    os.makedirs(save_dir, exist_ok=True)
    file_path = "{}test_{:.6f}.csv".format(save_dir, time.time())
    np.savetxt(file_path, time_keeper, delimiter=",")
    print(f"CSV file saved at: {file_path}")
    #np.savetxt("./data/network_test/test{:02f}.csv".format(time.time()), time_keeper, delimiter=",")
    print("We are done.")
    # rospy.spin()


