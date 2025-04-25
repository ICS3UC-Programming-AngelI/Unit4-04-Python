# !/usr/bin/env python3
# Created by:Angel
# Created on: April 22,2025
# This program asks the user to guess a random number
# between 1 and 9 and then checks if the number guessed 
# is the right number and also uses a break statement.
import random

def main():
    try:
        # this function uses a break statement
        rand_num = random.randint(1, 9)

        while True:
              # asks the user to guess a number and write it.
              user_number = int(input("Enter the number: "))
              print("")

              if user_number == rand_num: 
                print("Correct guess!")
                break
              else:
                 print("Wrong guess. Try again")
    except:
      print ("Not correct!")

if __name__ == "__main__":
    main()