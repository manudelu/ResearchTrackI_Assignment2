#!/usr/bin/env python3

import rospy
import actionlib
import actionlib.msg
import assignment_2_2022.msg
import os
import sys

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from rt1a2.msg import custom_odom

if __name__ == '__main__':
	rospy.init_node("NodeA")
	
	rospy.loginfo("Hello from NodeA")
	
	rospy.sleep(1.0)
	
	rospy.loginfo("Program Ended")
