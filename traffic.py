import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
red = 12
yellow = 10
green = 16
channels = [red, yellow, green]

GPIO.setup(channels, GPIO.OUT)

while True:
  GPIO.output(channels, False)
  GPIO.output(green, True)
  sleep(3)
  GPIO.output(green, False)
  GPIO.output(yellow, True)
  sleep(1)
  GPIO.output(yellow, False)
  GPIO.output(red, True)
  sleep(3)
  GPIO.output(yellow, True)
  sleep(1)
