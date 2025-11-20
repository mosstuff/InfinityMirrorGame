from team import Team

class Gamemanager:
    def __init__(self):
        self.team_left = Team("left")
        self.team_right = Team("right")

        self.game_state = "init"

        self.round = 1

        self.score_left = 0
        self.score_right = 0

        self.game_setup()

    def game_setup(self):
        self.game_state = "setup"
        self.team_left.start_setup()
        self.team_right.start_setup() #Make async
        