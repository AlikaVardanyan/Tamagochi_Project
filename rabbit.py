from pet import Pet
import os
import time

class Rabbit(Pet):

    happy = r"""
       (\_/)
      ( ^.^ ) 
      (  -  ) 
       (   )  
    """

    sad = r"""
       (v_v)  
      ( T.T ) 
      (  -  ) 
       (   )  
    """

    sleeping = r"""
       (\_/)   z Z Z
      ( -.- ) 
      (  -  ) 
       (   )  
    """

    def __init__(self, name, hunger = 0, happiness = 10, energy = 10):
        super().__init__(name, hunger, happiness, energy)

    def feed(self):
        return super().feed()

    def play(self):
        return super().play()

    def sleep(self):
        return super().sleep()

    def status(self):
        return super().status()
    
    def get_hungry(self):
        return super().get_hungry()
    
    def get_sad(self):
        return super().get_sad()
    
    def get_tired(self):
        return super().get_tired()
    
    # --- like Fish ---
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_animation(self):
        if self.happiness > 5 and self.energy > 3:
            while True:
                Rabbit.clear_screen()
                print(self.happy)
                time.sleep(1)
        elif self.happiness <= 5:
            Rabbit.clear_screen()
            print(self.sad)
        else:
            Rabbit.clear_screen()
            print(self.sleeping)


# Example usage
bunny = Rabbit("Fluffy")

def loop():
    while True:
        bunny.display_animation()

loop()