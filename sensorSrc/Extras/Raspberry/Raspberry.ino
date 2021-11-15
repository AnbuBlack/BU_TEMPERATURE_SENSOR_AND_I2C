// Modified by John 2015 11 03
// MIT license

#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); // B
  pinMode(12, OUTPUT); // G
  pinMode(11, OUTPUT); // R
  pinMode(3, OUTPUT); // Relay
}
void loop() {
  delay(2000);
  int h = dht.readHumidity();
  int t = dht.readTemperature();
  //Serial.print("Humidity: ");
  if (t >= 24) {  // R
     digitalWrite(11, HIGH); // sets the digital pin 13 on
     delay(1000);            // waits for a second
     digitalWrite(11, LOW);

     digitalWrite(3, HIGH); // sets the digital pin 13 on
     delay(5000);            // waits for a second
     digitalWrite(3, LOW);
     delay(1000); 
     
  } else if (t >= 22) {
     digitalWrite(12, HIGH); // sets the digital pin 13 on
     delay(1000);            // waits for a second
     digitalWrite(12, LOW);

      digitalWrite(3, HIGH); // sets the digital pin 13 on
     delay(1000);            // waits for a second
     digitalWrite(3, LOW);
      delay(1000); 
     
  } else  {
     digitalWrite(13, HIGH); // sets the digital pin 13 on
     delay(1000);            // waits for a second
     digitalWrite(13, LOW);

     digitalWrite(3, HIGH); // sets the digital pin 13 on
     delay(20000);            // waits for a second
     digitalWrite(3, LOW);
     delay(1000); 
  } 
  Serial.println(t);
 // Serial.print(" %\t");
 // Serial.print("Temperature: ");
 // Serial.print(t);
 // Serial.println(" C");
}
