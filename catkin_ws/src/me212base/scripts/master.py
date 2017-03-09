#!/usr/bin/python

import rospy
import cv2  # OpenCV module
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point, Pose, Twist, Vector3, Quaternion
from std_msgs.msg import ColorRGBA
cv_bridge = CvBridge();
import message_filters

rospy.init_node('master', anonymous=True)

from me212arm import run_reach
from me212arm import run_reach_pika
from me212arm import run_drop
from me212arm import run_drop_pika

from me212arm import run_planning
from me212cv import object_detection
from me212bot import apriltag_navi



def main():
    R = 0.225;
    ready = False
    while not ready:
        rgb_data = rospy.wait_for_message("/camera/rgb/image_rect_color", Image)
        depth_data = rospy.wait_for_message("/camera/depth_registered/image", Image)
        ready = object_detection.ready_or_not(rgb_data, depth_data)
        rospy.sleep(0.1)
    print(ready);
    
    apriltag_navi.init();
    run_planning.main();
    rospy.sleep(2)
    apriltag_navi.naviOne(R);
    
    path = None
    while path is None:
        rgb_data = rospy.wait_for_message("/camera/rgb/image_rect_color", Image)
        depth_data = rospy.wait_for_message("/camera/depth_registered/image", Image)
        path = object_detection.left_or_right(rgb_data, depth_data)
        rospy.sleep(0.1)
    print(path)
    
    apriltag_navi.naviTwo(R, path);
    apriltag_navi.naviThree(R);
    run_reach.main(); #gripper (task = 1)
    rospy.sleep(2)
    apriltag_navi.naviThree2(R);
    run_planning.main()
    apriltag_navi.naviFour(R);
    #rospy.sleep(0.1)
    run_drop.main(); #gripper (task = 2)
    rospy.sleep(2)
    run_planning.main()
    rospy.sleep(0.1)
    apriltag_navi.naviFive(R);
    apriltag_navi.naviFiveTag(R);  
    boxChoice = None
    while  boxChoice is None:
        rgb_data = rospy.wait_for_message("/camera/rgb/image_rect_color", Image)
        _, _, boxChoice,colorChoice  = object_detection.HSVObjectDetection(rgb_data,False)
        rospy.sleep(0.1)
    print("colorChoice = " + str(colorChoice) + ", boxChoice = " + str(boxChoice))
    apriltag_navi.naviSix(R, boxChoice);
    run_reach.main(); #gripper (task = 1)
    run_planning.main()
    apriltag_navi.naviSeven(R, boxChoice);
    run_drop.main(); #gripper (task = 2)
    run_planning.main()
    apriltag_navi.naviEight(R);
    apriltag_navi.naviEightTag(R);
    run_reach_pika.main(); #gripper (task = 1)
    rospy.sleep(2)
    run_planning.main()
    apriltag_navi.naviNine(R);
    run_drop_pika.main(); #gripper (task = 2)
    
def image_callback(img):
    depth_data = img;
    
if __name__ =="__main__":
    main();
