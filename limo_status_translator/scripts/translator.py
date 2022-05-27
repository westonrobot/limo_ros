#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from limo_status_translator.srv import *
from limo_status_translator.msg import *

def callback(req):
    if req.get_status == 0:
        if req.vehicle_state == 0x00:
            veh_state_str = "System normal"
        else:
            veh_state_str = "System exception"
    else if req.get_status == 1:
        if req.vehicle_state == 0x00:
            ctrl_src_str = "Standby"
        else if req.vehicle_state == 0x01:
            ctrl_src_str = "Command Control"
        else if req.vehicle_state == 0x02:
            ctrl_src_str = "App Control"
        else if req.vehicle_state == 0x03:
            ctrl_src_str = "Remote Control"
    else if req.get_status == 2:
            batt_vol_str = str(req.battery_voltage)
    else if req.get_status == 3:
            #bit 0 and bit 1 will not be accessed cuz it's 0b
            #access the bits from [2] onwards to [11]
            error_code = bin(req.error_code)
            if(error_code[2] == 1):
                error_code_str = "Battery undervoltage fault"
            else if(error_code[3] == 1):
                error_code_str = "Battery undervoltage warning"
            else if(error_code[4] == 1):
                error_code_str = "Remote control connection loss"
            else if(error_code[5] == 1):
                error_code_str = "(Motor No. 1) Steering motor driver communication failure"
            else if(error_code[6] == 1):
                error_code_str = "(Motor No. 2) Steering motor driver communication failure"
            else if(error_code[7] == 1):
                error_code_str = "(Motor No. 3) Steering motor driver communication failure"
            else if(error_code[8] == 1):
                error_code_str = "(Motor No. 4) Steering motor driver communication failure"
            else if(error_code[10] == 1):
                error_code_str = "Driver failure"
            else if(error_code[10] == 1):
                error_code_str = "Upper layer communication status"
    else if req.get_status == 4:
        if req.motion_mode == 0x00:
            motion_str = "4-wheel differential"
        else if req.motion_mode = 0x01:
            motion_str = "Ackerman"
        else if req.motion_mode = 0x02:
            motion_str = "Mecanum"    

    hello_str = "Hi, I am" + str(req.get_status)
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', req.get_status)
    resp = GetLimoStatusResponse()
    resp.status_string = hello_str
    return resp

if __name__ == '__main__':
    rospy.init_node('translator_node')
    rospy.Service('abc', GetLimoStatus, callback)

    rospy.loginfo("Translation ready")
    rospy.spin()

# #!/usr/bin/env python
# import rospy
# from std_msgs.msg import String
# from limo_status_translator.msg import LimoStatus

# # def callback(data):
# #     rospy.loginfo("I heard %s\n", data.data)

# # def get_limo_info():
# #     rospy.init_node('translator', anonymous=True)
# #     rospy.Subscriber('limo_status', LimoStatus, callback)
# #     rospy.spin()

# # if __name__ == '__main__':
# #     get_limo_info()

# # vehicle_state = 8
# # something 
# # pub.publish(something)

# def callback(data):
#     rospy.loginfo(rospy.get_caller_id()+"I heard %s\n", data.data)

# def get_limo_info():
#     rospy.init_node('translator', anonymous=True)
#     rospy.Subscriber('limo_status', LimoStatus, callback)
#     rospy.spin()
# if __name__ == '__main__':
#     get_limo_info()


# def listener():

#     rospy.init_node('listener', anonymous=True)

#     rospy.Subscriber('updatedchat', String, callback)

#     # spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()
