#!/usr/bin/env python
import rospy
from limo_status_client.srv import *

if __name__ == "__main__":
    rospy.init_node('client')

    abc_client = rospy.ServiceProxy('abc', GetLimoStatus)

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        while 1:
            for x in range(0, 5):
                req = GetLimoStatusRequest()

                # print(req)
                req.get_status = x
                rospy.loginfo("Generated [%d], sending addition request..." % (x))
                # req.second = b
                resp = abc_client(x)
                # resp = GetLimoStatusResponse()
                # resp = calc_client(a, b)

                rospy.loginfo("HIIIIReceived response: %d" % resp.status_string)

                # r.sleep()
                if x == 4:
                    x = 0