import serial 
ser=serial.Serial("COM4",10400)
import binascii
import time

while True:
    data=ser.read(200)
    data=binascii.hexlify(data).decode()
    # print(data)
    c=data.split("720772200002f3")[1][0:16]
    # print(int(c[-4:-2],16)/128.25651)
    print(c)
    # print(int(c[-6:-2],16)/13.142708/1000)

# 154,63917


# ADV=data/2-64
# o2=data[4]/13.142708/1000
# stf=dataB/128.25651      
