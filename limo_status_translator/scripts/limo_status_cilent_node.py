#!/usr/bin/env python

from std_msgs.msg import String
from limo_status_translator.srv import GetLimoStatus
import rospy

def Limo_status_cilent():
    rospy.init_node('limo_status_cilent_node')
    Get_Limo_Status = rospy.ServiceProxy('Get_Limo_Status', GetLimoStatus)
    
    rate = rospy.Rate(1)
    for val in range(5):
        response = Get_Limo_Status(val)
        if response == 0:
            pub0 = rospy.Publisher('/limo_ros/vehicle_state', String, queue_size=10)
        elif response == 1:
            pub1 = rospy.Publisher('/limo_ros/control_mode', String, queue_size=10)
        elif response == 2:
            pub2 = rospy.Publisher('/limo_ros/battery_voltage', String, queue_size=10)
        elif response == 3:
            pub3 = rospy.Publisher('/limo_ros/error_code', String, queue_size=10)
        elif response == 4:
            pub4 = rospy.Publisher('/limo_ros/motion_mode', String, queue_size=10)  
        rate.sleep()

if __name__ == "__main__":
        Limo_status_cilent()

