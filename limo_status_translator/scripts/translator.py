#!/usr/bin/env python


from __future__ import print_function
from std_msgs.msg import String
from limo_status_translator.srv import GetLimoStatus
from limo_status_translator.msg import LimoStatus
import rospy
listStatus = list()
listError = list()


def callback(info):
    # rospy.loginfo('\n%d \n%d \n%f \n%d \n%d' % (info.vehicle_state, info.control_mode, info.battery_voltage, info.error_code, info.motion_mode))
    if info.vehicle_state == 2:
        listStatus.append("System Exception")
    elif info.vehicle_state == 0:
        listStatus.append("System Normal")

    if info.control_mode == 0:
        listStatus.append("Standby")
    elif info.control_mode == 1:
        listStatus.append("Command Control")
    elif info.control_mode == 2:
        listStatus.append("App Control")
    elif info.control_mode == 3:
        listStatus.append("Remote Control")

    listStatus.append(str(info.battery_voltage))

    listStatus.append(format(info.error_code, '016b'))

    if info.motion_mode == 0:
        listStatus.append("4-wheel differential")
    elif info.motion_mode == 1:
        listStatus.append("Ackerman")
    elif info.motion_mode == 2:
        listStatus.append("Mecanum")


def print(data):
    rospy.loginfo( "Returning values for %d:" % data.get_status)
    if data.get_status == 0:
        return listStatus[0]
    elif data.get_status == 1:
        return listStatus[1]
    elif data.get_status == 2:
        return listStatus[2]
    elif data.get_status == 3:
        return listStatus[3]
    elif data.get_status == 4:
        return listStatus[4]
    else:
        return "Try again"


def translator_server():
    rospy.init_node('limo_status_translator_node', anonymous=True)
    rospy.Subscriber('limo_status', LimoStatus, callback)
    s = rospy.Service('translator_service', GetLimoStatus, print)
    rospy.spin()

if __name__ == '__main__':
    translator_server()
