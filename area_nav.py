#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

def inp():
	print("Input a list of X,Y,Z coordinates (ex. [(-1,3),(-3,3),(3,0)]), or enter 'go' to use the default coordinates:\n")
	coordinate_list = input()
	if type(coordinate_list) != list():
		coordinate_list = [(-8,-8),(-4,-8),(-4,-4),(-8,-4),(-8,-8), #top left building
                                   (-4,-8),(0,-8),(4,-8),(8,-8),(8,-4),(4,-4),(4,-8),(8,-8),(8,-4),(8,0),(8,4), #bottom left building
                                   (8,8),(4,8),(4,4),(8,4),(8,8),(4,8),(0,8),(-4,8), #bottom right building
                                   (-8,8),(-8,4),(-4,4),(-4,8),(-8,8),(-8,4),(-8,0),(-8,-4),(-8,-8)] #top right building and return to start
	return coordinate_list

def send(coord, goal_publisher, time):
	goal = PoseStamped()

       	goal.header.seq = 0
       	goal.header.stamp = rospy.Time.now()
       	goal.header.frame_id = "map"

       	goal.pose.position.x = coord[0]
	goal.pose.position.y = coord[1]
	goal.pose.position.z = 0.0

        goal.pose.orientation.w = 1.0

       	rospy.sleep(1)
		
       	print("Publishing point {}".format(coord))
       	goal_publisher.publish(goal)
       	rospy.sleep(time)

def send_msgs(coordinate_list, goal_publisher):
	for i in range(len(coordinate_list)):
                coord = coordinate_list[i]
                if i == 0:
                        send(coord, goal_publisher, 30)
                else:
                        send(coord, goal_publisher, 9)

	print("Done.")
	return

def main():               
	rospy.init_node("area_nav")
	pub = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=5)
        
	coordinate_list = inp()
	send_msgs(coordinate_list, pub)

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		print("ERROR")