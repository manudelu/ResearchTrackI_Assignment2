#!/usr/bin/env python3

import rospy
import math

from my_robot_controller.msg import RobotMsg

def callback_subscriber(data):
	# Get the desired position from the ROS parameter server
	des_pos_x = rospy.get_param("des_pos_x")
	des_pos_y = rospy.get_param("des_pos_y")

	# Calculate the distance between the current and the desired position
	distance = math.sqrt(pow(des_pos_x - data.x, 2) + (pow(des_pos_y - data.y, 2))
	
	# Calculate the velocity   
    vel = math.sqrt(pow(data.v_x, 2) + pow(data.v_y, 2))
    
    # Print distance and velocity
    rospy.loginfo("Distance to the goal: ", distance)
    rospy.loginfo("Average speed: ", vel)
    

if __name__ == '__main__':

	# Init the Node
	rospy.init_node("NodeC")
	
	# Subscribe to the RobotMsg topic and pass the info to the callback function
	rospy.Subscriber('my_pos_and_my_vel', RobotMsg, callback_subscriber)
	
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		rate.sleep()
	
	# Keep the node running
	rospy.spin()
	
