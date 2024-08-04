#Author : Guillaume SOULIER, will not use this main program
#Used certain part for the new main program
import os
import time
from datetime import datetime
import camera
import temperature
import readT_P
import led_panel

led_panel.manage_leds() # control the leds

while True:
    date = datetime.today().strftime('%d-%m-%Y')
    os.mkdir(date)
    os.mkdir("./{}/camera".format(date))

    #camera

    camera.set_up()
    path = "./{}/camera/{}".format(date, datetime.today())
    # Take a photo twice a day
    current_hour = datetime.now().hour
    if current_hour == 8 or current_hour == 20:
        camera.capture_photo(path)

    # Create a video every 5 days
    if int(datetime.now().strftime('%d')) % 5 == 0:
        camera.capture_video(path)

    time.sleep(3600)  # Wait for 1 hour
    text_name = datetime.today()
    with open('./{}/{}.txt'.format(date, text_name), 'w') as f:
        f.write(date)
        f.write('\n')
        if readT_P.readProbe(17)[1] < 500: #on lit la pression sur le pin 17
            a = readT_P.readProbe(17)[1]
            if a < 500:
                f.write("WARNING : pressure is lower than 0.5 Bar")
        if readT_P.readProbe(17)[1] > 2000:
            a = readT_P.readProbe(17)[1]
            if a > 2000:
                f.write("WARNING : pressure is higher than 2 Bar")
        f.write("intern pressure : {} mBar".format(readT_P.readProbe(17)[1]))
        f.write('\n')      
        if readT_P.readProbe(17)[0] < 10: #on lit la temperature sur le pin 17
            a = readT_P.readProbe(17)[0]
            if a < 10:
                f.write("WARNING : temperature is lower than 10°C")
        if readT_P.readProbe(17)[0] > 35:
            a = readT_P.readProbe(17)[0]
            if a > 35:
                f.write("WARNING : temperature is higher than 35°C")
        f.write("intern temperature : {} °C".format(readT_P.readProbe(17)[0]))
        f.write('\n')
        if temperature.get_temperature() > 70:
            a = temperature.get_temperature()
            if a > 70:
                f.write("WARNING : PCB temperature is higher than 70°C")
        f.write("PCB temperature : {} °C".format(temperature.get_temperature())) 
        f.write('\n')





