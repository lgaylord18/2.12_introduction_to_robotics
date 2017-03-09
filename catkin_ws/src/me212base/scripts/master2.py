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
    apriltag_navi.init();
    run_planning.main();
    rospy.sleep(2)
    
    apriltag_navi.mMoveTime(-0.1,-0.1,2)
    apriltag_navi.naviFiveTag(R);
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
