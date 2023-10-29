# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 23:40:05 2023

@author: 1
"""
def displayMenu():
    print("1.Add Matrices \n" + "2.Check Rotation \n" + "3.Invert Dictionary \n" + "4.Convert Matrix to Dictionary \n" + "5.Check Palindrome \n" + "6.Search for an Element and Merge sort \n" + "7.Exit")
def main():
    user_name = input("please enter your name: ")
    print("Welcome", user_name)
    choice = 0
    #enter the code while user does not want to exit
    while choice !=7 :
        displayMenu()
        choice = eval(input("Enter your choice: "))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        else:
            print("Please enter a valid option")
    
main()
        
