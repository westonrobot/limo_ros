!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def intercept():
    	rospy.init_node('intercept', anonymous=True)
	sub = rospy.Subscriber('chat', String, callback)
	pub = rospy.Publisher('chatter', String, queue_size=1)
    	rate = rospy.Rate(10) # 10hz

    	while not rospy.is_shutdown():
        	intercept_str = "Intercept %s" % rospy.get_time()
        	rospy.loginfo(intercept_str)
        	pub.publish(intercept_str)
        	rate.sleep()

if __name__ == '__main__':
    try:
        intercept()
    except rospy.ROSInterruptException:
        pass
