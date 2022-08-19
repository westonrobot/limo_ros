#!/usr/bin/env python
import rospy
from limo_status_translator.srv import *
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node('limo_status_client_node', anonymous=True)



    abc_client = rospy.ServiceProxy('abc', GetLimoStatus)

    r = rospy.Rate(1)

    pub_vs = rospy.Publisher('limo_status/vehicle_state', String, queue_size=10)
    pub_cm = rospy.Publisher('limo_status/control_mode', String, queue_size=10)
    pub_bv = rospy.Publisher('limo_status/battery_voltage', String, queue_size=10)
    pub_ec = rospy.Publisher('limo_status/error_code', String, queue_size=10)
    pub_mm = rospy.Publisher('limo_status/motion_mode', String, queue_size=10)

    while not rospy.is_shutdown():
        req = GetLimoStatusRequest()
        for x in range(0, 5):
            # print(req)
            req.get_status = x
            rospy.loginfo("Generated [%d], sending addition request..." % (x))
            resp = abc_client(req)
            # rospy.loginfo("Received response: %s" % resp.status_string)
            
            pub_vs.publish(resp.status_string)
            pub_cm.publish(resp.status_string)
            pub_bv.publish(resp.status_string)
            pub_ec.publish(resp.status_string)
            pub_mm.publish(resp.status_string)

    
    
    
        
        # req.second = b


        # resp = calc_client(a, b)


        r.sleep()
