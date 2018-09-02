<header>2.12 Final Project Team 2A Repo</header>

#Structure
#In 'catkin_ws/src':
<dl>
<dt>me212arm - arm control code</dt>
<dd>Dynamixel, IK and RRT code for use with the arms in Lab 5</dd>
<dd>model - robot description (URDF)</dd>
<dd>scripts/collision.py - elementary collision test</dd>
<dd>scripts/joint_state_publisher.py - publishes joint state</dd>
<dd>scripts/planner.py - inverse kinematics solver</dd>
<dd>scripts/rrt.py - rapidly-expanding random tree search algorithm</dd>

<dt>me212bot - high level code (navigation)</dt>
<dd>model - robot description (URDF)</dd>
<dd>scripts/me212helper/helper.py - poses and transforms</dd>
<dd>scripts/me212helper/marker_helper.py - creates markers</dd>
<dd>scripts/apriltag_navi.py - feed velocity for target</dd>
<dd>src/controller/controller.ino - arduino code</dd>
<dd>src/controller/helper.cpp - encoder measurements</dd>
<dd>src/controller/helper.h - updates pose, PI controller</dd>
<dd>setup.py - gets values from scripts</dd>

<dt>me212base - low level code (velocity + arduino)</dt>
<dd>msg - wheel cmd velocity file</dd>
<dd>scripts/apriltag_navi.py - feed velocity for target</dd>
<dd>scripts/helper.py - matrix and pose creation</dd>
<dd>scripts/me212bot.py - prints data</dd>
<dd>src/controller/controller.ino - arduino code</dd>
<dd>src/controller/helper.cpp - encoder measurements</dd>
<dd>src/controller/helper.h - updates pose, PI controller</dd>

<dt>me212cv - computer vision code</dt>
<dd>msg - wheel cmd velocity file</dd>
<dd>scripts/object_detection - identify objects with kinect</dd>
</dl>


#In 'software/config':
<dl>
<dt>environment.sh</dt>
<dd>Required as-is, essentially points your terminal to the files it needs to work with ROS</dd>
<dt>procman.pmd</dt>
<dd>procman config file, adjust this to make your pman show the nodes and launch files you need</dd>
</dl>
