#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32
from barc.msg import Input, ECU
import numpy

def talker():
	
	stepcount = 0
	pub = rospy.Publisher('uOpt', Input, queue_size=10)
	rospy.init_node('PWM_Node_test_test', anonymous=False)

	rate = rospy.Rate(2) # 2hz
	while not rospy.is_shutdown():
		out = Input()
		out.accel = 10
		
		if numpy.mod(stepcount,4) == 0:
			out.delta = 0
			stepcount = stepcount+1
		elif numpy.mod(stepcount,4) == 1:
			out.delta = 4			
			stepcount = stepcount+1
		elif numpy.mod(stepcount,4)== 2:
			out.delta = 0
			stepcount = stepcount+1
		elif numpy.mod(stepcount,4)== 3:
			out.delta = -4
			stepcount = stepcount+1
		disp(numpy.mod(stepcount,4))
		pub.publish(out)
		rate.sleep()

		  
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
