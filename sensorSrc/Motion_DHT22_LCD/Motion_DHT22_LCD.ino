/*
 * PIR sensor tester
 */
 
int ledPin = 13;                // choose the pin for the LED
int inputPin = 3;               // choose the input pin (for PIR sensor)
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                    // variable for reading the pin status

//----------------------------------------------
#include <LiquidCrystal_I2C.h>//DFRobot I2C LCD 디스플레이를 위한 LiquidCrystal Arduino 라이브러리
#include <DHT.h> //DHT센서를 위한 라이브러리
#define DHTPIN 2 // 습도센서 Signal 선 연결
#define DHTTYPE DHT22 // 습도센서 종류: DHT22
DHT dht(DHTPIN, DHTTYPE);//DHT라이브러리를 사용하기 위해 필요한 pin번호와 type을 정해준다
 
LiquidCrystal_I2C lcd(0x27,20,4); //클래스 객체 생성하는 함수, (LCD주소: 0x27 또는 0x3F, LCD열의 길이,행의길이)
float hum; // 습도값 저장 변수
float temp; // 온도값 저장 변수

void setup() {
    pinMode(ledPin, OUTPUT);      // declare LED as output
  pinMode(inputPin, INPUT);     // declare sensor as input
 
  Serial.begin(9600);// put your setup code here, to run once:
   //-----------------------------------------------------------
  dht.begin();//Start printting the values in the serial monitor
  delay(2000);
  lcd.init();//lcd초기화
  lcd.backlight();//lcd백라이트 켬
  lcd.setCursor(2,0);//0번째 줄 2번째 셸부터 입력하게 한다.
  delay(5000);
  lcd.clear();//LCD 모든 내용을 지운 후 커서의 위치를 (0,0)으로 옮김

}

void loop() {
   val = digitalRead(inputPin);  // read input value

 // -------------------------------
  hum = dht.readHumidity();//온도값 읽기
  temp= dht.readTemperature();//습도값 읽기
   Serial.print("Movement: ");
  if (val == HIGH) {            // check if the input is HIGH
    //We set it ass low
      // we have just turned on
      Serial.print("Motion!");
      // We only want to print on the output change, not state
      pirState = HIGH;
    
  } else {
     // turn LED OFF
    
      // we have just turned of
      Serial.print("M_ended!");
      // We only want to print on the output change, not state
     
  }// put your main code here, to run repeatedly:
  
  

 
  Serial.print("HUMIDITY: "); // "HUMIDITY:" 출력
  Serial.print(hum,0);// 습도 값 소수점 이하 자리 없음
  Serial.print("  TEMPERATURE: "); //"%"(습도단위) "TEMPERATURE:" 출력
  Serial.print(temp, 1);//온도값은 소수점 이하 1자리까지 표시
  Serial.println(" C"); //"C" 온도 단위 표시
  
  lcd.setCursor(0,0); // LCD Cursor 원점
  lcd.print("TEMP:"); // LCD에 "temp" 표시
  float t = temp; // 온도값을 t에 할당
  lcd.print(t,1); // 온도값 LCD로 출력
  lcd.print(" C"); // 온도 단위 표시
  lcd.setCursor(0,1); //LCD 커서 줄바꿈
  lcd.print("HUMIDITY:"); //LCD 2번째 줄에 "humidity:" 출력
  int h = hum; //습도값 h에 할당
  lcd.print(h); //습도값 LCD에 출력
  lcd.print(" % "); //습도 단위 출력
  
  lcd.setCursor(0,2);
  lcd.print("Movement: ");
  if (val == HIGH) {            // check if the input is HIGH
    //We set it ass low
      // we have just turned on
      lcd.print("Motion!");
      // We only want to print on the output change, not state
      pirState = HIGH;
    
  } else {
     // turn LED OFF
    
      // we have just turned of
      lcd.print("M_ended!");
      // We only want to print on the output change, not state
     
  }// put your main code here, to run repeatedly:
  
  

  
  lcd.println();
  //----- 추가 코드
  
    
  //------
  delay(2500); // 샘플링 간격 2초
  

}
