#!/usr/bin/env python
"""
THIS PROGRAM CAN BE USED TO CONTRALL A PAINTER ROBOT TO PAINT A GIVEN SURFACE WITH THE DESIRED
FRACTAL IMAGE
"""
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

#########################################################
# THE infinity_drawer FUNCTION DRAWS USING              #
# THE linear.x VALUE AND angular.z VALUE OF THE TWIST   #
# VALUE PASSED AS ARGUMENT. NOTE THAT THE REST VALUES   #
# OF THE PASSED ARGUMENT MUST BE ZERO. FOR ASSURANCE    #
# THE FUNCTION CAN BE MODIFIED TO MAKE THE OTHER VALUES #
# OF THE PASSED ARGUMENT 0.                              #
#########################################################
def infinity_drawer(vel_msgin_inf):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg_inf = Twist()
    vel_msg_inf = vel_msgin_inf
    relative_angle = 2*PI
    done =True
    reverse = True
    angular_speed = vel_msg_inf.angular.z
    current_angle = 0

    while (done):
        t0 = rospy.Time.now().to_sec()
        while(current_angle < relative_angle):
            velocity_publisher.publish(vel_msg_inf)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)
        if reverse :
            vel_msg_inf.angular.z = -vel_msg_inf.angular.z
            reverse = False
        else :
            vel_msg_inf.angular.z = abs(vel_msg_inf.angular.z) + 0.2
            reverse = True
        angular_speed = abs(vel_msg_inf.angular.z)
        current_angle = 0
        if vel_msg_inf.angular.z >= 4.0 :
            done = False


def rotate_quarter(vel_msgin_rot):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg_rot = Twist()
    vel_msg_rot = vel_msgin_rot
    current_angle = 0
    vel_msg_rot.linear.x = 0
    angular_speed = abs(vel_msg_rot.angular.z)
    relan = PI/4.0
    t0 = rospy.Time.now().to_sec()
    while(current_angle < relan):
       velocity_publisher.publish(vel_msg_rot)
       t1 = rospy.Time.now().to_sec()
       current_angle = angular_speed*(t1-t0)
    #vel_msg_rot.angular.z = 0 #to stop turtle rotation after quarter rotation


def start_fractal():
   #Starts a new node
   rospy.init_node('robot_cleaner', anonymous=True)
   velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
   vel_msg = Twist()

   vel_msg.linear.x=3.0
   vel_msg.linear.y=0
   vel_msg.linear.z=0
   vel_msg.angular.x = 0
   vel_msg.angular.y = 0
   vel_msg.angular.z = 1.5

   #draw any number of crossed infinity by increasing the number of values in the list, [1, 2, 3], of the for loop.
   for i in [1, 2, 3, 4]:
       #begin infinity_drawer
       vel_msg.linear.x=3.0
       infinity_drawer(vel_msg)
       #end of infinity drawer
       #rotate turtle by quarter of a circle
       vel_msg.angular.z = 1.5
       rotate_quarter(vel_msg)
       #end of rotation by quarter



#Forcing our robot to stop
   vel_msg.angular.z = 0
   vel_msg.linear.x = 0
   velocity_publisher.publish(vel_msg)
   rospy.spin()

if __name__ == '__main__':
   try:
       # Testing our function
       start_fractal()
   except rospy.ROSInterruptException:
       pass
