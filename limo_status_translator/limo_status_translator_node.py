#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# callback from client
def callback_client(data):
	rospy.loginfo("%s", data.data)

# callback to limo
def callback_limo(data):
	rospy.loginfo("%s", data.data)

def status_string():
	rospy.init_node('limo_status_translator_node', anonymous=True)
	#sub_limo = rospy.Subscriber('limo_status', String, callback_limo)
	sub_client = rospy.Subscriber('status_received', String, callback_client)
	pub_client = rospy.Publisher('status_from_translator', String, queue_size=0)
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		# communicate to client - return a string
		rtn_str = "STATUS"
		pub_client.publish(rtn_str)
		rate.sleep()
		rospy.loginfo(rtn_str + " sent")

if __name__ == '__main__':
    try:
        status_string()
    except rospy.ROSInterruptException:
        pass
