import Jetson.GPIO as GPIO
import keyboard
import time

b1 = 18
bu = 19
bd= 20
bl = 21
br = 22
be =23
bes = 24
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bu, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bd, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bl, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(br, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(be, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bes, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(b1) == GPIO.LOW:
            keyboard.press_and_release("space")
            time.sleep(0.2)  
        
        elif GPIO.input(bu) == GPIO.LOW:
            keyboard.press_and_release("up")
            time.sleep(0.2)
        elif GPIO.input(bd) == GPIO.LOW:
            keyboard.press_and_release("down")
            time.sleep(0.2)
        elif GPIO.input(bl) == GPIO.LOW:
            keyboard.press_and_release("left")
            time.sleep(0.2)
        elif GPIO.input(br) == GPIO.LOW:
            keyboard.press_and_release("right")
            time.sleep(0.2)
        elif GPIO.input(be) == GPIO.LOW:
            keyboard.press_and_release("enter")
            time.sleep(0.2)
        elif GPIO.input(bes) == GPIO.LOW:
            keyboard.press_and_release("esc")
            time.sleep(0.2)

        time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()
