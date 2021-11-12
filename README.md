# Sonar

### MaxSonar.py Class Diagram
```
MaxSonar.Ultrasonic
- DEVICE_ADDR  **# Sensor I2C address
- RANGE_COMMAND # Range command byte
- INITIATE_READ # Initiate a read at the sensor address
- I2CBUS # I2C Bus 

+ Ultrasonic(DEVICE_ADDR, RANGE_COMMAND, INITIATE_READ, I2CBUS) # Class Constructor
+ start_sensor(): boolean # Initiate a write at sensor address and writes a range command
+ read_sensor(): int # Reports the last range value
+ take_range_reading(): int # Does start_sensor() and read_sensor() in one funcstion. Used with read_the_senor_example_default.py 
```

### read_the_senor_example_default.py
* Reads a range reading from default I2C bus and device address.

### read_the_senor_example_custom.py
* Reads a range reading from a user defined I2C bus and device address.
