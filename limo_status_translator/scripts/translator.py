#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from limo_status_translator.srv import *
from limo_status_translator.msg import *

def callback(req):

    if req.get_status == 0:
        # hello_str = "Vehicle status is " + str(req.get_status)
        print("vehicle state")
        if req.GET_STATUS_VEHICLE_STATE == 0x00:
            status_str = "System normal"
        else:
            status_str = hello_str + "System exception"
    elif req.get_status == 1:
        print("control mode")
        if req.GET_STATUS_CONTROL_MODE == 0x00:
            status_str = "Standby"
        elif req.GET_STATUS_CONTROL_MODE == 0x01:
            status_str = "Command Control"
        elif req.GET_STATUS_CONTROL_MODE == 0x02:
            status_str = "App Control"
        elif req.GET_STATUS_CONTROL_MODE == 0x03:
            status_str = "Remote Control"
    elif req.get_status == 2:
            status_str = "Battery voltage level: " + str(req.GET_STATUS_BATTERY_VOLTAGE)
            print("battery volt")
    elif req.get_status == 3:
            #bit 0 and bit 1 will not be accessed cuz it's 0b
            #access the bits from [2] onwards to [11]
            error_code = bin(req.GET_STATUS_ERROR_CODE)
            print(type(error_code))
            if(error_code[2] == 1):
                status_str = "Battery undervoltage fault"
            elif(error_code[3] == 1):
                status_str = "Battery undervoltage warning"
            elif(error_code[4] == 1):
                status_str = "Remote control connection loss"
            elif(error_code[5] == 1):
                status_str = "(Motor No. 1) Steering motor driver communication failure"
            elif(error_code[6] == 1):
                status_str = "(Motor No. 2) Steering motor driver communication failure"
            elif(error_code[7] == 1):
                status_str = "(Motor No. 3) Steering motor driver communication failure"
            elif(error_code[8] == 1):
                status_str = "(Motor No. 4) Steering motor driver communication failure"
            elif(error_code[10] == 1):
                status_str = "Driver failure"
            elif(error_code[10] == 1):
                status_str = "Upper layer communication status"
    elif req.get_status == 4:
        print("motion mode")
        if req.GET_STATUS_MOTION_MODE == 0x00:
            status_str = "Motion mode is 4-wheel differential"
        elif req.GET_STATUS_MOTION_MODE == 0x01:
            status_str = "Motion mode is Ackerman"
        elif req.GET_STATUS_MOTION_MODE == 0x02:
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

