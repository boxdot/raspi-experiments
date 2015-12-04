import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
red = 12
yellow = 10
green = 16
channels = [red, yellow, green]

GPIO.setup(channels, GPIO.OUT)

while True:
  for num in range(8):
    GPIO.output(green, num & 0b001)
    GPIO.output(yellow, num & 0b010)
    GPIO.output(red, num & 0b100)
    sleep(1)
