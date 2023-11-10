# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:58:10 2023

@author: 1
"""

from urllib.request import urlopen
# urllib.request library for opening URLs


def displayMenu():
    # O(1) function will always display a constant number of options which is 9
    print("---------------------------------------")
    print("1. Open Tab \n" + "2. Close Tab \n" + "3. Switch Tab \n" +
          "4. Display All Tabs \n" + "5. Open Nested Tab \n" +
          "6. Clear All Tabs \n" + "7. Save Tabs \n" + "8. Import Tabs \n" +
          "9. Exit")
    print("---------------------------------------")


def openTab():
    # O(n) n is the number of tabs user want to open
    # create empty dict
    new_tab = {}
    # set a condition to indicate if we taking new Tab
    add_newTab = True
    # generate number of tabs and used as a key
    tabs_num = 0

    # to check if user still want to add a new Tab
    while add_newTab:
        # title of tab is used as a key
        title = input("Enter the title of Tab: ")
        url = input("Enter the URL of the website: ")
        # creating dict of name new_tab key = title and valur = url
        new_tab[title] = url
        # incrementing number of tabs in case
        tabs_num += 1
        # check if the user want to add a new tab
        repeat = input("do you want to add a new Tab ??: ")
        # use lower() to make char in lower case
        if repeat.lower() == 'no':
            add_newTab = False
    return new_tab


def closeTab(tab):
    # create a function to remove a specific tab the have the dictionary of all tabs as parameter
    # O(n) n is the number of itmes "in worst case user close the last tab exist
    index = int(input("Enter the index of tab that you want to close: "))
    # tab.keys() shows the keys list of dict
    # list used to convert dict keys into list for indexing
    key_list = list(tab.keys())
    # check if the index higher or equal to length of list => close the last tab
    if index >= len(key_list):
        del tab[key_list[-1]]
    # enter else when index is smaller than last key
    else:
        # searching for the inex in key list
        for i in range(len(key_list)):
            # if the index is finded => remove it
            if index == i + 1:
                del tab[key_list[i]]
    return tab


def switchTab(tab):
    # O(n) n is the number of elements of dict cause in worst case senario we will iterate thru all values
    # same as closeTab function check for index if is higher or equal to number of element switch the last tab
    index = int(input("Enter the index of tab that you want to close: "))
    url_list = list(tab.values())
    if index >= len(url_list):
        url = url_list[-1]
        html_code = urlopen(url).read().decode("utf-8")
        print(html_code)
    else:
        # searching for the inex in key list
        for i in range(len(url_list)):
            # if the index is finded => remove it
            if index == i + 1:
                pass
    return tab


def displayTabs(tab):
    # O(n) n is the number of values that exist in the dict
    list_of_titles = []
    # tab.items() display items of dictionary
    for value in tab.items():
        # value[1][0], [1] to access the value
        # [0] to access the first item of value which is the title
        list_of_titles.append(value[0])
    return list_of_titles


def clearAllTabs(tab):
    # O(n) n is the number of opened tabs
    # adding the keys of dict to a list
    key_list = list(tab.keys())
    # iterating thru the length of list and removing each key with corresponding value
    for i in range(len(key_list)):
        del tab[key_list[i]]
    return tab


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
            switchTab(openTab())
        elif choice == 4:
            j = 1
            for i in displayTabs(openTab()):
                print("Title ", j, " is: ", i)
                j += 1
        elif choice == 5:
            pass
        elif choice == 6:
            print("All Tabs are closed: ", clearAllTabs(openTab()))
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
