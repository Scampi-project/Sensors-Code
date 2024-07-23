import RPi.GPIO as GPIO
from datetime import datetime
import time
class Led_panel:
    def __init__(self):
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

            if GPIO.input(self.gpio_luminosity_pin) == GPIO.LOW:  # If low luminosity
                GPIO.output(self.gpio_emergency_led_pin, GPIO.HIGH)  # Turn on Emergency LED
            else:
                GPIO.output(self.gpio_emergency_led_pin, GPIO.LOW) # Turn off Emergency LED

        else:
            GPIO.output(self.gpio_day_led_pin, GPIO.LOW)   # Turn off Day LED
            GPIO.output(self.gpio_emergency_led_pin, GPIO.LOW) # Turn off Emergency LED
    def led_temperature_control(self,temperature, percentage=None,duration=120):
        if percentage == None: #if the temperature is too high, so not a request from the user 
            while temperature>26: 
                    try :
                        #lowering luminosity of the led panel by half
                        GPIO.output(self.gpio_day_led_pin, GPIO.HIGH)
                        time.sleep(0.005)
                        GPIO.output(self.gpio_day_led_pin, GPIO.LOW)
                        time.sleep(0.005)
                    except KeyboardInterrupt:
                        temperature = 25
                        GPIO.cleanup()
        else:
            self.time = time.time()
            # reduce the luminosity with the % wanted
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
    test = Led_panel()
    test.led_temperature_control(15, 100, 5)
    print("80%")
    test.led_temperature_control(15, 80, 5)
    print("60%")
    test.led_temperature_control(15, 60, 5)
    print("40%")
    test.led_temperature_control(15, 40, 5)
    print("20%")
    test.led_temperature_control(15, 20, 5)
