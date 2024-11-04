#include "flycapture/FlyCapture2.h"

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/opencv.hpp"

#include <iostream>

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <unistd.h>
#include <time.h> 

using namespace cv;

// THIS CODE HAS BEEN ADAPTED FROM THE ORIGINAL VERSION
// IN ORDER TO USE THE USB CAMERA MICROSCOPE INSTEAD OF THE
// FIREWIRE POINTGREY CAMERA 
// DATE: 3/15/2020 
// AUTHOR: BRIAN

int main(int argc, char** argv)
{
    unsigned int microseconds = 1000000;

    // publish part
    ros::init(argc, argv, "image_publisher");
    ros::NodeHandle nh;
    image_transport::ImageTransport it(nh);
    image_transport::Publisher pub = it.advertise("camera/image", 1);

    // convert to rgb
    cv::VideoCapture cap(0);

    if(!cap.isOpened()){
        std::cout << "Error opening video stream or file" << std::endl;
        return -1;
    }

    usleep(microseconds);

    char key = 0;
    while(nh.ok())
    {
        // Capture frame-by-frame
        cv::Mat image;
        cap >> image;

        // Uncomment lines below to show images while publishing
        // cv::imshow("image", image);
        // char c = (char)cv::waitKey(25);
        // if (c == 27)
        //     break;
        
        // declaring argument of time() 
        //time_t my_time = time(NULL); 
        // printf("%s", ctime(&my_time)); 

        // publish part
        sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();
        // sensor_msgs::ImagePtr msg = image.toImageMsg();

        // ros::Rate loop_rate(5);
        pub.publish(msg);
        ros::spinOnce(); // necessary for call back functions - thrown-in for good measure
        // loop_rate.sleep();
    }

    return 0;
}
