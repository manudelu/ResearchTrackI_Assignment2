#!/usr/bin/env python3

import rospy
import os
import math
from my_robot_controller.msg import RobotMsg

def callback_subscriber(data):
	des_pos_x = rospy.get_param("/des_pos_x")
	des_pos_y = rospy.get_param("/des_pos_y")
	
	cur_pos_x = data.x
	cur_pos_y = data.y
	
	des_pos_distance= math.sqrt(((des_pos_x - cur_pos_x)**2)+((des_pos_y - cur_pos_y)**2))
	
	cur_vel_x = data.vel_x
    cur_vel_y = data.vel_y
    
    cur_vel= math.sqrt(((cur_vel_x)**2)+((cur_vel_y)**2))
    
    global somma = 0
    somma += cur_vel
    
    global count = 0
    
    count += 1
    
    media = somma/count
    

if __name__ == '__main__':

	# Initialization on the Node that we will call NodeC
	rospy.init_node("NodeC")
	
	rospy.Subscriber('my_pos_and_my_vel', RobotMsg, callback_subscriber)
	
	
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		rate.sleep()
	
	rospy.spin()
	
