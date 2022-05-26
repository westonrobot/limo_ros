#!/usr/bin/env python

from __future__ import print_function

from limo_status_translator.srv import GetLimoStatus
from limo_status_translator.msg import Num
import rospy

def handle_process_msg(request):
    if request.get_status == 0:
        print('0')
        status_string = "GET_STATUS_VEHICLE_STATE = %s"% Num.vehicle_state
    elif request.get_status == 1:
        print('1')
        status_string = "GET_STATUS_CONTROL_MODE = %s"% Num.control_mode
    elif request.get_status == 2:
        print('2')
        status_string = "GET_STATUS_BATTERY_VOLTAGE = %s"% Num.battery_voltage
    elif request.get_status == 3:
        print('3')
        status_string = "GET_STATUS_ERROR_CODE = %s"% Num.error_code
    elif request.get_status == 4:
        print('4')
        status_string = "GET_STATUS_MOTION_MODE = %s"% Num.motion_mode

    return status_string

def limo_translator():
    rospy.init_node('limo_status_translator_node')
    s = rospy.Service('Get_Limo_Status', GetLimoStatus, handle_process_msg)
    print("Ready to translate.")
    rospy.spin()

if __name__ == "__main__":
    limo_translator()
