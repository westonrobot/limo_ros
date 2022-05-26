import sys
import rospy
from std_msgs.msg import String
from limo_status_translator.srv import GetLimoStatus

def Limo_status_cilent():
    rospy.init_node('limo_status_translator_node')
    Get_Limo_Status = rospy.ServiceProxy('Get_Limo_Status', GetLimoStatus)
    
    rate = rospy.Rate(1)
    for val in range(5):
        response = Get_Limo_Status(val)
        if response == 0:
            pub = rospy.Publisher('/limo_ros/vehicle_state', String, queue_size=10)
        elif response == 1:
            pub = rospy.Publisher('/limo_ros/control_mode', String, queue_size=10)
        elif response == 2:
            pub = rospy.Publisher('/limo_ros/battery_voltage', String, queue_size=10)
        elif response == 3:
            pub = rospy.Publisher('/limo_ros/error_code', String, queue_size=10)
        elif response == 4:
            pub = rospy.Publisher('/limo_ros/motion_mode', String, queue_size=10)  
        rate.sleep()

    
    rospy.spin()

if __name__ == "__main__":
    try:
        Limo_status_cilent()
    except rospy.ROSInitException:
        pass
