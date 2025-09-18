from pet import Pet
import os
import time
class Fish(Pet):
    swimming_right_1 = r'''
**************************
*                        *
*    ><(((*>             *
*                        *
**************************
'''
    swimming_right_2 = r'''
**************************
*                        *
*              ><(((*>   *
*                        *
**************************
'''
    swimming_left_1 = r'''
**************************
*                        *
*             <*(((><    *
*                        *
**************************
'''
    swimming_left_2 = r'''
**************************
*                        *
*  <*(((><               *
*                        *
**************************
'''
    dirty_aquarium = r'''
**************************
*        too dirty       *
*        in here!        *
*><(((x>                 *
**************************
'''
    hungry_fish = r'''
**************************
*        too dirty       *
*        in here!        *
*><(((x>                 *
**************************
'''
    hugry_dirty = r'''
**************************
*  too dirty in here!    *
*       I am hungry!     *
*><(((x>                 *
**************************
'''


    def __init__(self, name, hunger = 0, aquarium_dirty = False):
        self.name = name
        self.hunger = hunger
        self.aquarium_dirty = aquarium_dirty #bool

    def clean_up(self):
        if self.aquarium_dirty == True:
            self.aquarium_dirty = False

    def feed(self):
        return super().feed()
    
    def get_hungry(self):
        return super().get_hungry()
    
    def get_dirty(self):
        self.aquarium_dirty = True


    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_animation(self):
        
        if self.hunger < 7 and self.aquarium_dirty == False: 
            while True:
                Fish.clear_screen()
                print(self.swimming_right_1)
                time.sleep(1)
                Fish.clear_screen()
                print(self.swimming_right_2)
                time.sleep(1)
                Fish.clear_screen()
                print(self.swimming_left_1)
                time.sleep(1)
                Fish.clear_screen()
                print(self.swimming_left_2)
                time.sleep(1)
        elif self.hunger >= 7 and self.aquarium_dirty == True:
            time.sleep(1)
            print(self.hugry_dirty)
        elif self.hunger >= 7 and self.aquarium_dirty == False:
            time.sleep(1)
            print(self.hungry_fish)
        elif self.hunger < 7 and self.aquarium_dirty == True:
            time.sleep(1)
            print(self.dirty_aquarium)

dzuk = Fish("Dzknik")
def loop():
    while True:
        dzuk.display_animation()

loop()