# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 09:28:59 2023

@author: 1
"""

# display this menu if user choose choice 1


def displayMenu2():
    print("a. Add Node\n" + "b. Display Nodes\n" +
          "c. Search for & Delete Node\n" + "d. Return to main\n")


def singlyLL():
    choice_2 = 0
    # while loop to check the user choice
    # if your choose 'd' loop will be break and the code go back to the main function
    while choice_2 != 'd':
        displayMenu2()
        choice_2 = input("Peek your choice from the list: ")
        if choice_2 == 'a':
            pass
        elif choice_2 == 'b':
            pass
        elif choice_2 == 'c':
            pass
        elif choice_2 == 'd':
            print("Return back to main Menu")
        else:
            print("Invalid input!!" + "Try again:")


def displayMenu():
    print("\n1. Singly Linked List\n" + "2. Check if Palindrome\n" +
          "3. Priority Queu\n" + "4. Evalute an Inflix Expression\n" + "5. Graph\n" + "6. Exit\n")


def main():
    user_name = input("Please enter your name: ")
    print("\nWelcome to our programme", user_name)
    choice = 0
    while choice != 6:
        displayMenu()
        choice = int(input("Please enter your choice from the list above: "))
        if choice == 1:
            singlyLL()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            print("You are exiting")
        else:
            print("Please enter a valid choice")
    print("You did exit the programme")


main()
