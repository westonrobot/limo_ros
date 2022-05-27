#!/usr/bin/env python

# import sys
from __future__ import print_function
from typing import List
from limo_status_translator.srv import *
from std_msgs.msg import String
import rospy
listClient = list()
listError = list()

def get_status_client(num):
    rospy.wait_for_service('translator_service')
    try:
        get_status = rospy.ServiceProxy('translator_service', GetLimoStatus)
        resp1 = get_status(num)
        return resp1.status_string
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def talker():
    veh = rospy.Publisher('limo_status/vehicle_state', String, queue_size=10)
    con = rospy.Publisher('limo_status/control_mode', String, queue_size=10)
    batt = rospy.Publisher('limo_status/battery_voltage', String, queue_size=10)
    err = rospy.Publisher('limo_status/error_code', String, queue_size=10)
    motion = rospy.Publisher('limo_status/motion_mode', String, queue_size=10)
    rospy.init_node('limo_status_client_node', anonymous=True)

    veh.publish(listClient[0])
    con.publish(listClient[1])
    batt.publish(listClient[2])
    err.publish(listClient[3])
    motion.publish(listClient[4])

def error_print(value):
    count = int()
    strError = str()
    for j in range(6,15):
        if value[j] == '1':
            print("Bit[%d], has error" % 16-value)
            strError += '\nBit[' + j + '], has error'
            count+=1
    if count == 0:
        print("System has no fault")
        strError += '\nSystem has no fault'
    count = 0
    listClient[3] = str(value) + strError

if __name__ == "__main__":
    while 1:
        for index in range(0,5):
            print("Requesting number %s" % index)
            print("Value = %s" % get_status_client(index))
            listClient.append(get_status_client(index))

            if index == 3:
                error_print(get_status_client(index))

            rospy.sleep(1)
        talker()
        
