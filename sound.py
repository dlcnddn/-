import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

scale = [70, 78, 88, 93, 105, 117, 131, 140]
p = GPIO.PWM(BUZZER, 261)
p.start(50)

try :
	for a in scale :
		p.ChangeFrequency(a)
		time.sleep(1.0)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()

