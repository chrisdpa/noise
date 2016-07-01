import RPi.GPIO as GPIO
import falcon
from wsgiref import simple_server


class RaspOutput():
    def __init__(self, pin=23, default_state=1):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, default_state)

    def set_output(self, state):
        GPIO.output(self.pin, state)


class NoiseThread():

    def __init__(self, light, sound):
        self.api = falcon.API()
        self.api.add_route('/noise/{action}', self)
        self.light = light
        self.sound = sound
        self.httpd = simple_server.make_server('', 80, self.api)
        self.httpd.serve_forever()

    def on_get(self, req, resp, action):
        if action == 'on':
            self.light.set_output(0)
        if action == 'off':
            self.light.set_output(1)
        if action == 'loud':
            self.sound.set_output(0)
        if action == 'silent':
            self.sound.set_output(1)
        resp.status = falcon.HTTP_200


if __name__ == "__main__":
    light = RaspOutput(pin=20)
    sound = RaspOutput(pin=21)
    noise_api = NoiseThread(light, sound)
