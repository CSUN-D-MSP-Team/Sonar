from MaxSonar import Ultrasonic

# Main
if __name__ == '__main__':
    sonar = Ultrasonic() # Default Constructor
    range = 0
    while(1):
        range = sonar.take_range_reading() # Returns int
        print('Range: {} cm'.format(range))
        print('--------------------------')


