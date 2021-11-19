#define SCL_PIN 5
#define SCL_PORT PORTD
#define SDA_PIN 4
#define SDA_PORT PORTC
#include <SoftI2CMaster.h>
#include <SoftWire.h>

boolean start_sensor(byte bit8address){
//  Serial.println("B");
  boolean errorlevel = 0;
  bit8address = bit8address & B11111110;
  errorlevel = !i2c_start(bit8address) | errorlevel;
  errorlevel = !i2c_write(81) | errorlevel;
//  Serial.println(errorlevel);
  i2c_stop();
  return errorlevel; 
}

int read_sensor(byte bit8address){
  boolean errorlevel = 0;
  int range = 0;
  byte range_highbyte = 0;
  byte range_lowbyte = 0;
  bit8address = bit8address | B00000001;

  errorlevel = !i2c_start(bit8address) | errorlevel;
  range_highbyte = i2c_read(0); 
  range_lowbyte = i2c_read(1);
//  Serial.println(range_highbyte);
//  Serial.println(range_lowbyte);
  i2c_stop();
  range = (range_highbyte * 256) + range_lowbyte;
  if(errorlevel){
    return 0; 
  }
  else{
    return range;
  } 
}

void read_the_sensor_example(){
  boolean error = 0; 
  int range;
  
  error = start_sensor(224);
//  Serial.println(error);
  if (!error){
    delay(100);
    range = read_sensor(224);
    Serial.print("Range:");Serial.print(range);Serial.println(" cm");
    }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  i2c_init();

}
void loop() {
  // put your main code here, to run repeatedly:
  read_the_sensor_example();

}
