#! /usr/bin/env python3

"""
.. module:: NodeC
   :platform: Unix
   :synopsis: Python module for the second assignment of Research Track I course
   
.. moduleauthor:: Manuel Delucchi

A more detailed description of the node:

This node prints the robot speed and the distance from the desired target

Subsribes to:
	/pos_vel
	
"""

import rospy
import math

from assignment_2_2022.msg import RobotMsg


def callback_subscriber(msg):
	"""
	Function that calculates the distance between the robot and the goal and the speed of the robot
	
	*Args*: 
	*msg(RobotMsg)*: Contains the coordinates and velocity of the robot
	
	"""
	# Get the desired position from the ROS parameter server
	des_pos_x = rospy.get_param("des_pos_x")
	des_pos_y = rospy.get_param("des_pos_y")

	# Calculate the distance between the current and the desired position
	distance = math.sqrt(pow(des_pos_x - msg.x, 2) + pow(des_pos_y - msg.y, 2))
		
	# Calculate the velocity   
	vel = math.sqrt(pow(msg.vel_x, 2) + pow(msg.vel_y, 2))
		
	# Print distance and velocity
	print("Distance to the goal: ", distance)
	print("Average speed: ", vel)  

if __name__ == '__main__':
	
	# Init the Node
	rospy.init_node("NodeC")
	
	# Setting the rate of publishing chosen in launch file
	freq = rospy.get_param("freq")
	rate = rospy.Rate(freq)
	
	# Subscribe to the RobotMsg topic and pass the info to the callback function
	rospy.Subscriber('/pos_vel', RobotMsg, callback_subscriber)
	
	while not rospy.is_shutdown():
		rate.sleep()
	
	# Keep the node running
	rospy.spin()
	
