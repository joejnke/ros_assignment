#!/usr/bin/env python
import rospy
import thread
from geometry_msgs.msg import Twist
from Tkinter import *


def usr_move():

    rospy.init_node('user_driven', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    vel_msg.linear.x= 0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    def publisher(vel):
        while (True):
            velocity_publisher.publish(vel)

    def stop_button():
        vel_msg.angular.z = 0
        vel_msg.linear.x= 0
    def fwd_button():
        keep_moving = True
        vel_msg.angular.z = 0
        vel_msg.linear.x= 0.5

    def bwd_button():
        keep_moving = True
        vel_msg.angular.z = 0
        vel_msg.linear.x= -0.5

    def turnL_button():
        keep_moving = True
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0.8

    def turnR_button():
        keep_moving = True
        vel_msg.linear.x = 0
        vel_msg.angular.z = -0.8



    #start the gui
    myGui = Tk()
    myGui.title("JOYSTICK")
    myGui.geometry("115x115")

    #immages for the addButtons
    stop_img = PhotoImage(file = "/home/kira/Downloads/stop.png")
    stop_img = stop_img.subsample(4)

    fwd_img = PhotoImage(file = "/home/kira/Downloads/forward.png")
    fwd_img = fwd_img.subsample(4)

    bwd_img = PhotoImage(file = "/home/kira/Downloads/backward.png")
    bwd_img = bwd_img.subsample(4)

    tl_img = PhotoImage(file = "/home/kira/Downloads/turnleft.png")
    tl_img = tl_img.subsample(4)

    tr_img = PhotoImage(file = "/home/kira/Downloads/turnright.png")
    tr_img = tr_img.subsample(4)
    #Control buttons
    FWD = Button(myGui, image = fwd_img, width=32, command=fwd_button).grid(row=1, column=2, sticky=W)
    BWD = Button(myGui, image = bwd_img, width=32, command=bwd_button).grid(row=1, column=0, sticky=W)
    STOP = Button(myGui, image = stop_img, width=32, command=stop_button).grid(row=1, column=1, sticky=W)
    TURNL = Button(myGui, image = tl_img, width=32, command=turnL_button).grid(row=0, column=1, sticky=W)
    TURNR = Button(myGui, image = tr_img, width=32, command=turnR_button).grid(row=2, column=1, sticky=W)
    #start tread that will publish vel_msg in baground and prevent the
    #gui from freezing
    thread.start_new(publisher, (vel_msg,))

    myGui.mainloop()

if __name__ == '__main__':
    try:
        usr_move()
    except rospy.ROSInterruptException:
        pass
