#!/usr/bin/env python
# coding: utf-8
import rospy
from std_msgs.msg import String

def callback(data):
    #Display the received data in the terminal
    #Data is data.Received in data
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
      
def node():
    #Declare node name
    rospy.init_node('limo_status_translator_node.py', anonymous=True)
    #Create a Subscriber. Load the topic.
    sub = rospy.Subscriber('chatter', String, callback)
    #Create Publisher('Topic name',Mold,size)
    pub = rospy.Publisher('chatter2', String, queue_size=10)
    #Loop period.
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        #Fill in the data to publish
        hello_str = "hello world %s" % rospy.get_time()
        #Display the data to publish in the terminal
        rospy.loginfo(hello_str)
        #Publish data
        pub.publish(hello_str)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInitException:
        pass