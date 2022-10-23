#----------------------------------------
#Engineer: Michael Granberry
#Project: ARCS Smart Pallet
#Device: Ultrasonic Sensor
#Model: I2C MaxSonar EZ Series - MB1212
#Program: ROS Subscriber Node, Sonar Array
#Last Modified Date: Oct 23, 2022
#----------------------------------------

#Currently Not Wokring

#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class SonarArray:
	def __init__(self):
		self.sonar0x70_range = None
		self.sonar0x72_range = None
		self.sonar0x74_range = None
	
	def getSonarArray(self):
		self.sonarRangeList = [self.sonar0x70_range, 
				  self.sonar0x72_range, 
				  self.sonar0x74_range]
		print(self.sosnarRangeList)

	def sonar_callback_0x70(self, message):
		sonar0x70_range = message.date
		print_rospy_loginfo(0x70, message.data)

	def sonar_callback_0x72(self, message):
		sonar0x72_range = message.date
		print_rospy_loginfo(0x72, message.data)

	def sonar_callback_0x74(self, message):
		sonar0x74_range = message.date
		print_rospy_loginfo(0x74, message.data)
	
	# Print rospy.loginfo hepler function
	def print_rospy_loginfo(self, address, data):
		rospy.loginfo("sonar" + str(address) + ": " + str(data))

	def listener(self):
		rospy.Subscriber("sonar0x70_range_topic", Int32, self.sonar_callback_0x70)
		rospy.Subscriber("sonar0x72_range_topic", Int32, self.sonar_callback_0x72)
		rospy.Subscriber("sonar0x74_range_topic", Int32, self.sonar_callback_0x74)
		rospy.spin()


if __name__ == '__main__':
	rospy.init_node('sonar_listener', anonymous=True)
	s = SonarArray()
	s.listener()
	s.getSonarArray()
