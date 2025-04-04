import RPi.GPIO as GPIO
import time

LED_PIN = 27
BUTTON_PIN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)  
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

led_state = False 

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            led_state = not led_state  
            
            if led_state:
                GPIO.output(LED_PIN, GPIO.HIGH)  
            else:
                GPIO.output(LED_PIN, GPIO.LOW)  
            time.sleep(0.2)  

except KeyboardInterrupt:
    print("\nBye")
    GPIO.cleanup() 

