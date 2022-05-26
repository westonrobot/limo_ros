#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback1(data):
	rospy.loginfo("%s", data.data)

def status_string():
	rospy.init_node('limo_status_translator_node', anonymous=True)
	#sub1 = rospy.Subscriber('limo_status', String, callback2)
	sub2 = rospy.Subscriber('status_received', String, callback1)
	pub = rospy.Publisher('status_from_translator', String, queue_size=1)
	rate = rospy.Rate(1) # 10hz

	while not rospy.is_shutdown():
		rtn_str = "STATUS"
		pub.publish(rtn_str)
		rate.sleep()
		rospy.loginfo(rtn_str)

if __name__ == '__main__':
    try:
        status_string()
    except rospy.ROSInterruptException:
        pass
