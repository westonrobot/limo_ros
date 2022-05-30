#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from limo_status_translator.srv import *
from limo_status_translator.msg import *

def callback(req):
    rospy.loginfo('-------I heard %s-------', req.get_status)

    if req.get_status == 0:
        if req.GET_STATUS_VEHICLE_STATE == 0x00:
            status_str = "System normal"
        else:
            status_str = hello_str + "System exception"
        #print vehicle state
        infolog = "Vehicle state: " + status_str
        print(infolog)
    elif req.get_status == 1:
        if req.GET_STATUS_CONTROL_MODE == 0x00:
            status_str = "Standby"
        elif req.GET_STATUS_CONTROL_MODE == 0x01:
            status_str = "Command Control"
        elif req.GET_STATUS_CONTROL_MODE == 0x02:
            status_str = "App Control"
        elif req.GET_STATUS_CONTROL_MODE == 0x03:
            status_str = "Remote Control"
        #print control mode
        infolog = "Control mode: " + status_str
        print(infolog)

    elif req.get_status == 2:
        status_str = "Battery voltage level: " + str(req.GET_STATUS_BATTERY_VOLTAGE)
        #print battery level
        print(status_str)
    elif req.get_status == 3:
            #bit 0 and bit 1 will not be accessed cuz it's 0b
            #access the bits from [2] onwards to [11]
        print(req.GET_STATUS_ERROR_CODE)
        terror_code = bin(req.GET_STATUS_ERROR_CODE)
        # error_code = terror_code.zfill(12)
        error_code = '{:<012}'.format(terror_code)
        # temp = '{:<012}' #--> zfill has same function as {:<012}
        # error_code = temp.format(terror_code)
        print(error_code)
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
        elif(error_code[11] == 1):
            status_str = "Upper layer communication status"
        else:
            status_str = "No error"
        #print error code
        infolog = "Error code: " + status_str
        print(infolog)
    elif req.get_status == 4:
        if req.GET_STATUS_MOTION_MODE == 0x00:
            status_str = "Motion mode is 4-wheel differential"
        elif req.GET_STATUS_MOTION_MODE == 0x01:
            status_str = "Motion mode is Ackerman"
        elif req.GET_STATUS_MOTION_MODE == 0x02:
            status_str = "Motion mode is Mecanum" 
        else:
            status_str = "Not detected"
        #print Motion mode
        infolog = "Motion mode: " + status_str
        print(infolog)
    resp = GetLimoStatusResponse()
    resp.status_string = status_str
    return resp

def listen(data):
    rospy.loginfo("Message received\nVehicle state:%s\nControl Mode: %s\nBattery Voltage:%s\nError Code: %s\nMotion Code: %s\n", 
                    data.vehicle_state, data.control_mode, data.battery_voltage, data.error_code, data.motion_mode)

if __name__ == '__main__':
    rospy.init_node('translator_node')
    pub = rospy.Subscriber('limo_status', LimoStatus, listen)

    rospy.Service('abc', GetLimoStatus, callback)

    rospy.loginfo("Translation ready")
    rospy.spin()

