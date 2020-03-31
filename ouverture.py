import time
import RPi.GPIO as GPIO

def ouvrir():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    UP = 7
    GPIO.setup(UP, GPIO.OUT)
    GPIO.output(UP, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(UP, GPIO.LOW)
    GPIO.cleanup()

def fermer():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    DOWN = 11
    GPIO.setup(DOWN, GPIO.OUT)
    GPIO.output(DOWN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(DOWN, GPIO.LOW)
    GPIO.cleanup()
