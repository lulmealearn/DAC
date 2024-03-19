import RPi.GPIO as GPIO
import time
dac = [8,11 , 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(n):
    n = format(n, 'b')
    return n 

T = float(input())/512

try:
    while True:
        n = 0
        while n <= 255:
            bin_n = dec2bin(n)
            number = [int(i) for i in str(bin_n)]
            for j in range(8 - len(number)):
                number = [0] + number

            GPIO.output(dac, number)
            if n != 255:
                n += 1
                time.sleep(T)

            else:
                while n > 0:
                    bin_n = dec2bin(n)
                    number = [int(i) for i in str(bin_n)]
                    for j in range(8 - len(number)):
                        number = [0] + number

                    GPIO.output(dac, number)
                    n -= 1
                    time.sleep(T)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
