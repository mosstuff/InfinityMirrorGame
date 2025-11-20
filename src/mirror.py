import asyncio

class Mirror:
    def __init__(self, state, led_begin, led_end):
        self.state = state #allowed states are: idle, game_instructor, 'game_mover' and 'game_intermediate'
        self.led_begin = led_begin
        self.led_end = led_end
        self.is_running = False
        self.i_target_distance = None
        self.i_sensor_obj = None

    def set_state(self, state, i_target_distance = None, i_sensor_obj = None):
        self.state = state
        self.i_target_distance = i_target_distance
        self.i_sensor_obj = i_sensor_obj

    async def refresh_art():
        pass

    async def game_instructor(self):
        if self.i_target_distance and self.i_sensor_obj:
            
            pass #do instructor things

    async def game_mover():
        pass

    async def run_main_loop(self):
        self.is_running = True
        while self.is_running:
            match self.state:
                case "idle":
                    pass
                case "art":
                    await self.refresh_art()
                case "game_instructor":
                    await self.game_instructor()
                case "game_mover":
                    await self.game_mover()
