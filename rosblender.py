#!/usr/bin/env python
import rospy
import socket
from geometry_msgs.msg import Twist

s = socket.socket()

host = socket.gethostname()
port = 5001
s.bind((host, port))

s.listen(5)

def start_fractal():
   #Starts a new node
   rospy.init_node('robot_cleaner', anonymous=True)
   velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
   vel_msg = Twist()

   vel_msg.linear.x=0
   vel_msg.linear.y=0
   vel_msg.linear.z=0
   vel_msg.angular.x = 0
   vel_msg.angular.y = 0
   vel_msg.angular.z = 0

   runbr = True
   while runbr:
       c, addr = s.accept()
       print 'Got connection from: ' , addr
       c.send('Thank you for connecting')
       data = str(c.recv(1024).decode())
       velocities = data.split( )
       X = float(velocities[0])/3.0
       Z = float(velocities[1])

       vel_msg.angular.z = Z
       vel_msg.linear.x = X
       velocity_publisher.publish(vel_msg)
       c.close()
   rospy.spin()

if __name__ == '__main__':
   try:
       # Testing our function
       start_fractal()
   except rospy.ROSInterruptException:
       pass
