#!/usr/bin/env python
import rospy
from limo_status_translator.srv import *

if __name__ == "__main__":
    rospy.init_node('client')

    abc_client = rospy.ServiceProxy('abc', GetLimoStatus)

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        req = GetLimoStatusRequest()
        for x in range(0, 5):
            # print(req)
            req.get_status = x
            rospy.loginfo("Generated [%d], sending addition request..." % (x))
            resp = abc_client(req)
            rospy.loginfo("HIIIIReceived response: %s" % resp.status_string)


        
        
        # req.second = b


        # resp = calc_client(a, b)


        r.sleep()
