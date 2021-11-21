#include <DHT.h>

#define DHTPIN 7
#define PIR 8
#define DHTTYPE DHT11

int value = 0;
bool flag = false;
DHT dht(DHTPIN, DHTTYPE);



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PIR, INPUT);
  dht.begin();
}

void loop() {
  delay(1000);
  value = digitalRead(PIR);
  int h = dht.readHumidity();
  int t = dht.readTemperature();
  
  if(value == HIGH && flag == true){
    flag=false;
  }
  else if (value == HIGH && flag == false){
    flag = true;
  }
  Serial.print(flag);
  Serial.print(h);
  Serial.print(t);
  Serial.print("\n");
}
