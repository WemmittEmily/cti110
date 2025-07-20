#Emily Wemmitt
#7/12/25
#P5HW
#Create a fun video game

import random

def createPlayer1():
    name = "Player 1"
    health_points = 100
    inventory = []

    add_item = input(f"Should {name} have any starting items? (y/n): ")
    #Loop to keep getting items from the user
    while add_item.lower() != "n":
        obj = input("Enter an item to add to inventory: ")
        #Add object to list
        inventory.append(obj)
        add_item = input("Add another item? (y/n):")
    #Loop breaks here
    print(f"You successfully created {name}'s inventory: ")
    print()
    print(inventory)
    #Create the dictionary that represents the character
    character = {"name": name, "inventory": inventory, "health_points": health_points}
    return character

def move_right(character):
     print("You open the door to find...")
     print("🟩A Gelatinous Cube!🟩")

     inventory = character["inventory"]
     
     if "sword" in inventory:
        print("You draw your sword and slay the Gelatinous Cube!")
        print("You make your way through the opening at the other side of the room.")
        print("......")
     elif "axe" in inventory:
         print("You ready your axe and slay the Gelatinous Cube!")
         print("You make your way through the opening at the other side of the room.")
         print("......")
     else:
        character["health_points"] -= 15
        print("You run for the opening across the room, but not before the Gelatinous Cube attacks you. You lose 15 health.")
        print(f"{character["name"]}'s new health is {character["health_points"]}")
        print("You stagger through the opening at the other side of the room.")
        print("......")

def move_left(character):
    print("You enter the room and find only a chest.")
    add_item = (input("Do you open it? (y/n)"))
    if add_item.lower() == "y":
        print("You have found a torch to help light your way.")
        print("🕯🕯🕯🕯🕯🕯🕯🕯🕯🕯🕯")
        character["inventory"].append("torch")
        print("Torch added to your inventory!")
        print("There's nothing left in this room for you, you must go back and turn right.")
        move_right(character)
    else:
        print("You leave the chest and walk out of the room, forcing you to go right.")
        move_right(character)

def torch_explore(character):
    inventory = character["inventory"]
    if "torch" in inventory:
        print("Good thing you found this torch!")
        print("You use the torch to light your way.")
        print("......")
        print("You notice something crawling towards you...")
        print("🕸🕷It's a huge spider!🕷🕸")
        print("......")
        if "sword" in inventory:
            print("You take out the spider with one swing of your sword.")
            print("You continue down the dark tunnel...")
        elif "axe" in inventory:
            print("You take the spider down with one whack of your axe.")
            print("You continue down the dark tunnel...")
        elif "sword" not in inventory:
            print("......")
            print("You have no weapon!")
            print("The spider attacks as you try to run away, you lose 20 health.")
            character["health_points"] -= 20
            print(f"{character["name"]}'s new health is {character["health_points"]}")
            print("You continue down the dark tunnel...")
        elif "axe" not in inventory:
            print("......")
            print("You have no weapon!")
            print("The spider attacks as you try to run away, you lose 20 health.")
            character["health_points"] -= 20
            print(f"{character["name"]}'s new health is {character["health_points"]}")
            print("You continue down the dark tunnel...")
    else:
        print("You hear something running towards you but can't see what it is...")
        print("A huge spider attacks as you try to run away, you lose 20 health.")
        character["health_points"] -= 20
        print(f"{character["name"]}'s new health is {character["health_points"]}")
        print("You continue down the dark tunnel...")

def answer_riddle(character):
    inventory = character["inventory"]
    answer = input("What is the answer?...Hint:You found it in the chest....  ")
    if answer == "torch":
        print("You wave your torch around and notice a crack in the wall that looks like the outline of a door.")
        print("You push on the wall and it shifts...")
        print("......")
        print("The door moves and you see a pile of gold laying on the floor!")
        gold_amount = random.randint(20, 100)
        character["inventory"].append(f"{gold_amount} gold")
        print(f"{gold_amount} gold has been added to your inventory!")
    else:
        print("That's not right, continue through the cavern...")

def fight_ogre(character):
    inventory = character["inventory"]
    answer = input("Will you fight or try to run? (fight/run)")
    if answer == "run":
        print("You try to run but the ogre is too quick and cuts you down with its club!")
        print("GAME OVER")
        print("☠☠☠☠")
        try_again = input("Try again? (y/n)")
        if try_again == "y":
            main()
        elif try_again == "n":
            print("You lie dead on the floor of the dungeon, forever a victim to its monsters...")
    elif answer == "fight":
        print("You stand to fight the ogre...")
        if "sword" in inventory:
            print("You draw your sword and go to battle.")
            print("You take off the head of the ogre, victorious!")
            print("You run for the door, finally free!")
            print("YOU'VE ESCAPED THE DUNGEON, GREAT JOB!")
            main()
        if "axe" in inventory:
            print("You draw your axe and go to battle.")
            print("You stab the ogre in the heart, victorious!")
            print("You run for the door, finally free!")
            print("YOU'VE ESCAPED THE DUNGEON, GREAT JOB!")
            main()
        else:
            print("You have no weapon to fight, the ogre cuts you down with its club!")
            print("GAME OVER")
            print("☠☠☠☠")
            main()

            




    

        

    


def main():
    print()
    print("🔥Welcome to Escape the Dungeon!!🔥")
    print()
    print("Don't forget to pack a weapon, a sword or axe perhaps?.. Or maybe you won't need either...")
    # Call the function to create the character
    character = createPlayer1()
    print("You enter the huge wooden doors and as soon as you step inside, they slam behind you.")
    print("......")
    print("The only way out is to venture through!")
    print("......")
    print("As you walk to the end of the dark hallway, you come across two rooms.")

    direction = input("Which room will you enter, left or right? ")
    print("......") 
    if direction == "left":
         # Call a function
         move_left(character)
    if direction == "right":
         # Call a function
        move_right(character)
    print("......")

    print("As you walk through the opening, you notice it's very dark...")

    torch_explore(character)
    print()
    print("The tunnel leads into a huge dimly lit cavern, you find a note laying on a dusty old box...")
    print("The note reads...")
    print("I have no eyes but I help you see")
    print("Light me up, and dark will flee")
    print("What am I?")

    answer_riddle(character)

    print("You navigate your way through the rest of the cavern and find your way back to the end of the dungeon.")
    print("You're almost out...")
    print("You walk into an old, dusty room and see the door to your escape!")
    print("You run for the door...")
    print("Just then a huge ogre comes out of the shadows and blocks the door!")

    fight_ogre(character)
    



#Call the main
if __name__ == "__main__":
        main()