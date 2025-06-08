import rospy
from std_msgs.msg import Float64MultiArray

def velocity_publisher():
    # ROS节点初始化
    rospy.init_node('velocity_publisher', anonymous=True)

    # 创建Publisher
    vel_pub = rospy.Publisher('/roller_skating_controller/command', Float64MultiArray, queue_size=10)

    rate = rospy.Rate(10)

    # 零速度指令
    stop_msg = Float64MultiArray()
    stop_msg.data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # 圆周运动指令
    motion_msg = Float64MultiArray()
    motion_msg.data = [0, 0, 0.5, 0, 0, 0.5, 0, 0, 0.5, 0, 0, 0.5]

    try:
        # 先发送停止指令
        for _ in range(10):
            vel_pub.publish(stop_msg)
            rate.sleep()

        # 持续发送运动指令
        while not rospy.is_shutdown():
            vel_pub.publish(motion_msg)
            rospy.loginfo("Publishing circle motion command")
            rate.sleep()

    finally:
        # 退出时发送停止指令
        for _ in range(10):
            vel_pub.publish(stop_msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass