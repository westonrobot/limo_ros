#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback1(data):
	rospy.loginfo(rospy.get_caller_id() + "Vehicle sate is %s", data.data)

def callback2(data):
	rospy.loginfo(rospy.get_caller_id() + "Control mode is %s", data.data)

def callback3(data):
	rospy.loginfo(rospy.get_caller_id() + "Battery voltage is %s", data.data)

def callback4(data):
	rospy.loginfo(rospy.get_caller_id() + "Error code is %s", data.data)

def callback5(data):
	rospy.loginfo(rospy.get_caller_id() + "Motion mode is %s", data.data)

def listener():
    rospy.init_node('client', anonymous=True)
	rospy.Subscriber('vehicle state', String, callback1)
	rospy.Subscriber('control mode', String, callback2)
	rospy.Subscriber('battery voltage', String, callback3)
	rospy.Subscriber('error code', String, callback4)
	rospy.Subscriber('motion code', String, callback5)
    rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        request = "requesting" % rospy.get_time()
        rospy.loginfo(request)
        pub.publish(request)
        rate.sleep()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass