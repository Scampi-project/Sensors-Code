import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BOARD)
gpio_luminosity_pin = 18  # Pin for the photocell that checks if LEDs are working
gpio_day_led_pin = 22      # Pin for the Day LED transistor
gpio_emergency_led_pin = 23    # Pin for the Emergency LED transistor
GPIO.setup(gpio_luminosity_pin, GPIO.IN)  # Input mode for LDR
GPIO.setup(gpio_day_led_pin, GPIO.OUT)     # Output mode for Day LED
GPIO.setup(gpio_emergency_led_pin, GPIO.OUT)   # Output mode for Emergency LED
current_hour = datetime.now().hour

def manage_leds():

    if 8 <= current_hour < 20:  # Between 8am and 8pm
        GPIO.output(gpio_day_led_pin, GPIO.HIGH)  # Turn on Day LED

        if GPIO.input(gpio_luminosity_pin) == GPIO.LOW:  # If low luminosity
            GPIO.output(gpio_emergency_led_pin, GPIO.HIGH)  # Turn on Emergency LED
        else:
            GPIO.output(gpio_emergency_led_pin, GPIO.LOW) # Turn off Emergency LED

    else:
        GPIO.output(gpio_day_led_pin, GPIO.LOW)   # Turn off Day LED
        GPIO.output(gpio_emergency_led_pin, GPIO.LOW) # Turn off Emergency LED