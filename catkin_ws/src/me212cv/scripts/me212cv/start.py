#!/usr/bin/python

import rospy
import numpy as np
import cv2  # OpenCV module

from sensor_msgs.msg import Image, CameraInfo
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point, Pose, Twist, Vector3, Quaternion
from std_msgs.msg import ColorRGBA

from cv_bridge import CvBridge, CvBridgeError
import message_filters
import math

# Bridge to convert ROS Image type to OpenCV Image type
cv_bridge = CvBridge()  

def main():
    rospy.init_node('starting_condition', anonymous=True)
    rospy.Subscriber('/camera/depth_registered/image', Image, left_or_right)
    rospy.spin()
def find_marker():
    try:
        cv_image = cv_bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5),0)
    edged = cv2.Canny(gray,35,125)
    cnts, mask_g = cv2.findCountours(edged.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if cnts == None:
        ready = False
    else:
        ready = True
    print ready
    return [ready, cnts, mask_g];

# choosing sides for task 1
def left_or_right(depth_data):
    try:
        cv_image = cv_bridge.imgmsg_to_cv2(msg, "bgr8")
        cv_depthimage = cv_bridge.imgmsg_to_cv2(depth_data, "32FC1")
        cv_depthimage2 = np.array(cv_depthimage, dtype=np.float32)
    except CvBridgeError as e:
        print(e)
    
    [r, cnts, mask_g] = find_marker()
    
    for c in cnts:
        xp,yp,w,h = cv2.boundingRect(c)
        
        # Get depth value from depth image, need to make sure the value is in the normal range 0.1-10 meter
        if not math.isnan(cv_depthimage2[int(yp)][int(xp)]) and cv_depthimage2[int(yp)][int(xp)] > 0.1 and cv_depthimage2[int(yp)][int(xp)] < 10.0:
            zc = cv_depthimage2[int(yp)][int(xp)]
            print 'zc', zc
        else:
            continue
            
        centerx, centery = xp+w/2, yp+h/2
        cv2.rectangle(cv_image,(xp,yp),(xp+w,yp+h),[0,255,255],2)
        
        showPyramid(centerx, centery, zc, w, h)
        
        xg,yg,zg = getXYZ(xp, yp, zc, fx,fy,cx,cy)
        if .5 < zg <.65:
            path = 1;
            break
        else:
            path = 2;
        print path
        
if __name__=='__main__':
    main()
