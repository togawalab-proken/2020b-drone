import tello
from tello_control_ui import TelloUI
import socket
import time
import threading

def worker1(vplayer):
     vplayer.root.mainloop()
drone = tello.Tello('', 8889)
vplayer = TelloUI(drone,"./img/")
th1=threading.Thread(target=worker1,args=(vplayer,))
th1.start()
tello_ip = '192.168.10.1'
tello_port = 8889
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = (tello_ip , tello_port)
socket.sendto('command'.encode('utf-8'),tello_address)
time.sleep(5)
socket.sendto('takeoff'.encode('utf-8'),tello_address)
time.sleep(5)
print('A')
vplayer.takeSnapshot()
time.sleep(5)
socket.sendto('land'.encode('utf-8'),tello_address)