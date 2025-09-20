import time
class Pet:
    def __init__(self, name, hunger = 0, happiness = 10, energy = 10):
        self.name = name
        self.hunger = hunger #0-10 scale
        self.happiness = happiness #0-10 scale
        self.energy = energy #0-10 scale



    def feed(self):
        if self.hunger < 10:
            self.hunger -= 1

        else:
            return "I am not hungry"

    def play(self):
        if self.happiness < 10:
            self.happiness += 1

        else:
            return "I dont want to play"

    def sleep(self):
        if self.energy < 10:
            self.energy += 1

    def status(self):
        return f"{self.name} is \n{self.hunger} / 10 points hungry \n{self.happiness} / 10 points happy \nenergy is {self.energy} / 10 "
    
    def get_hungry(self):
        if self.hunger < 10:
            self.hunger += 1

    def get_sad(self):
        if self.happiness > 0:
            self.happiness -=1
    
    def get_tired(self):
        if self.energy > 0:
            self.energy -= 1

    
    def to_dict(self):
        return
    {
                "name": self.name,
                "hunger": self.hunger,
                "happiness": self.happiness,
                "energy": self.energy,
                "kind": self.__class__.__name__

            }
        

