import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def state(pin=17):
    return bool(GPIO.input(pin))

def on(pin=17):
    GPIO.output(pin, 1)
    return True

def off(pin=17):
    GPIO.output(pin, 0)
    return False

def toggle(pin=17):
  if state(pin) is True:
    return off(pin)
  else:
    return on(pin)