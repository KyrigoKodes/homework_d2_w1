#Lesson 2: Assignments: Nested If


#1. Nested Decisions: The Adventure Game 🏰
#Objective:
#To practice the use of nested if statements in creating a simple text-based adventure game.
#Task 1: Code Correction
#You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.
#Buggy Code:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    elif place == "cave":
        print("You find a hidden treasure!")

#Task 2: Setting the Scene
#Based on the corrected code from Task 1, expand the game. 
#If the user chooses "cave", ask them if they want to "light a torch" 
#or "proceed in the dark", and provide outcomes for each decision.
if place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You see a shiny object!")
    elif action == "proceed in the dark":
        print("You stumble and fall!")
    else:
        pass
#Task 3: Default Path
#If the user makes an invalid choice at any point, use the pass statement for now. 
#Later, you can enhance this to provide feedback or a different branch of the story.

#---------------------------Next Task-----------------------------------
#2. Quick Decisions: The Event Planner 🎉
#Objective:
#To practice the use of shorthand if statements in determining event-related decisions.
#Task 1: Code Correction
#You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

#Buggy Code:
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
#Task 2: Venue Selection
#Based on the corrected code from Task 1, further enhance the program to recommend additional facilities 
#like "audio system" or "projector" based on the number of attendees.
if attendees > 100:
    print("You may need an audio system.")
else:
    print("You may need a projector.")
#Task 3: Catering Choices
#Ask the user if they want "vegetarian" food. 
#Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
food = input("Do you want vegetarian food? (yes/no) ")
if food == "yes":
    print("We recommend Veggie Delight Caterers.")
else:
    print("We recommend Gourmet Meals Caterers.")