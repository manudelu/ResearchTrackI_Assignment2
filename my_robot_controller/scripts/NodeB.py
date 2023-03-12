#!/usr/bin/env python3

import rospy
import actionlib
import actionlib.msg
import assignment_2_2022
import assignment_2_2022.msg

from my_robot_controller.srv import target, targetResponse 
	
# Initialize global count variables to 0
goals_cancelled = 0
goals_reached = 0

def target_srv(request):
	global goals_cancelled 
	global goals_reached 
	
	# Get the current number of goals reached and cancelled
	goals_reached = goals_reached
	goals_cancelled = goals_cancelled
	
	# Print the current number of goals reached and cancelled 
	print("Number of goals reached: ", goals_reached)
	print("Number of goals cancelled: ", goals_cancelled)
	
	# Create and return the responde for the goal service
	response = targetResponce()
	responce.goals_reached = goals_reached
	responce.goals_cancelled = goals_cancelled
	return responce
	
def status(msg):
	global goals_cancelled 
	global goals_reached
	
	# Update the number of goals reached or cancelled based on the status
	if msg.status.status == 2:
		count_cancelled += 1
	elif msg.status.status == 3:
		count_reached += 1

if __name__ == '__main__':

	# Init the Node
	rospy.init_node("NodeB")
	
	# Create a service server
	target = rospy.Service("goal", target, target_srv)
	
	# Create a subscriber to listen ot the goal result topic
	sub_goal = rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, status)
	
	# Keep the node running
	rospy.spin()
	
