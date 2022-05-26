#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# callback from client
client_data = None

def callback_client(data):
	global client_data
	client_data = data.data
	rospy.loginfo("%s", client_data) 

# callback to limo
def callback_limo(data):
	rospy.loginfo("%s", data.data)

def status_string():
	rospy.init_node('limo_status_translator_node', anonymous=True)
	#sub_limo = rospy.Subscriber('limo_status', String, callback_limo)
	sub_client = rospy.Subscriber('status_received', String, callback_client)
	pub_client = rospy.Publisher('status_from_translator', String, queue_size=0)
	rate = rospy.Rate(1)
	rtn_str = "Status"
	

	while not rospy.is_shutdown():
		if client_data == "0" : rtn_str = "STATUS 0"
		if client_data == "1" : rtn_str = "STATUS 1"
		if client_data == "2" : rtn_str = "STATUS 2"
		if client_data == "3" : rtn_str = "STATUS 3"
		if client_data == "4" : rtn_str = "STATUS 4"
		# communicate to client - return a string
		pub_client.publish(rtn_str)
		rate.sleep()
		rospy.loginfo(rtn_str + " sent")

if __name__ == '__main__':
    try:
        status_string()
    except rospy.ROSInterruptException:
        pass
