/*************************************************** 
  This is a library example for the MLX90614 Temp Sensor
  Designed specifically to work with the MLX90614 sensors in the
  adafruit shop
  ----> https://www.adafruit.com/products/1748
  ----> https://www.adafruit.com/products/1749
  These sensors use I2C to communicate, 2 pins are required to  
  interface
  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!
  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx1 = Adafruit_MLX90614(0x5A); //0x55 is adress device 1
Adafruit_MLX90614 mlx2 = Adafruit_MLX90614(0x2B); //0x58 is adress device 2
void setup() {
  Serial.begin(9600);

  Serial.println("Adafruit MLX90614 test");  

  mlx1.begin();
  mlx2.begin(); 
   
}

void loop() {
  Serial.print("Ambient = "); Serial.print(mlx1.readAmbientTempC()); 
  Serial.print("*C\tObject = "); Serial.print(mlx1.readObjectTempC()); Serial.println("*C");
  Serial.print("Ambient = "); Serial.print(mlx1.readAmbientTempF()); 
  Serial.print("*F\tObject = "); Serial.print(mlx1.readObjectTempF()); Serial.println("*F");
  Serial.print("Ambient = "); Serial.print(mlx2.readAmbientTempC()); 
  Serial.print("*C\tObject = "); Serial.print(mlx2.readObjectTempC()); Serial.println("*C");
  Serial.print("Ambient = "); Serial.print(mlx2.readAmbientTempF()); 
  Serial.print("*F\tObject = "); Serial.print(mlx2.readObjectTempF()); Serial.println("*F");


  Serial.println();
  delay(500);
}
