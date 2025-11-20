class Sensor:
    def __init__(self,id):
        self.id = id
    
    def read(self):
        print("Reading sensor " + self.id)
        return 1 #Dummy data till we get to work on real hardware