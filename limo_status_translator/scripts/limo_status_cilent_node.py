import sys
import rospy
#from std_msgs.msg import String
from limo_status_translator.srv import GetLimoStatus

def Limo_status_cilent(status_string):
    rospy.wait_for_service('Get_Limo_Status')
    try:
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
#            for x in range(5):
#               print(x)
            Get_Limo_Status = rospy.ServiceProxy('Get_Limo_Status', GetLimoStatus)
            resp1 = Get_Limo_Status(status_string)
            pub = rospy.Publisher('vehicle_state', resp1, queue_size=10)
            pub1 = rospy.Publisher('control_mode', resp1, queue_size=10)
            pub2 = rospy.Publisher('battery_voltage', resp1, queue_size=10)
            pub3 = rospy.Publisher('error_code', resp1, queue_size=10)
            pub4 = rospy.Publisher('motion_mode', resp1, queue_size=10)
            rate.sleep()
            
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    try:
        Limo_status_cilent()
    except rospy.ROSInitException:
        pass
