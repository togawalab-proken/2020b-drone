import tello
import time
from tello_control_ui import TelloUI


def main():

    drone = tello.Tello('', 8889)  
    vplayer = TelloUI(drone,"./img/")

    vplayer.telloTakeOff()
    time.sleep(8)
    vplayer.takeSnapshot()
    time.sleep(8)
    vplayer.telloLanding()
    
	# start the Tkinter mainloop
    vplayer.root.mainloop() 

if __name__ == "__main__":
    main()
