1 Insatalasi hardware:
-  hubungkan esp8266 ke laptop
-  install CH340 driver
-  buka device manager lihat pada port berapa esp8266 anda berada
-  install visual studio code

2 Install Python 3.7

3 Install firmware micropython ketik pada terminal:

-  buka visual studio code
-  copy lokasi folder yang berisi firmware micropython dan paste ketik cd <lokasi folder> pada terminal visual studio code
-  pip install esptool
-  pip install adafruit-ampy
-  esptool.py --chip esp8266 --port /dev/ttyUSB0 erase_flash
-  esptool.py --port COM10 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190529-v1.11.bin

4 Membuat project:
- buka folder project yg akan kita isi project
- buat file python misalnya led.py
- ketik:
	cd <lokasi folder project>

5 menjalankan progam:
- ketik pada terminal 
	* untuk widows:
		- ampy -p COM10 run led.py
	* untuk linux:

		- export AMPY_PORT=/dev/ttyUSB0
		- ampy run led.py








