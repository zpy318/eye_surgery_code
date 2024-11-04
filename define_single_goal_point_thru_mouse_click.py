# For defining the target point on the images
# !/usr/bin/env python
from __future__ import print_function
import cv2 # for saving/loading images - see online page for details
import time # for accessing current time
from PIL import Image # apparently the fastest tool to save images
import rospy # for writing a ROS node
from geometry_msgs.msg import Vector3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import csv

# for camera image recording
camera_image = None
# for clicking goal points and publishing over ros
clicked_goal = None
clicked_goal_list = []

class image_converter:

  def __init__(self):
    self.camera_img_sub = rospy.Subscriber("/decklink/camera/image_raw", Image, self.get_camera_image)
    self.clicked_goal_sub = rospy.Subscriber("/click_goal", Vector3, self.get_clicked_goal)

  def get_camera_image(self, data):
    global camera_image
    bridge = CvBridge()
    camera_image = bridge.imgmsg_to_cv2(data, "bgr8")

  def get_clicked_goal(self,data):
    global clicked_goal
    global clicked_goal_list
    clicked_goal = data
    print("select code, print clicked goal: ", clicked_goal)
    if len(clicked_goal_list) == 0:
      clicked_goal_list.append(clicked_goal)
    else:
      clicked_goal_list = []
      clicked_goal_list.append(clicked_goal)


# Path to save CSV file
#csv_file = '/home/peiyao/Downloads/clicked_positions.csv'




# for publishing the clicked goal position
def create_publisher():
  """
      Usage:
        publisher = create_publisher()
        publisher.publish(desired_position[0], desired_position[1], desired_position[2])
  """
  pub = rospy.Publisher("/click_goal", Vector3, queue_size=10)
  return pub  

def mouseRGB(event,x,y,flags,param):
    global frame
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
        colors = frame[y,x]
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)
        # with open(csv_file, 'a', newline='') as file:
        #   writer = csv.writer(file)
        #   writer.writerow([x,y])
        #   file.flush()  # Explicitly flush the buffer to ensure data is written immediately

        # frame = cv2.rectangle(frame, (x - 5 , y - 5), (x+5, y+5), color = (0,255,0))
        publisher_send_clicked_goal.publish(x, y, 0.0)

##############################################
# MAIN CODE STARTS HERE
#############################################

ic = image_converter()
# for sending clicked goal position over ros node
publisher_send_clicked_goal = create_publisher()
rospy.init_node('image_converter', anonymous=True)
time.sleep(2)
    
# save_directory = "intact_eye_test/inference_data"
sleep_duration = 0.08
# create main directory
# if not os.path.exists(save_directory):
#   os.makedirs(save_directory)

# setup callback for registering clicked positions
# the name of the window must align with the name of the windows mentioned below
# i.e. 'frame
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouseRGB)





for i in range(4000):
  while not rospy.is_shutdown():
    
    # read images to display them
    frame = camera_image
    frame = frame[90:990, 510:1410, :]
    frame = cv2.resize(frame, (512, 512))
    sz = 8

    # plot the clicked goal positions
    if len(clicked_goal_list) == 1:
      xx = int(clicked_goal_list[0].x)
      yy = int(clicked_goal_list[0].y)
      sz_ = 8
      frame = cv2.rectangle(frame, (xx-sz, yy-sz), 
                          (xx+sz, yy+sz), color = (255, 255,255), thickness = 1)
      frame = cv2.rectangle(frame, (xx-1, yy-1), 
                          (xx+1, yy+1), color = (255,255,255), thickness = 1)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      pass
    # DO NOT RECORD IF X == 0
    time.sleep(sleep_duration)
  clicked_goal_list = []