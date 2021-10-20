#include <SHT1x.h>
#include <dht.h>


#define dht_apin A0 // Analog Pin sensor is connected to

// Specify data and clock connections and instantiate SHT1x object
#define dataPin  10
#define clockPin 11 
SHT1x sht1x(dataPin, clockPin);

 
dht DHT;
 
void setup(){
 
  Serial.begin(9600);
  delay(500);//Delay to let system boot
  Serial.println("DHT11 Humidity & temperature Sensor\n\n");
  delay(1000);//Wait before accessing Sensor

//SHT

  Serial.begin(115200); // Open serial connection to report values to host
   Serial.println("Starting up");
   Serial.begin(9600);
  delay(500);//Delay to let system boot

 
}//end "setup()"
 
void loop(){
  //Start of Program 
 
    DHT.read11(dht_apin);
    
    Serial.print("Current humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(DHT.temperature); 
    Serial.println("C  ");
    
    delay(5000);//Wait 5 seconds before accessing sensor again.
 
  //Fastest should be once every two seconds.
 

///sht

  float temp_c;
  float temp_f;
  float humidity;
  

  // Read values from the sensor
  temp_c = sht1x.readTemperatureC();
  temp_f = sht1x.readTemperatureF();
  humidity = sht1x.readHumidity();

  // Print the values to the serial port
  Serial.print("Temperature: ");
  Serial.print(temp_c, DEC);
  Serial.print("C / ");
  Serial.print(temp_f, DEC);
  Serial.print("F. Humidity: ");
  Serial.print(humidity);
  Serial.println("%");

  delay(2000);
  







}// end loop(
