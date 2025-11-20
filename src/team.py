from mirror import Mirror
from sensor import Sensor

class Team:
    def __init__(self, side):
        self.side = side
        if self.side == "left": # Define adress spaces for neopixel in that mirror. Since we start left, it's 0
            addr_l_beg = 0
            addr_l_end = 59
            self.sens_l = 1
            addr_r_beg = 60
            addr_r_end = 119
            self.sens_r = 2
        else:
            addr_l_beg = 120
            addr_l_end = 179
            self.sens_l = 3
            addr_r_beg = 180
            addr_r_end = 239
            self.sens_r = 4

        self.mirror_left = Mirror("game_intermediate", addr_l_beg, addr_l_end)
        self.mirror_right = Mirror("game_intermediate", addr_r_beg, addr_r_end)

    def start_setup(self):
        sens_obj_l = Sensor(self.sens_l)
        sens_obj_r = Sensor(self.sens_r)
        self.mirror_left.set_state("game_instructor", 50, sens_obj_l)
        self.mirror_right.set_state("game_intructor", 50, sens_obj_r)
