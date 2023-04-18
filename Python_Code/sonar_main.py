#----------------------------------------
#Engineer: Michael Granberry
#Project: ARCS Smart Pallet
#Device: Ultrasonic Sensor
#Model: I2C MaxSonar EZ Series - MB1212
#Last Modified Date: Oct 23, 2022
#----------------------------------------

from sonar import Sonar
from datetime import datetime #Date


def main():
	s0x70 = Sonar(0x70)
	s0x71 = Sonar(0x71)
	s0x72 = Sonar(0x72)
	while True:
		print("---------------------")
		print("0x70: " + str(s0x70.read_range()) + "cm")
		print("0x71: " + str(s0x71.read_range()) + "cm")
		print("0x72: " + str(s0x72.read_range()) + "cm")
		print(datetime.now())
		print("---------------------")

if __name__ == "__main__":
	main()
