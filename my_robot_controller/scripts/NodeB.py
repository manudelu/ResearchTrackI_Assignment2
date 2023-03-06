#!/usr/bin/env python3

import rospy
import os
import assignment_2_2022.msg

# Initialize global count variables to 0
count_cancelled = 0
count_reached = 0

def status(data):
	global count_cancelled 
	global count_reached 
	
	if data.status.status == 2:
		count_cancelled += 1
	elif data.status.status == 3:
		count_reached += 1


if __name__ == '__main__':

	# Initialization on the Node that we will call NodeB
	rospy.init_node("NodeB")
	
	rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, status)
	
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		rate.sleep()
	
	rospy.spin()
	
	
