#!/usr/bin/env python


import rospy 
from std_msgs.msg import Float32
from barc.msg import Input, ECU
import numpy

def callback(MPC_data):

	servo= (MPC_data.accel-71.0977)/-0.0461 
 	motor= 1580 
 	pub.publish(1)
 	

def talker():
	sub = rospy.Subscriber('uOpt', Input, callback)
	pub = rospy.Publisher('ecu', ECU, queue_size=10)
	pub2 = rospy.Publisher('wendy', Float32, queue_size=10 )

	rospy.init_node('PWM_Node', anonymous=False)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
  		
  		pub2.publish(1)
		rate.sleep()
  
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

