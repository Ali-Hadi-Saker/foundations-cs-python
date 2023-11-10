# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:58:10 2023

@author: 1
"""


def displayMenu():
    print("---------------------------------------")
    print("1. Open Tab \n" + "2. Close Tab \n" + "3. Switch Tab \n" +
          "4. Display All Tabs \n" + "5. Open Nested Tab \n" +
          "6. Clear All Tabs \n" + "7. Save Tabs \n" + "8. Import Tabs \n" +
          "9. Exit")
    print("---------------------------------------")


def openTab():
    # create empty dict
    new_tab = {}
    # set a condition to indicate if we taking new Tab
    add_newTab = True
    # generate number of tabs and used as a key
    tabs_num = 0

    # to check if user still want to add a new Tab
    while add_newTab:
        # create empty list that contain title and URL
        element_list = []
        # incrementing tabs_num by 1 and using it as a key
        key = tabs_num + 1
        # taking elements from user and adding them to a list
        title = input("Enter the title of Tab: ")
        element_list.append(title)
        url = input("Enter the URL of the website: ")
        element_list.append(url)
        # store the list of elements with the in the dict
        new_tab[key] = element_list
        # incrementing number of tabs
        tabs_num += 1
        # check if the user want to add a new tab
        repeat = input("do you want to add a new Tab ??: ")
        # use lower() to make char in lower case
        if repeat.lower() == 'no':
            add_newTab = False
    return new_tab
# create a function to remove a specific tab the have the dictionary of all tabs as parameter


def closeTab(tab):
    index = int(input("Enter the index of tab that you want to close: "))
    # tab.keys() shows the keys list of dict
    # list used to convert dict keys into list for indexing
    key_list = list(tab.keys())
    # key_list[-1] to index for the last element of list
    # last key will be removed if index is equal or bigger then him
    if index >= key_list[-1]:
        del tab[key_list[-1]]
    # enter else when index is smaller than last key
    else:
        # searching for the inex in key list
        for i in range(len(key_list)):
            # if the index is finded => remove it
            if index == key_list[i]:
                del tab[key_list[i]]
            # if no check next key
            else:
                i = + 1
    return tab


def displayTabs(tab):
    for value in tab.items():
        print("titles are: ", value[1][0])


def main():
    # calling other functions
    print("Welcome to Advanced Browser Tabs Simulation")
    choice = 0
    while choice != 9:
        # checking the choice
        # (wrong input repeat the code and exit to end the task)
        displayMenu()
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            print("You open tab: \n", openTab())
        elif choice == 2:
            print("The list of tabs after modification is: \n",
                  closeTab(openTab()))
        elif choice == 3:
            pass
        elif choice == 4:
            print(displayTabs(openTab()))
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            pass
        elif choice == 9:
            print("You are exiting")
        else:
            print("Inavalid input !! \n" + "Try again")
    print("You did exit the program")


main()
