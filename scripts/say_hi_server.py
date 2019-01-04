#!/usr/bin/env python

from ros_demo.srv import *
import rospy

def handle_say_hi(req):
    print "Heard " + req.ask
    return SayHiResponse("I don't know what your say")

def say_hi_server():
    rospy.init_node('say_hi_server')
    s = rospy.Service('say_hi', SayHi, handle_say_hi)
    print "Ready to answer say hi."
    rospy.spin()

if __name__ == "__main__":
    say_hi_server()