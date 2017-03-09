#!/usr/bin/python
# 2.12 Lab 3 AprilTag Navigation: use AprilTag for current global robot (X,Y,Theta), and to navigate to target (X,Y,Theta)
# Peter Yu Sept 2016

import rospy
import tf
import numpy as np
import threading
import serial
import tf.transformations as tfm
import math
import time # for time in MoveTime

from me212base.msg import WheelVelCmd
from apriltags.msg import AprilTagDetections
from helper import poseTransform, pubFrame, cross2d, lookupTransformList, pose2list, invPoseList, diffrad

    
def apriltag_callback(data):
    global lr, br
    global apriltag_number
    # use apriltag pose detection to find where is the robot
    for detection in data.detections:
        if detection.id == apriltag_number: 
            tagframe = '/apriltag%d' % detection.id
            ##
            poselist_tag_cam = pose2list(detection.pose)
            poselist_tag_base = poseTransform(poselist_tag_cam, homeFrame = '/camera', targetFrame = '/robot_base', listener = lr)
            poselist_base_tag = invPoseList(poselist_tag_base)
            poselist_base_map = poseTransform(poselist_base_tag, homeFrame = tagframe, targetFrame = '/map', listener = lr)
            pubFrame(br, pose = poselist_base_map, frame_id = '/robot_base', parent_frame_id = '/map')
            print apriltag_number

def init():
    global lr, br
    lr = tf.TransformListener()
    br = tf.TransformBroadcaster()

def naviOne(R):
    #Go to Orange Line
    MoveTime(0,0,4)
    MoveJames(0.05,1/R,np.pi*R/16)
    MoveTime(0,-0.1,1.3)
    MoveTime(0.1,0.1,3)
    print("test")
    MoveJames(0.05,-1/R,np.pi*R/7)
    print("test complete")
    MoveTime(0,0,2)
    print("test pause")
    #print wcv.desiredWV_R, wcv.desiredWV_L

def naviTwo(R, coursenum):
    if coursenum == 2:
        #course 1: Straight $ turn / use AprilTag2
        MoveTime(0.1,0.1,6)
    
        #apriltag_number = 2
        #target_pose2d = [0.30, 1.10, np.pi/2]
        #navi_loop(target_pose2d)
        #MoveTime(0,0,2)
        MoveJames(0.05,-1/R,np.pi*R/3.2)
        MoveTime(0.1,0.1,3)
    
        #apriltag_number = 4
        #target_pose2d = [1.2, 1.9, np.pi/2.5]
        #navi_loop(target_pose2d)
    
        ##Turning Toward Pidgey
        MoveJames(0.05,1/R,np.pi*R/8)
        MoveTime(0.1,0.1,1) #2s->1s after adding 1s in naviOne
        MoveTime(0,-0.1,2)
        MoveJames(0.05,1/R,np.pi*R/3)
        #MoveTime(0.1,0,1)
        MoveTime(0,0,2)
        MoveTime(-0.1,-0.1,2)
        MoveTime(0,-0.1,2)
    
    elif coursenum == 1:
        #course 2: turn & straight
        MoveJames(0.05,-1/R,np.pi*R/4)
        MoveTime(0.1,0.1,7)
        MoveJames(0.05, 1/R,np.pi*R/2)
        MoveTime(0,0,1)
        MoveTime(0,-0.1,1.5)
        MoveTime(0,0,2)
    
def naviThree(R):
    global apriltag_number
    apriltag_sub = rospy.Subscriber("/apriltags/detections", AprilTagDetections, apriltag_callback, queue_size = 1)
    #~ apriltag_number = 3
    #~ target_pose2d = [1, 1.9, np.pi]
    #~ navi_loop(target_pose2d)
    #~ MoveTime (0,0,1)
    
    
    apriltag_number = 1
    target_pose2d = (0.63, 1.93, np.pi)
    navi_loop(target_pose2d)
    MoveTime(0,0,2)
    
def naviThree2(R):
    MoveTime(-0.1,-0.1,3)
    MoveTime(-0.1,0,1.5)
    MoveTime(-0.1,-0.1,2)

def naviFour(R):
    MoveTime(0,0,2)
    MoveTime(-0.1,0,5)
    MoveTime(0,0,2)
    MoveTime(0.1,0.1,4.5)
    MoveTime(0,0,1)
    #MoveTime(-0.1,0,2.5)
    #MoveTime(0.1,0.1,4)
    #MoveTime(0,0,3)

#def naviFourTote(R):
    #global apriltag_number
    #apriltag_sub = rospy.Subscriber("/apriltags/detections", AprilTagDetections, apriltag_callback, queue_size = 1)
    #apriltag_number = 5
    #target_pose2d = [2.3, 1.8, np.pi/2]
    #navi_loop_ypos(target_pose2d)
    #MoveTime(0,0,2)
    

def naviFive(R):
    #Spin around to face 2nd box
    MoveTime(-0.1,-0.1,2)
    MoveTime(-0.1,0,6)
    MoveTime(-0.1,-0.1,2)  #Just uncommented this today (Nate) hopefully it doesn't mess shit up
    MoveTime(0,0.1,7)
    MoveTime(0.1,0.1,2)
    MoveTime(-0.1,0.1,1)
    MoveTime(0,0,2)
    
def naviFiveTag(R):
    #Center towards april tag 9
    global apriltag_number
    apriltag_sub = rospy.Subscriber("/apriltags/detections", AprilTagDetections, apriltag_callback, queue_size = 1)
    apriltag_number = 9
    target_pose2d = [1.8, 0.8, -np.pi/2]
    navi_loop(target_pose2d)
    MoveTime(0,0,4)

#***Object Identification and Grab
#Need "if elif else statements for color"

def naviSix(R, boxChoice):
    # boxChoice = 1
    
    #~ if boxChoice == 0:
        #~ MoveTime(-0.1,0,3)
        #~ MoveTime(-0.1,-0.1,4)
        #~ MoveTime(0.1,0,2.8)
        #~ MoveTime(0.1,0.1,1.41)      
        #~ #target_pose2d = [2.09,1,-np.pi/2]
    #~ elif boxChoice == 1:
        #~ MoveTime(-0.1,0,3)
        #~ MoveTime(-0.1,-0.1,3)
        #~ MoveTime(0.1,0,2.8)
        #~ MoveTime(0.1,0.1,0.7)
        #~ #target_pose2d = [2, 1, -np.pi/2]
    #~ else:
        #~ MoveTime(-0.1,0,3)
        #~ MoveTime(-0.1,-0.1,2)
        #~ MoveTime(0.1,0,2.8)
    MoveTime(-0.1,0,3)
    MoveTime(-0.1,-0.1,4.3)
    MoveTime(0.1,0,2.8)
    MoveTime(0.1,0.1,4.5)
    MoveTime(0,0,3)
    if boxChoice == 0:
        MoveTime(0.05,-0.05,2)
    elif boxChoice == 2:
        MoveTime(-0.05,0.05,2)
        MoveTime(0.1,0.1,1)    #I changed this recently, changed time from 0.5-1
    MoveTime(0,0,2)
    #navi_loop_y(target_pose2d)
    #~ MoveTime(0,0,4)
    #~ MoveTime(0.1,0.1,2.5)
    #~ MoveTime(0,0,2)

#Turn Around, return to Tote
def naviSeven(R,boxChoice):
    if boxChoice == 0:
        MoveTime(-0.05,0.05,2)
    elif boxChoice == 2:
        MoveTime(-0.1,-0.1,0.5)
        MoveTime(0.05,-0.05,2)
    MoveTime(-0.1,-0.1,2.5)
    MoveTime(-0.1,0,6)
    MoveTime(-0.1,-0.1,2)  
    MoveTime(0,0.1,7)
    MoveTime(0.1,0.1,4.5)
    MoveTime(0,0,2)

def naviEight(R):
    #~ #Drive to 3rd Box
    MoveTime(-0.1,0,6)
    MoveTime(0.1,0.1,9)
    MoveTime(0,0.1,6)
    MoveTime(0.1,0.1,1)
    MoveTime(0,0,4)
    
def naviEightTag(R):
    global apriltag_number
    apriltag_sub = rospy.Subscriber("/apriltags/detections", AprilTagDetections, apriltag_callback, queue_size = 1)
        
    apriltag_number = 8
    target_pose2d = [3.27,0.8,-np.pi/2]
    navi_loop_y(target_pose2d)
    MoveTime(0,0,4)
    MoveTime(0.05,0.05,3)
    MoveTime(0,0,2)

def naviNine(R):
    #Turn Around, return to Tote
    MoveTime(-0.1,-0.1,3.5)
    MoveTime(-0.1,0.1,4.5)
    MoveTime(0,0,2)
    MoveTime(0.1,0.1,5)
    MoveTime(0,0.1,2)
    MoveTime(0,0,2)
    MoveTime(0.1,0.1,4.5) #I changed this recently, time from 3.5-4.5 (Nate)
    MoveTime(0,0,4)

def main():
    global apriltag_number
    apriltag_number = 20 
    apriltag_sub = rospy.Subscriber("/apriltags/detections", AprilTagDetections, apriltag_callback, queue_size = 1)
    R = 0.225;
    init()
   
    #Initial Turn in Zone 1
    rospy.sleep(1)
    MoveTime(0,0,4)
    #naviOne(R);
    ##Avoiding Obstacles in Zone 2
    #naviTwo(R, 2);
    #Approaching to Pidgey using apriltag 3 & 1
    #naviThree(R);
    #
    #Use gripper, grab
    #Backing off & turn toward Tote
    #naviFour(R);
    #User gripper, drop
    #naviFive(R);
    #object identification
    #naviSix(R,boxChoice)
    #return to tote
    #naviSeven(R);
    #apriltag_number = 5
    #target_pose2d = [2.4,1.85,np.pi/2]
    #navi_loop(target_pose2d)
    #
    #use gripper, drop
    #naviEight(R);
    #use gripper, grab
    #naviNine(R);
    #apriltag_number = 5
    #target_pose2d = [2.4,1.85,np.pi/2]
    #navi_loop(target_pose2d)
    MoveTime(0,0,4)
    #Use Gripper, drop
    rospy.spin()

def constant_vel_loop():
    velcmd_pub = rospy.Publisher("/cmdvel", WheelVelCmd, queue_size = 1)
    rate = rospy.Rate(100) # 100hz
    
    while not rospy.is_shutdown() :
        wcv = WheelCmdVel()
        ##
        wcv.desiredWV_R = 0.1
        wcv.desiredWV_L = 0.2
        velcmd_pub.publish(wcv) 
        
        rate.sleep() 
        
def MoveJames(robotVel,K,path_dist):
    velcmd_pub = rospy.Publisher("/cmdvel", WheelVelCmd, queue_size = 1)
    rate = rospy.Rate(100) # 100hz
    #robotVel,K,path_dist
    r = 0.037
    b = 0.225
    wcv = WheelVelCmd()
    
    numIter = int(round((path_dist/robotVel)*100,0))
    print(numIter)
    for  i in range(1,numIter)   :
        #wcv.desiredWV_R = 0.5
        #wcv.desiredWV_L = 0.5
    
        wcv.desiredWV_R = (r)*((robotVel/r) + (K*b*robotVel)/(r))
        wcv.desiredWV_L = (r)*((robotVel/r) - (K*b*robotVel)/(r))

        velcmd_pub.publish(wcv) 
        
        rate.sleep() 

def AprilTagNoiseCorr( currentPos, PrevPos, resetVal, realSig ):
    # Compute change between samples
    delta = currentPos - PrevPos

    # If large drop in magnitude consiter noise and use previous at a point and set realSig to zero
    if delta < -0.3 :
        resetVal = PrevPos
        rawDataFilt = resetVal
        realSig = 0
            
    # check is incorrect position if so use resetVal
    elif realSig == 0 :
        rawDataFilt = resetVal
        if delta > 0.3 :
            realSig = 1               
    # use actual point if delta is small and realSig is 1
    else :
        rawDataFilt = currentPos
        realSig = 1
   	return [rawDataFilt, resetVal, realSig]

def MoveTime(wvelR, wvelL, duration) :
    velcmd_pub = rospy.Publisher("/cmdvel", WheelVelCmd, queue_size = 1)
    rate = rospy.Rate(100) # 100hz
    
    wcv = WheelVelCmd()
    
    t_end = time.time() + duration
    print time.time()
    print t_end
    while time.time() < t_end :
        
        wcv.desiredWV_R = wvelR
        wcv.desiredWV_L = wvelL
        
        velcmd_pub.publish(wcv)
        
        rate.sleep()

def navi_loop(target_pose2d):
    global lr, br
    velcmd_pub = rospy.Publisher("/cmdvel", WheelVelCmd, queue_size = 1)
    rate = rospy.Rate(100) # 100hz
    
    wcv = WheelVelCmd()
    
    arrived = False
    arrived_position = False
    count = 0
    
    while not rospy.is_shutdown() :
        # 1. get robot pose
        robot_pose3d = lookupTransformList('/map', '/robot_base', lr)
        
        if robot_pose3d is None:
            print '1. Tag not in view, Stop', '/ Target Pose:', target_pose2d
            wcv.desiredWV_R = 0.0  # right, left
            wcv.desiredWV_L = 0.0
            velcmd_pub.publish(wcv)  

            rate.sleep()
            continue
        
        robot_position2d  = robot_pose3d[0:2]
        target_position2d = target_pose2d[0:2]
        
        robot_yaw    = tfm.euler_from_quaternion(robot_pose3d[3:7]) [2]
        robot_pose2d = robot_position2d + [robot_yaw]
        
        rawDataFilt = [0, 0, 0];
        resetVal = [0, 0, 0];
        realSig = [0, 0, 0];

        # Apply AprilTagNoiseCorr function to each direction
        #if count == 0:
            #PrevPos = robot_pose2d
            #resetVal = robot_pose2d
            #realSig = 1
        #else:
            #[rawDataFilt[0], resetVal[0], realSig[0]] = AprilTagNoiseCorr( currentPos[0], PrevPos[0], resetVal[0], realSig[0] )
            #[rawDataFilt[1], resetVal[1], realSig[1]] = AprilTagNoiseCorr( currentPos[1], PrevPos[1], resetVal[1], realSig[1] )
            #[rawDataFilt[2], resetVal[2], realSig[2]] = AprilTagNoiseCorr( currentPos[2], PrevPos[2], resetVal[2], realSig[2] )

        #robot_pose2d = rawDataFilt;
        
        # 2. navigation policy
        # 2.1 if       in the target, 
        # 2.2 else if  close to target position, turn to the target orientation
        # 2.3 else if  in the correct heading, go straight to the target position,
        # 2.4 else     turn in the direction of the target position
        
        pos_delta         = np.array(target_position2d) - np.array(robot_position2d)
        robot_heading_vec = np.array([np.cos(robot_yaw), np.sin(robot_yaw)])
        heading_err_cross = cross2d( robot_heading_vec, pos_delta / np.linalg.norm(pos_delta) )
        
        #print 'robot_position2d', robot_position2d, 'target_position2d', target_position2d
        print 'pos_delta', pos_delta
        #print 'robot_yaw', robot_yaw
        #print 'norm delta', np.linalg.norm( pos_delta ), 'diffrad', diffrad(robot_yaw, target_pose2d[2])
        #print 'heading_err_cross', heading_err_cross
        print 'robot pose', robot_pose2d, 'target pose', target_pose2d
        
        if arrived or (np.linalg.norm( pos_delta ) < 0.08 and np.fabs(diffrad(robot_yaw, target_pose2d[2]))<0.05) :
            print 'Case 2.1  Stop'
            wcv.desiredWV_R = 0  
            wcv.desiredWV_L = 0
            arrived = True
            return
        elif np.linalg.norm( pos_delta ) < 0.08:    # distance < 8cm
            arrived_position = True
            if diffrad(robot_yaw, target_pose2d[2]) > 0:  # radians difference > 0
                print 'Case 2.2.1  Turn right slowly'      
                wcv.desiredWV_R = -0.05 
                wcv.desiredWV_L = 0.05
            else:
                print 'Case 2.2.2  Turn left slowly'
                wcv.desiredWV_R = 0.05  
                wcv.desiredWV_L = -0.05
                
        elif arrived_position or np.fabs( heading_err_cross ) < 0.2:
            if(pos_delta[0]<0):     # (x_target - x_robot) < 0
                print 'Case 2.3.1  Straight forward'  
                wcv.desiredWV_R = 0.1
                wcv.desiredWV_L = 0.1
            else:
                print 'Case 2.3.2  Straight backward'  
                wcv.desiredWV_R = -0.1
                wcv.desiredWV_L = -0.1
        else:
            if heading_err_cross < 0:     # cross product of robot vec and target vec < 0
                print 'Case 2.4.1  Turn right'
                wcv.desiredWV_R = -0.1
                wcv.desiredWV_L = 0.1
            else:
                print 'Case 2.4.2  Turn left'
                wcv.desiredWV_R = 0.1
                wcv.desiredWV_L = -0.1
                
        velcmd_pub.publish(wcv)  
        
        rate.sleep()
        
def navi_loop_y(target_pose2d):
    velcmd_pub = rospy.Publisher("/cmdvel", WheelVelCmd, queue_size = 1)
    rate = rospy.Rate(100) # 100hz
    
    wcv = WheelVelCmd()
    
    arrived = False
    arrived_position = False
    count = 0
    
    while not rospy.is_shutdown() :
        # 1. get robot pose
        robot_pose3d = lookupTransformList('/map', '/robot_base', lr)
        
        if robot_pose3d is None:
            print '1. Tag not in view, Stop', '/ Target Pose:', target_pose2d
            wcv.desiredWV_R = 0.0  # right, left
            wcv.desiredWV_L = 0.0
            velcmd_pub.publish(wcv)  

            rate.sleep()
            continue
        
        robot_position2d  = robot_pose3d[0:2]
        target_position2d = target_pose2d[0:2]
        
        robot_yaw    = tfm.euler_from_quaternion(robot_pose3d[3:7]) [2]
        robot_pose2d = robot_position2d + [robot_yaw]
        
        rawDataFilt = [0, 0, 0];
        resetVal = [0, 0, 0];
        realSig = [0, 0, 0];

        # Apply AprilTagNoiseCorr function to each direction
        #if count == 0:
            #PrevPos = robot_pose2d
            #resetVal = robot_pose2d
            #realSig = 1
        #else:
            #[rawDataFilt[0], resetVal[0], realSig[0]] = AprilTagNoiseCorr( currentPos[0], PrevPos[0], resetVal[0], realSig[0] )
            #[rawDataFilt[1], resetVal[1], realSig[1]] = AprilTagNoiseCorr( currentPos[1], PrevPos[1], resetVal[1], realSig[1] )
            #[rawDataFilt[2], resetVal[2], realSig[2]] = AprilTagNoiseCorr( currentPos[2], PrevPos[2], resetVal[2], realSig[2] )

        #robot_pose2d = rawDataFilt;
        
        # 2. navigation policy
        # 2.1 if       in the target, 
        # 2.2 else if  close to target position, turn to the target orientation
        # 2.3 else if  in the correct heading, go straight to the target position,
        # 2.4 else     turn in the direction of the target position
        
        pos_delta         = np.array(target_position2d) - np.array(robot_position2d)
        robot_heading_vec = np.array([np.cos(robot_yaw), np.sin(robot_yaw)])
        heading_err_cross = cross2d( robot_heading_vec, pos_delta / np.linalg.norm(pos_delta) )
        
        #print 'robot_position2d', robot_position2d, 'target_position2d', target_position2d
        print 'pos_delta', pos_delta
        #print 'robot_yaw', robot_yaw
        #print 'norm delta', np.linalg.norm( pos_delta ), 'diffrad', diffrad(robot_yaw, target_pose2d[2])
        #print 'heading_err_cross', heading_err_cross
        print 'robot pose', robot_pose2d, 'target pose', target_pose2d
        
        if arrived or (np.linalg.norm( pos_delta ) < 0.08 and np.fabs(diffrad(robot_yaw, target_pose2d[2]))<0.05) :
            print 'Case 2.1  Stop'
            wcv.desiredWV_R = 0  
            wcv.desiredWV_L = 0
            arrived = True
            return
        elif np.linalg.norm( pos_delta ) < 0.08:    # distance is less than 8cm
            arrived_position = True
            if diffrad(robot_yaw, target_pose2d[2]) > 0:    # radians difference > 0
                print 'Case 2.2.1  Turn right slowly'      
                wcv.desiredWV_R = -0.05 
                wcv.desiredWV_L = 0.05
            else:
                print 'Case 2.2.2  Turn left slowly'
                wcv.desiredWV_R = 0.05  
                wcv.desiredWV_L = -0.05
                
        elif arrived_position or np.fabs( heading_err_cross ) < 0.2:    # not arrived OR heading 
            if(pos_delta[1]<0):     # (y_target - y_robot) < 0
                print 'Case 2.3.1  Straight forward'  
                wcv.desiredWV_R = 0.1
                wcv.desiredWV_L = 0.1
            else:
                print 'Case 2.3.2  Straight backward'  
                wcv.desiredWV_R = -0.1
                wcv.desiredWV_L = -0.1
        else:
            if heading_err_cross < 0:    # cross product of robot vec & target vec < 0
                print 'Case 2.4.1  Turn right'
                wcv.desiredWV_R = -0.1
                wcv.desiredWV_L = 0.1
            else:
                print 'Case 2.4.2  Turn left'
                wcv.desiredWV_R = 0.1
                wcv.desiredWV_L = -0.1
                
        velcmd_pub.publish(wcv)  
        
        rate.sleep()

def navi_loop_ypos(target_pose2d):
    global lr, br;
    velcmd_pub = rospy.Publisher("/cmdvel", WheelVelCmd, queue_size = 1)
    rate = rospy.Rate(100) # 100hz
    
    wcv = WheelVelCmd()
    
    arrived = False
    arrived_position = False
    count = 0
    
    while not rospy.is_shutdown() :
        # 1. get robot pose
        robot_pose3d = lookupTransformList('/map', '/robot_base', lr)
        
        if robot_pose3d is None:
            print '1. Tag not in view, Stop', '/ Target Pose:', target_pose2d
            wcv.desiredWV_R = 0.0  # right, left
            wcv.desiredWV_L = 0.0
            velcmd_pub.publish(wcv)  

            rate.sleep()
            continue
        
        robot_position2d  = robot_pose3d[0:2]
        target_position2d = target_pose2d[0:2]
        
        robot_yaw    = tfm.euler_from_quaternion(robot_pose3d[3:7]) [2]
        robot_pose2d = robot_position2d + [robot_yaw]
        
        rawDataFilt = [0, 0, 0];
        resetVal = [0, 0, 0];
        realSig = [0, 0, 0];

        # Apply AprilTagNoiseCorr function to each direction
        #if count == 0:
            #PrevPos = robot_pose2d
            #resetVal = robot_pose2d
            #realSig = 1
        #else:
            #[rawDataFilt[0], resetVal[0], realSig[0]] = AprilTagNoiseCorr( currentPos[0], PrevPos[0], resetVal[0], realSig[0] )
            #[rawDataFilt[1], resetVal[1], realSig[1]] = AprilTagNoiseCorr( currentPos[1], PrevPos[1], resetVal[1], realSig[1] )
            #[rawDataFilt[2], resetVal[2], realSig[2]] = AprilTagNoiseCorr( currentPos[2], PrevPos[2], resetVal[2], realSig[2] )

        #robot_pose2d = rawDataFilt;
        
        # 2. navigation policy
        # 2.1 if       in the target, 
        # 2.2 else if  close to target position, turn to the target orientation
        # 2.3 else if  in the correct heading, go straight to the target position,
        # 2.4 else     turn in the direction of the target position
        
        pos_delta         = np.array(target_position2d) - np.array(robot_position2d)
        robot_heading_vec = np.array([np.cos(robot_yaw), np.sin(robot_yaw)])
        heading_err_cross = cross2d( robot_heading_vec, pos_delta / np.linalg.norm(pos_delta) )
        
        #print 'robot_position2d', robot_position2d, 'target_position2d', target_position2d
        print 'pos_delta', pos_delta
        #print 'robot_yaw', robot_yaw
        #print 'norm delta', np.linalg.norm( pos_delta ), 'diffrad', diffrad(robot_yaw, target_pose2d[2])
        #print 'heading_err_cross', heading_err_cross
        print 'robot pose', robot_pose2d, 'target pose', target_pose2d
        
        if arrived or (np.linalg.norm( pos_delta ) < 0.08 and np.fabs(diffrad(robot_yaw, target_pose2d[2]))<0.05) :
            print 'Case 2.1  Stop'
            wcv.desiredWV_R = 0  
            wcv.desiredWV_L = 0
            arrived = True
            return
        elif np.linalg.norm( pos_delta ) < 0.08:    # distance is less than 8cm
            arrived_position = True
            if diffrad(robot_yaw, target_pose2d[2]) > 0:    # radians difference > 0
                print 'Case 2.2.1  Turn right slowly'      
                wcv.desiredWV_R = -0.05 
                wcv.desiredWV_L = 0.05
            else:
                print 'Case 2.2.2  Turn left slowly'
                wcv.desiredWV_R = 0.05  
                wcv.desiredWV_L = -0.05
                
        elif arrived_position or np.fabs( heading_err_cross ) < 0.2:    # not arrived OR heading 
            if(pos_delta[1]>0):     # (y_target - y_robot) > 0
                print 'Case 2.3.1  Straight forward'  
                wcv.desiredWV_R = 0.1
                wcv.desiredWV_L = 0.1
            else:
                print 'Case 2.3.2  Straight backward'  
                wcv.desiredWV_R = -0.1
                wcv.desiredWV_L = -0.1
        else:
            if heading_err_cross < 0:    # cross product of robot vec & target vec < 0
                print 'Case 2.4.1  Turn right'
                wcv.desiredWV_R = -0.1
                wcv.desiredWV_L = 0.1
            else:
                print 'Case 2.4.2  Turn left'
                wcv.desiredWV_R = 0.1
                wcv.desiredWV_L = -0.1
                
        velcmd_pub.publish(wcv)  
        
        rate.sleep()

if __name__=='__main__':
    rospy.init_node('apriltag_navi', anonymous=True)
    main()
    
