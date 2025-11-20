class led_controller:
    def __init__(self):
        self.leds = [] # will be replaced by neopixel lib accordingly

    def set_leds(self, offset, data):
        i = 0
        for led in data:
            self.leds[i + offset] = led