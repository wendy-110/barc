#!/usr/bin/env python


import rospy 
from std_msgs.msg import Float32
from barc.msg import Input, ECU
import numpy

def callback(uOptdata):
	pub = rospy.Publisher('ecu', ECU, queue_size=10)
	servo= (uOptdata.delta-71.0977)/-0.0461 
 	#motor= 1550 
	motor = 1550
 	out = ECU(motor,servo)
	pub.publish(out)
 	

def talker():
	rospy.init_node('PWM_Node', anonymous=False)	
	sub = rospy.Subscriber('uOpt', Input, callback, queue_size=10)
	
	rospy.spin()
  
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

