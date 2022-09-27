from sonar import Sonar
from datetime import datetime #Date


def main():
	s0x72 = Sonar(0x70)
	s0x70 = Sonar(0x72)
	s0x70 = Sonar(0x74)
	while True:
		print("---------------------")
		print("0x70: " + str(s0x70.read_range()) + "cm")
		print("0x72: " + str(s0x72.read_range()) + "cm")
		print("0x74: " + str(s0x72.read_range()) + "cm")
		print(datetime.now())
		print("---------------------")

if __name__ == "__main__":
	main()
