#! /usr/bin/env python3

"""
.. module:: NodeB
   :platform: Unix
   :synopsis: Python module for the second assignment of Research Track I course
   
.. moduleauthor:: Manuel Delucchi

A more detailed description of the node:

This node prints the number of target canceled and the number of target reached

Subsribes to:
	/reaching_goal/result
	
"""

import rospy
import actionlib
import actionlib.msg
import assignment_2_2022
import assignment_2_2022.msg
	
# Initialize global count variables to 0
goals_cancelled = 0
goals_reached = 0

def status(msg):
	"""
	Function that updates the number of goals reached or cancelled based on the status 
	
	*Args*: msg
	
	"""
	global goals_cancelled 
	global goals_reached
	
	# Update the number of goals reached or cancelled based on the status
	if msg.status.status == 2:
		goals_cancelled += 1
	elif msg.status.status == 3:
		goals_reached += 1
		
	print("Number of Goals Reached: ", goals_reached)
	print("Number of Goals Cancelled: ", goals_cancelled)
	print("----------------------------------")

if __name__ == '__main__':

	# Init the Node
	rospy.init_node("NodeB")
	
	# Create a subscriber to listen ot the goal result topic
	sub_goal = rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, status)
	
	# Keep the node running
	rospy.spin()
	
