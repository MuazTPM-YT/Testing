import pyfirmata
from pyfirmata import Arduino, util
import time

board = pyfirmata.Arduino('COM3')
print("Communication Started!")

iterator = util.Iterator(board)
iterator.start()

LED = board.digital[9]
LED.mode = pyfirmata.PWM

pwm_counter = 0.01
increase_pwm = True
while True:
    if increase_pwm:
        pwm_counter += 0.01
        if pwm_counter >= 1:
            increase_pwm = False
    else:
        pwm_counter -= 0.01
        if pwm_counter <= 0:
            increase_pwm = True
    LED.write(pwm_counter)
    time.sleep(0.01)