#!/usr/bin/env python

import sys
import rospy
from ros_demo.srv import *

def say_hi_client(x):
    rospy.wait_for_service('say_hi')
    try:
        say_hi = rospy.ServiceProxy('say_hi', SayHi)
        resp1 = say_hi(x)
        return resp1.answer
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = sys.argv[1]
    else:
        print usage()
        sys.exit(1)
    print "Asking %s"%(x)
    print "Answering %s"%(say_hi_client(x))