from pet import Pet
from cat import Cat
from rabbit import Rabbit
from fish import Fish
from user import User  

def welcome_screen():
    print("HELLO! WELCOME TO PET SIMULATOR!\n")

    choice = input("Do you want to start a new game (1) or continue (2)? ")

    if choice == "2":
        print("Der patrast che.")
        return None 

    elif choice == "1":
        user_name = input("Enter your username: ")

        print("Choose your pet:")
        print("1 → Cat")
        print("2 → Rabbit")
        print("3 → Fish")
        pet_choice = input("Enter number (1-3): ")
        pet_name = input("Enter a name for your pet: ")

        if pet_choice == "1":
            pet = Cat(pet_name)
        elif pet_choice == "2":
            pet = Rabbit(pet_name)
        elif pet_choice == "3":
            pet = Fish(pet_name)
        else:
            pet = Cat(pet_name)

        return User(user_name, pet)

    else:
        print("Invalid choice. Starting default game with Cat.")
        return User("DefaultUser", Cat("Fluffy"))



if __name__ == "__main__":
    user = welcome_screen()
    if user:
        print(f"Welcome {user.name}! You have chosen {user.pet.__class__.__name__} named {user.pet.name}.")