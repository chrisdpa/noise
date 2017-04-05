#! /usr/bin/python
import RPi.GPIO as GPIO
import requests
import time

print "I am watching your services"

LIGHT = 8
ON = 0
OFF = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT, GPIO.OUT)


def light_on():
    GPIO.output(LIGHT, ON)
    print 'ON'


def light_off():
    GPIO.output(LIGHT, OFF)
    print 'OFF'


hdr = {'User-Agent': 'Mozilla/5.0',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def has_connection():
    failed = 0
    attempts = 0
    while attempts < 4:
        for service in ['rate', 'customer', 'fund', 'template', 'kyc', 'order', 'audit', 'user', 'sms', 'location', 'sanction', 'currency', 'country', 'bank']:
            r = requests.get(
                'https://wire.travelex.co.uk/v1/{}/health'.format(service),
                headers=hdr)
            print "{}: {}".format(service, r.status_code)
            if r.status_code != 200:
                failed += 1
        if failed == 0:
            return True
        time.sleep(10)
        failed = 0
        attempts += 1
    return False


try:
    light_on()
    time.sleep(1)
    light_off()
    while True:
        time.sleep(20)
        if has_connection():
            light_off()
        else:
            light_on()
except Exception as e:
    print "Exception caught: {}".format(e)

finally:
    GPIO.cleanup()

