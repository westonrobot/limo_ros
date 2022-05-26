#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from limo_status_translator.srv import *
from limo_status_translator.msg import *

def callback(req):
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
