#Author : Benjamin PONTY(class version, improvement/updating), Original code : Guillaume Soulier, modified by : Viren OLLIVIER

from time import sleep
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from libcamera import controls
from datetime import datetime
import sys
sys.path.insert(1,"/home/pi1/SCAMPI/Management") # import Utils file that is in another file
from Utils import Logger                     # have to modify the path if you change the organisation
 
# Ignition   
class Camera: 
    def __init__(self) :
        self.camera = Picamera2()
        self.config = self.camera.create_video_configuration()
        self.camera.configure(self.config)
        self.brightness_index = 100
        self.encoder = H264Encoder(10000000)
        self.logger = Logger()
    """   #inutile
    def set_up(self):
        self.logger.log_info("measurement_operations",'camera detected')
        self.camera.exposure_mode = 'auto' #exposure
        self.logger.log_info("measurement_operations",'exposure mode set to auto')
        
        self.camera.awb_mode = 'auto' #color/white balance
        self.logger.log_info("measurement_operations",'white balance set to auto')

        self.camera.image_effect = 'none' #image effect
        self.logger.log_info("measurement_operations",'image effect set to normal')

        self.camera.resolution = (2592, 1944)
        self.camera.framerate = 15
        self.logger.log_info("measurement_operations",'self.camera resolution set to high')

        self.logger.log_info("measurement_operations",'self.camera testing')
        self.camera.start_preview()
        self.logger.log_info("measurement_operations",'self.camera on')
        self.brightness_index = 100
        self.camera.brightness = self.brightness_index
        self.logger.log_info("measurement_operations",'self.camera brigthness set to default')
        #sleep(5)
        self.camera.stop_preview()
        self.logger.log_info("measurement_operations",'self.camera off')

"""

    # Standard Functions

    def rotate(self) :
        self.camera.rotation = 180
        self.logger.log_info("measurement_operations",'self.camera rotated')

    def transparency(self) :
        self.camera.start_preview(alpha=200)
        self.logger.log_info("measurement_operations",'picture transparency set to 200')

    def capture_photo(self) :
        self.camera.start_preview() #camera turn on
        self.logger.log_info("measurement_operations",'camera on')
        self.logger.log_info("measurement_operations",'camera focusing')
        #sleep(5) #focus time
        self.camera.start()
        self.camera.set_controls({"AfMode": controls.AfModeEnum.Continuous})
        sleep(2)
        self.camera.capture_file(f'/home/pi1/SCAMPI/Sensors/photo{datetime.now()}.jpg') #create a file indexed by the measurement name (ex file name : Photo31-01-2024-14:52)
        self.camera.stop_preview() #camera turn off
        self.logger.log_info("measurement_operations",'camera off')

    def capture_video(self,Long=False) :
        self.camera.start_preview()
        self.logger.log_info("measurement_operations",'camera on')
        self.camera.start_recording(self.encoder,f'/home/pi1/SCAMPI/Sensors/video{datetime.now()}.h264')
        self.camera.set_controls({"AfMode": controls.AfModeEnum.Continuous , "AfSpeed" : controls.AfSpeedEnum.Fast})
        self.logger.log_info("measurement_operations",'camera recording')
        if Long:
                sleep(60)#video d'une min
        else:
                sleep(15) #video de 15 secondes
        self.camera.stop_recording()
        self.logger.log_info("measurement_operations",'stop recording')
        self.camera.stop_preview()
        self.logger.log_info("measurement_operations",'camera off')

    def contrast_plus(self) :
        self.camera.start_preview()
        print('camera on')
        self.brightness_index = min(100, self.brightness_index + 10)
        self.camera.brightness = self.brightness_index
        print('brightness up')
        sleep(0.1)
        self.camera.stop_preview()
        print('camera off')

    def contrast_min(self) :
        self.camera.start_preview()
        print('camera on')
        brightness_index = min(100, self.brightness_index - 10)
        self.camera.brightness = self.brightness_index
        self.logger.log_info("measurement_operations",'brightness down')
        sleep(0.1)
        self.camera.stop_preview()
        print('camera off')
if __name__ == '__main__':
    test = Camera()
    test.capture_photo()
    #test.capture_video()
