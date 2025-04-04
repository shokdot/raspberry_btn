import RPi.GPIO as GPIO
import time

LED_PIN = 27
BUTTON_PIN = 17  

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.HIGH);    
        else:
            GPIO.output(LED_PIN. GPIO.LOW);
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nBye")
    GPIO.cleanup()  

