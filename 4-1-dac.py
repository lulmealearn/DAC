import RPi.GPIO as GPIO

dac = [8,11 , 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def binary(n):
    str_bin_list = list(bin(n))[2:]
    int_bin_list = [0 for i in range(0,8)]
    for i in str_bin_list:
        int_bin_list.append(int(i))
        result_list = int_bin_list[len(int_bin_list) - 8:len(int_bin_list)]
    return result_list

try:
    while True:
        number = input()
        if number == "q":
            break
        if number.isdigit():
            if int(number) >= 0 and int(number) <= 255:
                GPIO.output(dac, binary(int(number)))
            
            else:
                print("не 8 разрядное число")
                number = 0
            print(int(number)/(3.3*255))             
        else:
            print("не целое число")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()


