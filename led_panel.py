#Authors : Guillaume Soulier(manage_leds) Benjamin PONTY(transition to class code,reduce_temperature(),reduce_luminosity())

import RPi.GPIO as GPIO
from datetime import datetime
import time
import sys
sys.path.insert(1,"/home/pi/SCAMPI/Management") #Utils is in another folder have to give the path
from Utils import Logger
class Led_panel:
    def __init__(self):#should add the temperature from the aquarium
        self.logger = Logger()
        self.human_luminosity_control = False
        GPIO.setmode(GPIO.BCM)
        self.gpio_luminosity_pin = 11  # Pin for the photocell that checks if LEDs are working
        self.gpio_day_led_pin = 13     # Pin for the Day LED transistor
        self.gpio_day_led_pin_2 = 15
        self.gpio_day_led_pin_3 = 16
        self.gpio_day_led_pin_4 = 18
        self.gpio_emergency_led_pin = 23    # Pin for the Emergency LED transistor
        GPIO.setup(self.gpio_luminosity_pin, GPIO.IN)  # Input mode for LDR
        GPIO.setup(self.gpio_day_led_pin, GPIO.OUT)
        GPIO.setup(self.gpio_day_led_pin_2, GPIO.OUT)
        GPIO.setup(self.gpio_day_led_pin_3, GPIO.OUT)       # Output mode for Day LED
        GPIO.setup(self.gpio_day_led_pin_4, GPIO.OUT) 
        GPIO.setup(self.gpio_emergency_led_pin, GPIO.OUT)   # Output mode for Emergency LED
    def turn_on(self):
        GPIO.output(self.gpio_day_led_pin, GPIO.HIGH)  # Turn on Day LED
        GPIO.output(self.gpio_day_led_pin_2, GPIO.HIGH)
        GPIO.output(self.gpio_day_led_pin_3, GPIO.HIGH)
        GPIO.output(self.gpio_day_led_pin_4, GPIO.HIGH)
    def check_luminosity(self,temp):
    def check_luminosity(self,temp):
        if GPIO.input(self.gpio_luminosity_pin) == GPIO.LOW and temp<26 and self.human_luminosity_control == False:  # If low luminosity have to emmit an alert 
            GPIO.output(self.gpio_emergency_led_pin, GPIO.HIGH)  # Turn on Emergency LED                                    But have to check if can't add a luminosity sensor
            self.logger.log_info("power_operations","Emergency LED turn ON, luminosity is too low")
        else:
            GPIO.output(self.gpio_emergency_led_pin, GPIO.LOW) # Turn off Emergency LED
            self.logger.log_info("power_operations"," luminosity is fine")
            pass
    def turn_off(self):
        GPIO.output(self.gpio_day_led_pin, GPIO.LOW)   # Turn off Day LED
        GPIO.output(self.gpio_emergency_led_pin, GPIO.LOW) # Turn off Emergency LED
    def reduce_temperature(self,temperature):
        while temperature>26.1: # 0.1 in more to make sure that the condition for the emergency led isn't met
                try :           #Have to check if the code is still working or stopping
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
            self.manage_leds()
            
                            
            
        #GPIO.cleanup() have to cleanup led if during the shutdown sequence
if __name__ == "__main__":
    test = Led_panel()
    test.turn_on()
            
            
            
            
            
            
            
            
            
        
    
