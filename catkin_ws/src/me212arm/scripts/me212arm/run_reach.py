#!/usr/bin/python

# 2.12 Lab 5 trajectory planning
# Peter Yu Oct 2016
import rospy
import planner
import std_msgs.msg, sensor_msgs.msg
import numpy as np
from me212base.msg import gripper

port = '/dev/ttyACM0'

exec_joint1_pub = rospy.Publisher('/joint1_controller/command', std_msgs.msg.Float64, queue_size=1)
exec_joint2_pub = rospy.Publisher('/joint2_controller/command', std_msgs.msg.Float64, queue_size=1)
exec_joint_pub = rospy.Publisher('/virtual_joint_states', sensor_msgs.msg.JointState, queue_size=10)
gripper_pub = rospy.Publisher('gripper', gripper, queue_size=1);
use_real_arm = rospy.get_param('/real_arm', False)

def main():
    radius = 0.05          # (meter)
    center = [0.2, 0.15]  # (x,z) meter
    
    robotjoints = rospy.wait_for_message('/joint_states', sensor_msgs.msg.JointState)
    q0 = robotjoints.position
    rospy.sleep(1)

    #for theta in np.linspace(0, 4*np.pi):
    for i in np.linspace(0.15,0.3,5):   
        #target_xz = [center[0] + radius * np.cos(theta) , center[1] + radius * np.sin(theta) ]
        target_xz = [i,-0.02]

        #target_xz = [-0.035,0.29]
        q_sol = planner.ik(target_xz, q0)
        if q_sol is None:
            print 'no ik solution'
        else:
            print '(q_1,q_2)=', q_sol
            if use_real_arm:
                exec_joint1_pub.publish(std_msgs.msg.Float64(q_sol[0]))
                exec_joint2_pub.publish(std_msgs.msg.Float64(q_sol[1]))
            else:
                js = sensor_msgs.msg.JointState(name=['joint1', 'joint2'], position = q_sol)
                exec_joint_pub.publish(js)
            q0 = q_sol

            rospy.sleep(1)


    print('The gripper may start moving');
    gripper_msg = gripper()
    gripper_msg.task = 1
    gripper_pub.publish(gripper_msg);
    print('The gripper command is working');

if __name__ =="__main__":
    rospy.init_node("run_reach")
    main();
