#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from limo_status_translator.srv import *
from limo_status_translator.msg import *

def callback(req):

    if req.get_status == 0:
        # hello_str = "Vehicle status is " + str(req.get_status)
        if req.vehicle_state == 0x00:
            status_str = "System normal"
        else:
            status_str = hello_str + "System exception"
    else if req.get_status == 1:
        if req.vehicle_state == 0x00:
            status_str = "Standby"
        else if req.vehicle_state == 0x01:
            status_str = "Command Control"
        else if req.vehicle_state == 0x02:
            status_str = "App Control"
        else if req.vehicle_state == 0x03:
            status_str = "Remote Control"
    else if req.get_status == 2:
            status_str = "Battery voltage level: " str(req.battery_voltage)
    else if req.get_status == 3:
            #bit 0 and bit 1 will not be accessed cuz it's 0b
            #access the bits from [2] onwards to [11]
            error_code = bin(req.error_code)
            if(error_code[2] == 1):
                status_str = "Battery undervoltage fault"
            else if(error_code[3] == 1):
                status_str = "Battery undervoltage warning"
            else if(error_code[4] == 1):
                status_str = "Remote control connection loss"
            else if(error_code[5] == 1):
                status_str = "(Motor No. 1) Steering motor driver communication failure"
            else if(error_code[6] == 1):
                status_str = "(Motor No. 2) Steering motor driver communication failure"
            else if(error_code[7] == 1):
                status_str = "(Motor No. 3) Steering motor driver communication failure"
            else if(error_code[8] == 1):
                status_str = "(Motor No. 4) Steering motor driver communication failure"
            else if(error_code[10] == 1):
                status_str = "Driver failure"
            else if(error_code[10] == 1):
                status_str = "Upper layer communication status"
    else if req.get_status == 4:
        if req.motion_mode == 0x00:
            status_str = "Motion mode is 4-wheel differential"
        else if req.motion_mode = 0x01:
            status_str = "Motion mode is Ackerman"
        else if req.motion_mode = 0x02:
            status_str = "Motion mode is Mecanum"    

    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', req.get_status)
    resp = GetLimoStatusResponse()
    resp.status_string = status_str
    return resp

if __name__ == '__main__':
    rospy.init_node('translator_node')
    rospy.Service('abc', GetLimoStatus, callback)

    rospy.loginfo("Translation ready")
    rospy.spin()

