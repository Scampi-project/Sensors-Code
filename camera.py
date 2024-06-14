from picamera import PiCamera
from time import sleep

camera = PiCamera()
brightness_index = 50

# Ignition
def set_up() :

    camera = PiCamera()
    print('camera detected')

    camera.exposure_mode = 'auto' #exposure
    print('exposure mode set to auto')

    camera.awb_mode = 'auto' #color/white balance
    print('white balance set to auto')

    camera.image_effect = 'none' #image effect
    print('image effect set to normal')

    camera.resolution = (2592, 1944)
    camera.framerate = 15
    print('camera resolution set to high')

    print('camera testing')
    camera.start_preview()
    print('camera on')
    global brightness_index
    brightness_index = 50
    camera.brightness = bightness_index
    print('camera brigthness set to default')
    sleep(5)
    camera.stop_preview()
    print('camera off')



# Standard Functions

def rotate() :
    camera.rotation = 180
    print('camera rotated')

def transparency() :
    camera.start_preview(alpha=200)
    print('picture transparency set to 200')

def capture_photo(path) :
    camera.start_preview() #camera turn on
    print('camera on')
    print('camera focusing')
    sleep(5) #focus time
    camera.capture(path) #create a file indexed by the measurement name (ex file name : Photo31-01-2024-14:52)
    camera.stop_preview() #camera turn off
    print('camera off')
    print(path)

def capture_video(path) :
    camera.start_preview()
    print('camera on')
    camera.start_recording(path)
    print('camera recording')
    sleep(30) #video de 30 secondes
    camera.stop_recording()
    print('stop recording')
    camera.stop_preview()
    print('camera off')
    print(path)

def contrast_plus() :
    camera.start_preview()
    print('camera on')
    global brightness_index
    brightness_index = min(100, brightness_index + 10)
    camera.brightness = brightness_index
    print('brightness up')
    sleep(0.1)
    camera.stop_preview()
    print('camera off')

def contrast_min() :
    camera.start_preview()
    print('camera on')
    global brightness_index
    brightness_index = min(100, brightness_index - 10)
    camera.brightness = brightness_index
    print('brightness down')
    sleep(0.1)
    camera.stop_preview()
    print('camera off')