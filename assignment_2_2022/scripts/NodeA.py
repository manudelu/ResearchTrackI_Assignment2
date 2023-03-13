#! /usr/bin/env python3

"""
.. module:: NodeA
   :platform: Unix
   :synopsis: Python module for the second assignment of Research Track I course 
   
.. moduleauthor:: Manuel Delucchi

A more detailed description of the node:

This node implements an action client allowing the user to set a target (x,y) or to cancel it at any time. 
Also it publishes the robot position and velocity as a custom message by reling on the topic /odom.  

Subsribes to:
	/odom
	
Publishes to:
	/pos_vel
	
"""

import rospy
import os
import actionlib
import actionlib.msg
import assignment_2_2022
import assignment_2_2022.msg

from std_srvs.srv import *
from geometry_msgs.msg import Point, Pose, Twist
from nav_msgs.msg import Odometry
from assignment_2_2022.msg import RobotMsg

def callback(msg):
	"""
	Callback function to publish position and velocity of the robot taken from */odom* topic
	
	*Args*: 
	*msg(Odometry)*: Contains the odometry of the robot
	
	"""
	global pub
	
	# Create a custom message
	my_custom_msg = RobotMsg()
	
	# Set the robot position and linear velocity
	my_custom_msg.x = msg.pose.pose.position.x
	my_custom_msg.y = msg.pose.pose.position.y
	my_custom_msg.vel_x = msg.twist.twist.linear.x
	my_custom_msg.vel_y = msg.twist.twist.linear.y
    
	# Publish the message
	if not rospy.is_shutdown():
		pub.publish(my_custom_msg)

def get_target():		
	"""
		Function that ask the user to set the x and y position of the target and check whether the input is valid
		
		*Args*: None
		
	"""
	while True:
		try:
			x_pos = float(input("Enter the x value: "))
		except:
			print("Please enter a valid number!!")			
		else:
			break
			
	while True:
		try:
			y_pos = float(input("Enter the y value: "))
		except:
			print("Please enter a valid number!!")			
		else:			
			break	
			
	return x_pos, y_pos

def set_target():
	"""
	Function that allows the user to set the coordinates (x, y) of the target position that
	the robot must reach inside the simulation environment and send the target (goal) to the action server
	
	*Args*: None
	"""
	# Get target position from the get_target() function defined above
	(x_pos, y_pos) = get_target()
	
	# Print the selected coordinates 
	print("The position of the target is: (", x_pos, ", ", y_pos, ")")

	# Creates a goal message with the target coordinates
	goal = assignment_2_2022.msg.PlanningGoal()
	goal.target_pose.pose.position.x = x_pos
	goal.target_pose.pose.position.y = y_pos
    
	# Send the goal to the action server
	client.send_goal(goal)
	print("The target has been successfully sent to the sever!!")
 
	# Back to the interface function
	rospy.sleep(3)
	user_interface()	

def cancel_target():
	"""
	Function that checks whether there is an active goal and allows to cancel it
	
	*Args*: None
	
	"""
	# If there is an active goal then cancel it
	if client.get_state() == actionlib.GoalStatus.ACTIVE:
		client.cancel_goal()
		print("The target has been cancelled successfully!!")
	# If there is no active goal then display an error message
	else:
		print("Error. There's no target to cancel.")
        
	# Back to the interface function
	rospy.sleep(2)
	user_interface()

def user_interface():
	"""
	*User Interface (UI)*
	The function is called at the start of the program
	The user can choose to set a goal, to cancel it or to exit the program by entering the correct number
	
	*Args*: None
	
	"""
	# Clean the screen 
	os.system('clear')
	
	print("###############################################\n")    
	print("##          Robot Control Interface          ##\n")
	print("###############################################\n")
	print("## -------> Select 1: Target Position        ##\n")
	print("## -------> Select 2: Cancel Position        ##\n")
	print("## -------> Select 3: Exit                   ##\n")
	print("###############################################\n") 
        
	# Ask the user to select an operation
	choice = input("Select your operation: ")
        
	# Check the user selection
	if   (choice == "1"):
		set_target()
	elif (choice == "2"):
		cancel_target()     	
	elif (choice == "3"):
		print("Shutdown!! You'll no longer be able to interact with the interface!")
		rospy.sleep(2)
		exit()  
	else:
		print("Wrong choise!! Try Again...")
		rospy.sleep(2)
		user_interface()      
	
if __name__ == '__main__':

	# Init Node
	rospy.init_node("NodeA")
	
	# Define a global publisher in order to publish the RobotMsg custom message
	global pub
	pub = rospy.Publisher("/pos_vel", RobotMsg, queue_size = 1)

	# Define a subscriber which listen to the Odometry message and calls the callback function
	rospy.Subscriber("/odom", Odometry, callback)
    
	# Create a new client
	client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2022.msg.PlanningAction)	
    
	# Wait for the server to be ready to receive the goal 
	client.wait_for_server()
    
	# Call the UI function
	user_interface()
