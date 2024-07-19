from time import sleep
from picamera2 import Picamera2
from datetime import datetime

# Ignition
class Camera: 
    def __init__(self) :
        self.camera = Picamera2()
        self.brightness_index = 50
    def set_up(self) :
        print('camera detected')
    
        self.camera.exposure_mode = 'auto' #exposure
        print('exposure mode set to auto')
        
        self.camera.awb_mode = 'auto' #color/white balance
        print('white balance set to auto')

        self.camera.image_effect = 'none' #image effect
        print('image effect set to normal')

        self.camera.resolution = (2592, 1944)
        self.camera.framerate = 15
        print('self.camera resolution set to high')

        print('self.camera testing')
        self.camera.start_preview()
        print('self.camera on')
        self.brightness_index = 50
        self.camera.brightness = self.brightness_index
        print('self.camera brigthness set to default')
        sleep(5)
        self.camera.stop_preview()
        print('self.camera off')



    # Standard Functions

    def rotate(self) :
        self.camera.rotation = 180
        print('self.camera rotated')

    def transparency(self) :
        self.camera.start_preview(alpha=200)
        print('picture transparency set to 200')

    def capture_photo(self,path) :
        self.camera.start_preview() #camera turn on
        print('camera on')
        print('camera focusing')
        sleep(5) #focus time
        self.camera.start()
        
        self.camera.capture_file(path) #create a file indexed by the measurement name (ex file name : Photo31-01-2024-14:52)
        self.camera.stop_preview() #camera turn off
        print('camera off')
        print(path)

    def capture_video(self,path) :
        self.camera.start_preview()
        print('camera on')
        self.camera.start_recording(path)
        print('camera recording')
        sleep(30) #video de 30 secondes
        self.camera.stop_recording()
        print('stop recording')
        self.camera.stop_preview()
        print('camera off')
        print(path)

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
        print('brightness down')
        sleep(0.1)
        self.camera.stop_preview()
        print('camera off')
if __name__ == '__main__':
    test = Camera()
    test.set_up()
    test.capture_photo(f'/home/pi/SCAMPI/Sensors/photo{datetime.now()}.jpg')
