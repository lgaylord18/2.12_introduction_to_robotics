#!/usr/bin/python

# 2.12 Lab 4 object detection: a node for detecting objects
# Peter Yu Oct 2016

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

from me212cv.srv import DetectObject, DetectObjectResponse

path = 0;

# Publisher for publishing pyramid marker in rviz
vis_pub = rospy.Publisher('visualization_marker', Marker, queue_size=10) 

# Bridge to convert ROS Image type to OpenCV Image type
cv_bridge = CvBridge()  




def handle_object_detection(req):
    global r_count, b_count, g_count
    r_count = 0
    b_count = 0
    g_count = 0
    
    label = ''
    while True:
        if r_count > 30:
            label = 'red'
            break
            
        rospy.sleep(0.1)
    
    
    
    return DetectObjectResponse(0,0,0)
    

rospy.Service('/object_detection', DetectObject, handle_object_detection)

def main(useHSV, useDepth):
    rospy.init_node('object_detection', anonymous=True)
    global r_count, b_count, g_count
    r_count = 0
    b_count = 0
    g_count = 0
    
    if not useHSV:
        # Task 1
        #cv2.namedWindow("OpenCV_View")
        
        #cv2.setMouseCallback("OpenCV_View", cvWindowMouseCallBackFunc)
        # subscribe to image
        rospy.Subscriber('/camera/rgb/image_rect_color', Image, rosImageVizCallback)
    else:
        if not useDepth:
            # Task 2 Detect object using HSV
            #    Subscribe to RGB images
            rospy.Subscriber('/camera/rgb/image_rect_color', Image, rosHSVProcessCallBack)
        else:
            # Task 3: Use Kinect depth data
            #    Subscribe to both RGB and Depth images with a Synchronizer
            image_sub = message_filters.Subscriber("/camera/rgb/image_rect_color", Image)
            depth_sub = message_filters.Subscriber("/camera/depth_registered/image", Image)
            #rospy.Subscriber('/camera/depth_registered/image', Image, left_or_right)
            
            ts = message_filters.ApproximateTimeSynchronizer([image_sub, depth_sub], 10, 0.5)
            #ts.registerCallback(rosRGBDCallBack)
            #ts.registerCallback(left_or_right)
            #ts.registerCallback(ready_or_not)
            ts.registerCallback(HSVObjectDetection)

            
    rospy.spin()

# Task 1 callback for ROS image
def rosImageVizCallback(msg):
    # 1. convert ROS image to opencv format
    try:
        cv_image = cv_bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)

    # 2. visualize it in a cv window
    cv2.imshow("OpenCV_View", cv_image)

    # set callback func for mouse hover event
    cv2.setMouseCallback("OpenCV_View", cvWindowMouseCallBackFunc)
    cv2.waitKey(3)

# Task 1 callback for mouse event
def cvWindowMouseCallBackFunc(event, xp, yp, flags, param):
    print 'In cvWindowMouseCallBackFunc: (xp, yp)=', xp, yp  # xp, yp is the mouse location in the window
    # 1. Set the object to 2 meters away from camera
    zc = 2.0
    # 2. Visualize the pyramid
    showPyramid(xp, yp, zc, 10, 10)

# Task 2 callback
def rosHSVProcessCallBack(msg):
    try:
        cv_image = cv_bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
        
    contours, mask_image,_ = HSVObjectDetection(cv_image)
    if mask_image is None:
        return
    
    #for cnt in contours:
        # Find a bounding box of detected region
        #  xp, yp are the coordinate of the top left corner of the bounding rectangle
        #  w, h are the width and height of the bounding rectangle
        #xp,yp,w,h = cv2.boundingRect(cnt)  
        
        # Set the object to 2 meters away from camera
        #zc = 2    
        
        # Draw the bounding rectangle
        #cv2.rectangle(cv_image,(xp,yp),(xp+w,yp+h),[0,255,255], 2)
        
       # centerx, centery = xp+w/2, yp+h/2
        #showPyramid(centerx, centery, zc, w, h)
    

# Task 2 object detection code/ original object detector/ new color choosing
def HSVObjectDetection(rgb_data, toPrint = False):

        
    global r_count, g_count, b_count
    
    cv_image = cv_bridge.imgmsg_to_cv2(rgb_data, "bgr8")

    hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    
    # define range of red color in HSV
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    
    # Range for blue
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    # Range for green
    lower_green = np.array([38,50,50])
    upper_green = np.array([75,255,255])

    
    # Thresjold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv_image,lower_blue,upper_blue)
    # Threshold the HSV image to get only red colors
    red_mask = cv2.inRange(hsv_image,lower_red,upper_red)
    
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Threshold the HSV image to get only r,b,g colors

    red_mask_eroded         = cv2.erode(red_mask, None, iterations = 3)
    red_mask_eroded_dilated = cv2.dilate(red_mask_eroded, None, iterations = 10)
    
    blue_mask_eroded         = cv2.erode(blue_mask, None, iterations = 3)
    blue_mask_eroded_dilated = cv2.dilate(blue_mask_eroded, None, iterations = 10)
    
    
    green_mask_eroded         = cv2.erode(green_mask, None, iterations = 3)
    green_mask_eroded_dilated = cv2.dilate(green_mask_eroded, None, iterations = 10)
    
    #showImageInCVWindow(red_mask_eroded_dilated,green_mask_eroded_dilated,blue_mask_eroded_dilated)
    
    _, r_contours,_ = cv2.findContours(red_mask_eroded_dilated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    _,b_contours,_ = cv2.findContours(blue_mask_eroded_dilated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    _,g_contours,_ = cv2.findContours(green_mask_eroded_dilated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    #print len(r_contours)
    #print len(b_contours)
    #print len(g_contours)
    
    
    
    contours = [len(r_contours), len(b_contours), len(g_contours)]
    
    mask_eroded = None
    mask_eroded_dilated = None
    boxChoice = None
    
    #if len(r_contours) == max(contours):
        #r_count += 1
        #if r_count == 30:
            #contours= r_contours
            #mask_eroded = red_mask_eroded
            #mask_eroded_dilated = red_mask_eroded_dilated
            
    #elif len(b_contours) == max(contours):
        #b_count += 1
        #if b_count == 30:
            #contours = b_contours
            #mask_eroded = blue_mask_eroded
            #mask_eroded_dilated = blue_mask_eroded_dilated

    #else:
        #g_count += 1
        #if g_count == 30:
            #contours = g_contours
            #mask_eroded = green_mask_eroded
            #mask_eroded_dilated = green_mask_eroded_dilated

    #if toPrint:
        #print 'hsv', hsv_image[240][320] # the center point hsv
        
    #print str(r_count), str(g_count), str(b_count)
    
    
    # Figure out what color box we need to pick
    #coordinate of the color indicator
    xPix = [378, 457]
    yPix = [33, 110]
    
    ColorGiven = [0,0,0]
    PixGiven_R = red_mask_eroded_dilated[ yPix[0]:yPix[1] ][ :,xPix[0]:xPix[1] ]
    ColorGiven[0] = sum(sum(PixGiven_R))
    PixGiven_B = blue_mask_eroded_dilated[ yPix[0]:yPix[1] ][ :,xPix[0]:xPix[1] ]
    ColorGiven[1] = sum(sum(PixGiven_B))
    PixGiven_G = green_mask_eroded_dilated[ yPix[0]:yPix[1] ][ :,xPix[0]:xPix[1] ]
    ColorGiven[2] = sum(sum(PixGiven_G))
    
    # colorChoice is 0 = red, 1 = blue, 2 = green
    colorChoice = ColorGiven.index(max(ColorGiven))
    #print str(colorChoice)

    if colorChoice == 0:
        mask_color = red_mask_eroded_dilated
    elif colorChoice == 1:
        mask_color = blue_mask_eroded_dilated
    else:
        mask_color = green_mask_eroded_dilated

    # check box locations
    xPix_Pos0 = [210, 242]
    yPix_Pos0 = [328, 373]
    
    xPix_Pos1 = [319, 350]
    yPix_Pos1 = [328, 373]
    
    xPix_Pos2 = [418, 450]
    yPix_Pos2 = [328, 373]
    
    PixGiven = [0,0,0]
    boxGiven = [0,0,0]
    PixGiven[0] = mask_color[ yPix_Pos0[0]:yPix_Pos0[1] ][ :,xPix_Pos0[0]:xPix_Pos0[1] ]
    boxGiven[0] = sum(sum(PixGiven[0]))

    PixGiven[1] = mask_color[ yPix_Pos1[0]:yPix_Pos1[1] ][ :,xPix_Pos1[0]:xPix_Pos1[1] ]
    boxGiven[1] = sum(sum(PixGiven[1]))
    
    PixGiven[2] = mask_color[ yPix_Pos2[0]:yPix_Pos2[1] ][ :,xPix_Pos2[0]:xPix_Pos2[1] ]
    boxGiven[2] = sum(sum(PixGiven[2]))

    boxChoice = boxGiven.index(max(boxGiven))
    print("colorChoice = " + str(colorChoice) + ", boxChoice = " + str(boxChoice))

    cv2.imshow('OpenCV_Mask_Erode', cv2.bitwise_and(cv_image, cv_image, mask = red_mask_eroded_dilated))
    cv2.waitKey(1)
    
    #~ if mask_eroded_dilated is not None:
        #~ cv2.imshow('OpenCV_Mask_Erode', cv2.bitwise_and(cv_image, cv_image, mask = mask_eroded))
        #~ cv2.waitKey(1)
    
    #~ showImageInCVWindow(cv_image, mask_eroded, mask_eroded_dilated)
    #contours,hierarchy = cv2.findContours(mask_eroded_dilated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    return  contours, mask_color, boxChoice, colorChoice

#Color Choosing!!!
#def HSVObjectDetection(cv_image,toPrint = True):
    
    ##if cv_image is not used as an argument
    ##try:
     ##   cv_image = cv_bridge.imgmsd_to_cv2(msg, "bgr8")
    ##except CvBridgeError as e:
     ##   print(e)
    
    #hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    
    #boundaries = [([110,50,50],[130,255,255]),
                  #([170,50,50],[180,255,255]),
                  #([38,50,50],[75,255,255])]
    #for (lower, upper) in boundaries:
        #lower = np.array(lower, dtype = "uint8")
        #upper = np.array(upper, dtype = "uint8")
        
        #mask2 = cv2.inRange(hsv_image,lower,upper)
        #mask2_eroded = cv2.erode(mask2, None, iterations = 3)
        #mask2_eroded_dilated = cv2.dilate(mask2_eroded, None, iterations = 12)
        
        #showImageInCVWindow(cv_image, mask2_eroded, mask2_eroded_dilated)
        #counts2,hierarchy2 = cv2.findContours(mask2_eroded_dilated,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        #if len(counts2) > 3:
            #break
    #mask = mask2
    #mask_eroded = mask2_eroded
    #mask_eroded_dilated = mask2_eroded_dilated
    #contours= counts2
    
    #if toPrint:
        #print 'hsv', hsv_image[240][320] # the center point hsv
        
    #showImageInCVWindow(cv_image, mask_eroded, mask_eroded_dilated)
    
    #return contours, mask_eroded_dilated

# Task 3 callback
def rosRGBDCallBack(rgb_data, depth_data):
    try:
        cv_image = cv_bridge.imgmsg_to_cv2(rgb_data, "bgr8")
        cv_depthimage = cv_bridge.imgmsg_to_cv2(depth_data, "32FC1")
        cv_depthimage2 = np.array(cv_depthimage, dtype=np.float32)
    except CvBridgeError as e:
        print(e)

    contours, mask_image = HSVObjectDetection(cv_image, toPrint = False)

    for cnt in contours:
        xp,yp,w,h = cv2.boundingRect(cnt)
        
        # Get depth value from depth image, need to make sure the value is in the normal range 0.1-10 meter
        if not math.isnan(cv_depthimage2[int(yp)][int(xp)]) and cv_depthimage2[int(yp)][int(xp)] > 0.1 and cv_depthimage2[int(yp)][int(xp)] < 10.0:
            zc = cv_depthimage2[int(yp)][int(xp)]
            #print 'zc', zc
        else:
            continue
            
        centerx, centery = xp+w/2, yp+h/2
        cv2.rectangle(cv_image,(xp,yp),(xp+w,yp+h),[0,255,255],2)
        
        showPyramid(centerx, centery, zc, w, h)

def getXYZ(xp, yp, zc, fx,fy,cx,cy):
    ## 
    xn = (xp - cx) / fx
    yn = (yp - cy) / fy
    xc = xn * zc
    yc = yn * zc
    return (xc,yc,zc)

def showImageInCVWindow(cv_image, mask_erode_image, mask_image):
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(cv_image, cv_image, mask = mask_image)
    
    # Draw a cross at the center of the image
    cv2.line(cv_image, (320, 235), (320, 245), (255,0,0))
    cv2.line(cv_image, (325, 240), (315, 240), (255,0,0))
    
    # Show the images
    cv2.imshow('OpenCV_Original', cv_image)
    cv2.imshow('OpenCV_Mask_Erode', mask_erode_image)
    cv2.imshow('OpenCV_Mask_Dilate', mask_image)
    cv2.imshow('OpenCV_View', res)
    cv2.waitKey(3)

# Create a pyramid using 4 triangles
def showPyramid(xp, yp, zc, w, h):
    global fx, fy, cx, cy
    # X1-X4 are the 4 corner points of the base of the pyramid
    X1 = getXYZ(xp-w/2, yp-h/2, zc, fx, fy, cx, cy)
    X2 = getXYZ(xp-w/2, yp+h/2, zc, fx, fy, cx, cy)
    X3 = getXYZ(xp+w/2, yp+h/2, zc, fx, fy, cx, cy)
    X4 = getXYZ(xp+w/2, yp-h/2, zc, fx, fy, cx, cy)
    vis_pub.publish(createTriangleListMarker(1, [X1, X2, X3, X4], rgba = [1,0,0,1], frame_id = '/camera'))

# Create a list of Triangle markers for visualization
def createTriangleListMarker(marker_id, points, rgba, frame_id = '/camera'):
    marker = Marker()
    marker.header.frame_id = frame_id
    marker.type = marker.TRIANGLE_LIST
    marker.scale = Vector3(1,1,1)
    marker.id = marker_id
    
    n = len(points)
    
    if rgba is not None:
        marker.color = ColorRGBA(*rgba)
        
    o = Point(0,0,0)
    for i in xrange(n):
        p = Point(*points[i])
        marker.points.append(p)
        p = Point(*points[(i+1)%4])
        marker.points.append(p)
        marker.points.append(o)
        
    marker.pose = poselist2pose([0,0,0,0,0,0,1])
    return marker

def poselist2pose(poselist):
    return Pose(Point(*poselist[0:3]), Quaternion(*poselist[3:7]))

def init():
    global fx, fy, cx, cy
    # Get the camera calibration parameter for the rectified image
    msg = rospy.wait_for_message('/camera/rgb/camera_info', CameraInfo, timeout=None) 
    #     [fx'  0  cx' Tx]
    # P = [ 0  fy' cy' Ty]
    #     [ 0   0   1   0]

    fx = msg.P[0]
    fy = msg.P[5]
    cx = msg.P[2]
    cy = msg.P[6]

#Starting Task
def ready_or_not(rgb_data,depth_data):
    ready = False
    cv_image = cv_bridge.imgmsg_to_cv2(rgb_data, "bgr8")
    cv_depthimage = cv_bridge.imgmsg_to_cv2(depth_data, "32FC1")
    cv_depthimage2 = np.array(cv_depthimage, dtype=np.float32)
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5),0)
    edged = cv2.Canny(gray,35,125)
    _,cnts, mask_g = cv2.findContours(edged.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


    for c in cnts:
        xp,yp,w,h = cv2.boundingRect(c)
        
        # Get depth value from depth image, need to make sure the value is in the normal range 0.1-10 meter
        if not math.isnan(cv_depthimage2[int(yp)][int(xp)]) and cv_depthimage2[int(yp)][int(xp)] > 0.1 and cv_depthimage2[int(yp)][int(xp)] < 10.0:
            zstart = cv_depthimage2[int(yp)][int(xp)]
            #print 'zstart', zstart
        else:
            continue
         
        if zstart > 1:
            ready = True
    
    #print ready
    #showImageInCVWindow(cv_image, gray, edged)
    return ready

# choosing sides for task 1
def left_or_right(rgb_data,depth_data):
    path = 1
    try:
        cv_image = cv_bridge.imgmsg_to_cv2(rgb_data, "bgr8")
        cv_depthimage = cv_bridge.imgmsg_to_cv2(depth_data, "32FC1")
        cv_depthimage2 = np.array(cv_depthimage, dtype=np.float32)
    except CvBridgeError as e:
        print(e)
    
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5),0)
    edged = cv2.Canny(gray,35,125)
    #_,cnts2, mask_g2 = cv2.findContours(edged.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    #for c2 in cnts2:
        #xp,yp,w,h = cv2.boundingRect(c2)
    xp = 320
    yp = 430    
    # Get depth value from depth image, need to make sure the value is in the normal range 0.1-10 meter
    if not math.isnan(cv_depthimage2[int(yp)][int(xp)]) and cv_depthimage2[int(yp)][int(xp)] > 0.1 and cv_depthimage2[int(yp)][int(xp)] < 10.0:
        zBox = cv_depthimage2[yp][xp]
        #print 'zc', zc
    else:
        return
    if zBox <.95:
        path = 1
    else:
        path = 2
        
    return path
        
if __name__=='__main__':
    main(True, False)
    



#code for implemnting in master_open
#rgb_data = None
#depth_data = None
#def main():
    #rospy.subscribe(.../dir,Image,image_callback)
    #ready = false
    #while not ready:
        #ready = ready_or_not(rgb_data, depth_data)
    #//Other Codes//
    #path = None
    #while path is None:
        #path = left_or_right(rgb_data, depth_data)

    #~ while  mask_eroded_dilated is None
        #~ HSVObjectDetection(cv_image)
    
#def image_callback(img)
    #depth_data = img
    
