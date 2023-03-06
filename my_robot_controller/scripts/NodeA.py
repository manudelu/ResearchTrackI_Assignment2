#!/usr/bin/env python3

import rospy
import actionlib
import actionlib.msg
import assignment_2_2022.msg
import os

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from my_robot_controller.msg import RobotMsg

# This function allows the user to set the coordinates (x, y) of the target 
# position that the robot must reach in the simulation environment
def set_target():
	
	# Ask the user to set the x and y position of the target
	x_pos = input("\nEnter the x value: ")
	y_pos = input("\nEnter the y value: ")
	
	# Print the selected coordinates 
	print("\nThe position of the target is: (", x_pos, ", ", y_pos, ")")
	
	# Wait for the server to be ready to receive the goal 
    client.wait_for_server()

    # Creates a goal to send to the action server
    goal = PoseStamped()
      
    goal.pose.position.x = x_pos
    goal.pose.position.y = y_pos

    goal = assignment_2_2022.msg.PlanningGoal(goal)

    # Sends the goal to the action server
    client.send_goal(goal)
    print("\n**Goal sent to the sever**")
 
    # Back to the interface function 
    user_interface()	

# This function allows to cancel the goal that is sent to the action server
# It is called as soon as the user select it as an option in the UI function
def cancel_target():
	
	# Cancel the goal that is sent to the action server
    client.cancel_goal()
    print("\nThe target has been canceled!!")
        
    # Call the UI function once again
    user_interface()

# User Interface (UI)
# The function is called at the start of the program
# The user can choose between different options by entering the correct number
# If the option choosen is wrong then call again the UI
def user_interface():

	os.system('clear')
	
	print("###############################################\n")    
    print("##          Robot Control Interface          ##\n")
    print("###############################################\n")
    print("## -------> Select 1: Target Position        ##\n")
    print("## -------> Select 2: Cancel                 ##\n")
    print("## -------> Select 3: Exit                   ##\n")
    print("###############################################\n") 
        
    # Ask the user to select an operation
    option = input("Select your operation: ")
        
    # Check the user selection
    if   (option == "1"):
   		set_target()
    elif (option == "2"):
        cancel_target()     	
    elif (option == "3"):
       	exit()    
    else:
        print("Wrong Choise!! Try Again...")
        rospy.sleep(2)
        user_interface()      

def callback(data):
	
	pub = rospy.Publisher('my_pos_and_my_vel', RobotMsg, queue_size = 10)
	my_custom_msg = RobotMsg()
	my_custom_msg.x = data.pose.pose.position.x
    my_custom_msg.y = data.pose.pose.position.y
    my_custom_msg.vel_x = data.twist.twist.linear.x
    my_custom_msg.vel_y = data.twist.twist.linear.y

    my_publisher.publish(my_custom_msg)
	
if __name__ == '__main__':

	# Initialization on the Node that we will call NodeA
	rospy.init_node("NodeA")
	
	rospy.Subscriber("/odom", Odometry, callback)
	
    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    
	# Call the UI function
	user_interface()
	
	# Spin() keeps python from exiting until the ROS node is stopped
	rospt.spin()
