#Authors : Guillaume Soulier(manage_leds) Benjamin PONTY(transition to class code,reduce_temperature(),reduce_luminosity())

import RPi.GPIO as GPIO
from datetime import datetime
import time
import sys
sys.path.insert(1,"/home/pi/SCAMPI/Management") #Utils is in another folder have to give the path
from Utils import Logger
class Led_panel:
    def __init__(self,temperature):#should add the temperature from the aquarium
        self.logger = Logger()
        self.temp = temperature
        self.human_luminosity_control = False
        GPIO.setmode(GPIO.BCM)
        #self.gpio_luminosity_pin = 18  # Pin for the photocell that checks if LEDs are working
        self.gpio_day_led_pin = 17     # Pin for the Day LED transistor
        #self.gpio_emergency_led_pin = 23    # Pin for the Emergency LED transistor
        #GPIO.setup(self.gpio_luminosity_pin, GPIO.IN)  # Input mode for LDR
        GPIO.setup(self.gpio_day_led_pin, GPIO.OUT)     # Output mode for Day LED
        #GPIO.setup(self.gpio_emergency_led_pin, GPIO.OUT)   # Output mode for Emergency LED
        self.current_hour = datetime.now().hour

    def manage_leds(self):

        if 8 <= self.current_hour < 20:  # Between 8am and 8pm
            GPIO.output(self.gpio_day_led_pin, GPIO.HIGH)  # Turn on Day LED

            if GPIO.input(self.gpio_luminosity_pin) == GPIO.LOW and self.temp<26 and self.human_luminosity_control == False:  # If low luminosity
                GPIO.output(self.gpio_emergency_led_pin, GPIO.HIGH)  # Turn on Emergency LED
                self.logger.log_info("power_operations","Emergency LED turn ON, luminosity is too low")
            else:
                GPIO.output(self.gpio_emergency_led_pin, GPIO.LOW) # Turn off Emergency LED
                self.logger.log_info("power_operations"," luminosity is fine")
        else:
            GPIO.output(self.gpio_day_led_pin, GPIO.LOW)   # Turn off Day LED
            GPIO.output(self.gpio_emergency_led_pin, GPIO.LOW) # Turn off Emergency LED
    def reduce_temperature(self,temperature):
        while temperature>26.1: # 0.1 in more to make sure that the condition for the emergency led isn't met
                try :
                    #lowering luminosity of the led panel by half
                    GPIO.output(self.gpio_day_led_pin, GPIO.HIGH)
                    time.sleep(0.005)
                    GPIO.output(self.gpio_day_led_pin, GPIO.LOW)
                    time.sleep(0.005)
                except KeyboardInterrupt:
                    temperature = 25
                    GPIO.cleanup()
    def reduce_luminosity(self,percentage=100,duration=120):
            self.time = time.time()
            self.human_luminosity_control = True
            # reduce the luminosity by the % wanted
            while time.time()<self.time+duration:
                try :
                    GPIO.output(self.gpio_day_led_pin, GPIO.HIGH)
                    time.sleep(0.005*percentage/200)
                    GPIO.output(self.gpio_day_led_pin, GPIO.LOW)
                    time.sleep(0.005*(1-percentage/100)/2)
                except KeyboardInterrupt:
                    GPIO.cleanup()
                    break
            
                            
            
        #GPIO.cleanup() have to cleanup led if during the shutdown sequence
if __name__ == "__main__":
    test = Led_panel(15)
    test.reduce_luminosity(100, 5)
    print("80%")
    test.reduce_luminosity(80, 5)
    print("60%")
    test.reduce_luminosity(60, 5)
    print("40%")
    test.reduce_luminosity(40, 5)
    print("20%")
    test.reduce_luminosity(20, 5)

            
            
            
            
            
            
            
            
            
        
    
