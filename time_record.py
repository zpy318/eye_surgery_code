#!/usr/bin/env python
import time
import numpy as np
import rospy

count = 0
while not rospy.is_shutdown():
    print("**********Current trial number: ", count)
    time_keeper = []
    input("Press Enter to start navigation...")
    start = time.time()
    input("Press Enter to start puncture...")
    start_puncture = time.time()
    nav_duration = start_puncture - start
    print("The navigation duration is: ", nav_duration)
    time_keeper.append(nav_duration)
    input("Press Enter to start C_scan...")
    start_c_scan = time.time()
    punc_duration = start_c_scan - start_puncture
    print("The puncture duration is: ", punc_duration)
    time_keeper.append(punc_duration)
    input("Press Enter to start injection or infusion...")
    start_infusion = time.time()
    c_scan_duration = start_infusion - start_c_scan
    print("The c_scan duration is: ", c_scan_duration)
    time_keeper.append(c_scan_duration)
    input("Press Enter to start retraction...")
    start_retraction = time.time()
    infusion_duration = start_retraction - start_infusion
    print("The infusion duration is: ", infusion_duration)
    time_keeper.append(infusion_duration)
    input("Press Enter to finish...")
    end = time.time()
    retraction_duration = end - start_retraction
    print("The retraction duration is: ", retraction_duration)
    time_keeper.append(retraction_duration)
    # time_keeper = np.array(time_keeper)
    np.savetxt("./results/test{:02d}.csv".format(count), time_keeper, delimiter=",")
    count += 1

