import re
import time
import serial
ser=serial.Serial("COM4",115200,timeout=0.1)
time.sleep(2)
while True:
    data = ser.readline()#读取串口数据
    r = str(data)
    st = re.sub("\D", "", r)[0:2]
    st=st.replace("\n","")
    st=st.replace("\r","")
    if st==" ":
        print("kong")


    # s=st.strip("\n")
    s=int(st)

    print(st)

