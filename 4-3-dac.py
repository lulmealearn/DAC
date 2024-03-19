import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

value = GPIO.PWM(21, 100)

try:
    while True:
        k = int(input())
        value.start(float(k))
        print(3.3 * float(k)/100)

finally:
    GPIO.cleanup()

