
#include<DHT.h>
#include <PulseSensorPlayground.h>
#include <Arduino.h> 


//pin defines
#define DHTPIN 13
#define DHTTYPE DHT11
#define PULSE_PIN A0

int Signal=0;

DHT dht(DHTPIN,DHTTYPE);
PulseSensorPlayground pulseSensor;

void setup() 
{
  Serial.begin(9600);
  Serial1.begin(9600);
  //Serial.println("TESTING NOW.....");
  dht.begin();
}

void loop() 
{
  //Reading DHT
  delay(200);
  float h=dht.readHumidity();
  float t=dht.readTemperature();
  //Serial.print("Humidity:");
  Serial.print(h);
  Serial.print("x");
  //Serial.print("Temperature = ");
  Serial.print(t);
  Serial.print("x");
  Signal=analogRead(PULSE_PIN);
  if(Signal>550)
  { 
    
    float BPM = 14*6; 
    Serial.println(BPM);
  }
}
   
