#!/usr/bin/env python3

#Practice on else, if, elif

message = "You received a grade of "
#Adding int to make sure return is an integer (whole number)
score = int(input("What score did you receive?"))

if score > 100:
    print("You can't get higher than 100!!")
elif score > 90:
    print("You got an A! Congrats!")
elif score > 80: 
    print("Pretty good, you got a B.")
