# BU_TEMPERATURE_SENSOR_AND_I2C
This is a repository that aims interfacing multiple temperature sensors through an I2C protocol
<h1>Setting</h1>
First_module
==============
**<주요기능>**
=============
> 아두이노를 통해서 데이터를 받고, tkinter를 사용하여 사용자 UI를 생성,
카메라 영상과 센서 데이터 값을 확인할 수 있으며, 수집된 데이터를 마리아DB에 저장한다.

**<설치 필요 모듈>**
==================

    pip3 install serial  
    pip3 install opencv-python  
    pip3 install pymysql  

마리아DB 설치 [https://goddaehee.tistory.com/201]  


**<DHT_PIR.ino>** 
==============
> 아두이노에 업로드 후 사용. DHT 센서와 PIR 센서의 원하는 핀 위치가 다르다면,   
DHTPIN의 값과 PIR의 값을 수정 후 사용해주면 된다.  
바로 사용하고자 한다면, DHT는 7번핀,
PIR은 8번 핀에 연결 후 아두이노에 업로드해준다.  

**<main__py>**
===============
>#Arduino  
port : 아두이노의 포트 값 입력  
b_rate : 보드레이트 수치 입력  
#MariaDB  
my_host : MariaDB 서버의 ip address 입력  
my_user : 서버의 user 이름 입력  
my_passwd = 서버의 password 입력  
my_db : 데이터 입력을 하고자하는 데이터베이스의 이름 입력  
my_port : 서버의 port 값 입력  
└──> 입력하고자 하는 데이터의 개수와 이름이 달라진다면 record_data.py에서 수정  
#other module에 추가된 모듈들의 객체를 생성 후 각 객체들의 함수를 실행한다.   
데이터를 끊임없이 수신하고 UI에 표시하기 위해 thread를 이용하여 데이터 값을
지속적으로 받아준다.

**<receive_data.py>**  
================
> read_data() 실행시 seri를 통해서 아두이노로부터 데이터를 받을 준비를 한다. 이후 
while문을 통해서 아두이노로부터 데이터 값을 읽어오고, 읽어온 데이터 값을 원하는
정보 값으로 처리한다.

**<create_UI.py>** 
================
> creaet_UI 객체가 생성되면, tkinter를 사용하여 데이터 값 확인이 가능한 UI를
생성한다. 객체 생성 후 UI에 위젯 배치 후 video_play() 함수를 실행하여 UI에 카메라
영상을 띄운다. 센서 데이터는 main()의 receive_obj객체를 set_data()의 매개변수로 받아
데이터를 갱신한다.

**<record_data.py>**  
================
> 객체 생성시 마리아DB 연결에 필요한 호스트명, 사용자명, 암호, 포트 정보를 받아서
Maria객체를 생성한다. record_data()에서 main()의 receive_obj객체를 매개변수로 받는다. 
이후 sensor객체의 온습도, PIR 정보를 가져온 후 DB에 데이터 입력시간과 데이터 값을 저장한다.

**<xml파일>**
================
> opencv를 사용하여 사람을 인식하기 위해 학습된 파일.


**<사용법>**  
=======================
특별한 설정없이 바로 실행하기 위해서는 
1. 아두이노의 7번핀에 DHT 센서, 8번핀에 PIR 센서를 연결한다.
2. DHT_PIR.ino를 아두이노에 업로드한다.
3. main__.py에서 port에는 아두이노 포트 위치를 넣는다.  
3번까지 진행했을 경우, 코드에서 수정할 부분은 더 이상 없다.  
이후로는 MariaDB 설정이다.  
-----------------------
1. MariaDB의 설정을 특별한 변경없이 default값으로 생성한다. 비밀번호는 'xorms10'으로 한다.  
2. Maria_DB에 'raspi_db' 데이터 베이스를 생성하고, 'usertable' 테이블을 생성한다.
3. char형으로 date, temp, humi, wave 순서대로 데이터 타입을 지정해준다.  
  
명령 프롬프트에서 main__.py가 있는 폴더로 이동 후 python main__.py를 입력해주면 실행이 가능하다.

