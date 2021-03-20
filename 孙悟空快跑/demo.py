import serial
ser=serial.Serial("COM4",9600)

#



# import time
print(ser)

# from threading import Thread
# def main (name="python"):
#     for i in range(2):
#         print('hello',name)
#         time.sleep(2)
# thread_01=Thread(target=main)
# thread_01.start()
# thread_02=Thread(target=main,args=('MING',))
# thread_02.start()
# import serial
# def recv(serial):
#     while True:
#         data=serial.read_all()
#         if data=='':
#             continue
#         else:
#             break
#         sleep(0.02)
#     return  data
# t=serial.Serial('com4',9600)
# if serial.isOpen():
#     print('串口打开成功\n')
#     f=open('date.txt','w')
# else:
#     print('串口打开失败')
# while True:
#     data=recv(serial)
#     if data!=b'':
#         print("receive:",data)
#         serial.write(data)
