scoreTeam1 = 0
scoreTeam2 = 0
scoreTeam1.Increase
class Score:
    val = 0
    def Increase():
        val++
        if val > 4:
            val=0
    def setBack():
        val=0
        