import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count1 = 0
count2 = 0
count3 = 0
count4 = 0

lastsw1Value = 0
lastsw2Value = 0
lastsw3Value = 0
lastsw4Value = 0

try:
    while True:
        sw1Value = GPIO.input(SW1)
        sw2Value = GPIO.input(SW2)
        sw3Value = GPIO.input(SW3)
        sw4Value = GPIO.input(SW4)

        if lastsw1Value == 0 and sw1Value == 1:
            count1 += 1
            print("Sw1 has been touched", count1)
            time.sleep(0.02)

        if lastsw2Value == 0 and sw2Value == 1:
            count2 += 1
            print("Sw2 has been touched", count2)
            time.sleep(0.02)

        if lastsw3Value == 0 and sw3Value == 1:
            count3 += 1
            print("Sw3 has been touched", count3)
            time.sleep(0.02)

        if lastsw4Value == 0 and sw4Value == 1:
            count4 += 1
            print("Sw4 has been touched", count4)
            time.sleep(0.02)

        lastsw1Value = sw1Value
        lastsw2Value = sw2Value
        lastsw3Value = sw3Value
        lastsw4Value = sw4Value

        time.sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
