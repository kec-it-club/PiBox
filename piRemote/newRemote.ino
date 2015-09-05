#include<SoftwareSerial.h>
#include "Wire.h"
#include "I2Cdev.h"
#include "MPU6050.h"
MPU6050 mpu;
/*accelerometer*/ 
int16_t ax, ay, az;
int16_t gx, gy, gz;
int valx;
int valy;
int prevalx;
int prevaly;
/*button module*/
const int btnPin[] = {3,4,5,6,7,8,9,10};
int btnState[8];
char btnValue[] = {'0','1','2','3','4','5','6','7'};
SoftwareSerial btSerial(12,11);

void setup() 
{
    Wire.begin();
    Serial.begin(9600);
    mpu.initialize();
    for(int i=0;i<8;i++) {
	  pinMode(btnPin[i],INPUT);
     }
     btSerial.begin(9600);
}
 
void loop() 
{
  for(int i=0;i<8;i++) {
    btnState[i] = digitalRead(btnPin[i]);
    if(i==7 && btnState[i]) {
      mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
      valx = map(ax, -10000, 10000, 1500, 0);
      valy= map (ay, -10000, 10000, 900,0);
      
      if(valx!=prevalx || valy!=prevaly){
        prevalx=valx;
        prevaly=valy;
        Serial.print(rnd(valx));
        btSerial.print(rnd(valx));
        Serial.print(" ");
        btSerial.print(" ");
        Serial.println(rnd(valy));
        btSerial.println(rnd(valy));
       }
       
    }
    else if (btnState[i]) {
      Serial.println(btnValue[i]);
      btSerial.println(btnValue[i]);
    }
  }
       
  delay(100);
}
 


int rnd(int a){
  int temp;
  temp = a % 10;
  return temp<5?(a-temp):(a+10-temp);
  
}
 
