#!/usr/bin/env python
# coding: utf-8


    #Subscribe to the “/limo_status” topic.
    #Process the message received from the “/limo_status” topic into a “human readable string”
    #Implement a service (.srv file given), that will respond with the correct string depending on what was requested.
    #e.g. if get_status = 4, that means the client is requesting for the status_string corresponding to the robot’s current motion_mode





import rospy

from LIMO_STATUS_TRANSLATOR.srv import GetLimoStatus
#(GET_STATUS_VEHICLE_STATE, GET_STATUS_CONTROL_MODE, GET_STATUS_BATTERY_VOLTAGE, GET_STATUS_ERROR_CODE, GET_STATUS_MOTION_MODE)


def __init__(self):
        pass
def get_status_vehicle_state(self,req):
        rospy.loginfo('Vehicle State    ')
        response = 'GetLimoStatus.srv'.GET_STATUS_VEHICLE_STATERESPONSE()
        return response
def get_status_control_mode(self,req):
        rospy.loginfo('Control Mode    ')
        response = 'GetLimoStatus.srv'.GET_STATUS_CONTROL_MODERESPONSE()
        return response    
def get_status_battery_voltage(self,req):
        rospy.loginfo('Battery Voltage    ')
        response = 'GetLimoStatus.srv'.GET_STATUS_BATTERY_VOLTAGERESPONSE()
        return response
def get_status_error_code(self,req):
        rospy.loginfo('error code    ')
        response = 'GetLimoStatus.srv'.GET_STATUS_ERROR_CODERESPONSE()
        return response   
def get_status_motion_mode(self,req):
        rospy.loginfo('Motion Mode    ')
        response = 'GetLimoStatus.srv'.GET_STATUS_MOTION_MODERESPONSE()
        return response    

def node():
        rospy.init_node('limo_status_translator_node', anoymous=True)
        get_status_vehicle_state = rospy.Service('get_status_vehicle_state', GET_STATUS_VEHICLE_STATE)   
        if __name__ == '__main__':
            try:
                node()
            except rospy.ROSInitException:
                pass