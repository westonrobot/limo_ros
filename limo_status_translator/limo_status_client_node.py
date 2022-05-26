#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo("%s", data.data)

def get_status():
    	rospy.init_node('limo_status_client_node', anonymous=True)
	sub = rospy.Subscriber('status_from_translator', String, callback)
	pub = rospy.Publisher('status_received', String, queue_size=1)
    	rate = rospy.Rate(1)

    	while not rospy.is_shutdown():
			for get_status in range(0,5):
				if get_status == 0 : request_str = "0"
        			#rospy.loginfo(request_str)
        			pub.publish(request_str)
        			rate.sleep()
				if get_status == 1 : request_str = "1"
        			#rospy.loginfo(request_str)
        			pub.publish(request_str)
        			rate.sleep()
				if get_status == 2 : request_str = "2"
        			#rospy.loginfo(request_str)
        			pub.publish(request_str)
        			rate.sleep()
				if get_status == 3 : request_str = "3"
        			#rospy.loginfo(request_str)
        			pub.publish(request_str)
        			rate.sleep()
				if get_status == 4 : request_str = "4"
        			#rospy.loginfo(request_str)
        			pub.publish(request_str)
        			rate.sleep()
				#rospy.loginfo(request_str)
				
if __name__ == '__main__':
    try:
        get_status()
    except rospy.ROSInterruptException:
        pass