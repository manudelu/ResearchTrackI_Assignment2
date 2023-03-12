#!/usr/bin/env python3

import rospy
import os
import actionlib
import actionlib.msg
import assignment_2_2022.msg
import my_robot_controller.msg

from std_srvs.srv import *
from geometry_msgs.msg import Point, Pose, Twist
from nav_msgs.msg import Odometry
from my_robot_controller.msg import RobotMsg

def callback(msg):
	"""
	Callback function to publish position and velocity of the robot
	
	Args: msg
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
		my_pub.publish(my_custom_msg)

def set_target():
	"""
	Function that allows the user to set the coordinates (x, y) of the target 
	position that the robot must reach in the simulation environment
	
	Args: None
	"""
	
	# Ask the user to set the x and y position of the target
	x_pos = float(input("Enter the x value: "))
	y_pos = float(input("Enter the y value: "))
	
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
    user_interface()	

def cancel_target():
	"""
	This function allows to cancel the goal that is sent to the action server
	It is called as soon as the user select it as an option in the UI function
	
	Args: None
	
	"""
	# If there is an active goal then cancel it
	if client.get_state() == actionlib.GoalStatus.ACTIVE:
    	client.cancel_goal()
    	print("The target has been cancelled successfully!!")
    # If there is no active goal then display an error message
    else:
    	print("Error. There's no target to cancel.")
        
    # Back to the interface function
    user_interface()

def user_interface():
	"""
	User Interface (UI)
	The function is called at the start of the program
	The user can choose between different options by entering the correct number
	If the option choosen is wrong then call again the UI
	
	Args: None
	"""
	# Create a new client
    client = actionlib.SimpleActionClient('/reaching_goal', assignment_2_2022.msg.PlanningAction)	
    
    # Wait for the server to be ready to receive the goal 
    client.wait_for_server()
	
	# Clean the screen
	rospy.sleep(2) 
	os.system('clear')
	
	print("###############################################\n")    
    print("##          Robot Control Interface          ##\n")
    print("###############################################\n")
    print("## -------> Select 1: Target Position        ##\n")
    print("## -------> Select 2: Cancel                 ##\n")
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
       	rospy.signal_shutdown("Exiting...")    
    else:
        print("Wrong choise!! Try Again...")
        user_interface()      
	
if __name__ == '__main__':

	# Init Node
	rospy.init_node("NodeA")
	
	# Define a global publisher in order to publish the RobotMsg custom message
	global pub
	pub = rospy.Publisher("/pos_vel", RobotMsg, queue_size = 1)

    # Define a subscriber which listen to the Odometry message and calls the callback function
    rospy.Subscriber("/odom", Odometry, callback)
    
	# Call the UI function
	user_interface()
	
	# Spin() keeps python from exiting until the ROS node is stopped
	rospt.spin()
