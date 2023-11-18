#!/usr/bin/env python3
import rospy, random
from limo_status_client.srv import *

if __name__ == "__main__":
    rospy.init_node('client')

    abc_client = rospy.ServiceProxy('abc', GetLimoStatus)

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        req = GetLimoStatusRequest()
        for x in range(0, 5):
            # print(req)
            req.get_status = x
        rospy.loginfo("Generated [%d, %d], sending addition request..." % (a, b))

        
        
        # req.second = b

        resp = abc_client(req)

        # resp = calc_client(a, b)

        rospy.loginfo("Received response: %d" % resp.status_string)

        r.sleep()