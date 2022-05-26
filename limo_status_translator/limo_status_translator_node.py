#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "%s", data.data)

def status_string():
	rospy.init_node('limo_status_translator_node', anonymous=True)
	rospy.Subscriber('limo_status', String, callback)
	rospy.Subscriber('status_received')
	pub = rospy.Publisher('status_from_translator', String, queue_size=1)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		rtn_str = "(requested status message) %s" % rospy.get_time()
		rospy.loginfo(rtn_str)
		pub.publish(rtn_str)
		rate.sleep()

if __name__ == '__main__':
    try:
        status_string()
    except rospy.ROSInterruptException:
        pass
