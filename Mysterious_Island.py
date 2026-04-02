
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Mysterious Island.")
print("Your mission is to escape and find the hidden legend.")
choice1 = input('You woke up on an Mysterious Island, '
                'you are tired and exhausted but you know you need to go further,'
                'where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You saw a free path between the Trees,you entering it.'
                    'At the end of the road you come to a lake.'
          ' Type "wait" to wait for a boat. Type "swim" to swim across"\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrived in front of a big Mountain,"
                        "there are three holes with different colours above them. "
                        "red,green and blue "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("You are entering,its dark and cold,What is there?"
                  "NOOOOO The big old Mountain Ogre waits Inside! You Died! ")
        elif choice3 == "green":
            print("You entering,you can feel an weird smell,what is happening?"
                  "You are loosing your consciousness...You died!")
        elif choice3 == "blue":
            print("You entering,you can feel some warm wind,an bright light,"
                  "you walking up some stairs...there it is! "
                  "You found the mysterious Item which everyone was looking for!")
        else:
            print("You chose a door that does not exist, you are Dead")
    else:
        print("Something pulled you under the water! You have noe chance to escape! you died!")

else:
    print ("An venomous Snakes attacks you,you are Dead!")
