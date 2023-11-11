# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:58:10 2023

@author: 1
"""

from urllib.request import urlopen
# urllib.request library for opening URLs

parent_tabs = {}
# dict contain all opend tabs
nested_tab = {}
# dict contain nested tabs user want to open


def openTab():
    # O(n) n is the number of tabs user want to open
    # create empty dict

    # set a condition to indicate if we taking new Tab
    add_newTab = True
    # generate number of tabs and used as a key
    tabs_num = 0

    # to check if user still want to add a new Tab
    while add_newTab:
        # title of tab is used as a key
        title = input("Enter the title of Tab: ")
        url = input("Enter the URL of the website: ")
        # creating dict of name parent_tabs key = title and valur = url
        parent_tabs[title] = url
        # incrementing number of tabs in case
        tabs_num += 1
        # check if the user want to add a new tab
        repeat = input("do you want to add a new Tab ??: ")
        # use lower() to make char in lower case
        if repeat.lower() == 'no':
            add_newTab = False
    return parent_tabs


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
    index = int(input("Enter the index of tab that you want to show its HTML: "))
    url_list = list(tab.values())
    if index >= len(url_list):
        # youtube video that help me https://youtu.be/myAFVM7CxWk?si=IZTTnQdtzBJr4Z9t
        url = url_list[-1]
        html_code = urlopen(url).read().decode("utf-8")
    else:
        # searching for the index in key list
        for i in range(len(url_list)):
            # when index in found get the corresponding url
            if index == i + 1:
                url = url_list[i]
                html_code = urlopen(url).read().decode("utf-8")
    return html_code


def displayTabs(tab):
    # O(n) n is the number of values that exist in the dict
    list_of_titles = []
    # tab.items() display items of dictionary
    for value in tab.items():
        # value[1][0], [1] to access the value
        # [0] to access the first item of value which is the title
        list_of_titles.append(value[0])
    return list_of_titles


def openNestedTab(tab):
    # openNestedTab function take a parameter list of tabs that user create
    # and allow user to create a nested tab in a tab they want
    index = int(input(
        "enter index for the tab you want to open a nested tab to it: "))
    if index <= len(list(tab.key())):
        pass
    else:
        print("index of tab does not exist!!")


def clearAllTabs(tab):
    # O(n) n is the number of opened tabs
    # adding the keys of dict to a list
    key_list = list(tab.keys())
    # iterating thru the length of list and removing each key with corresponding value
    for i in range(len(key_list)):
        del tab[key_list[i]]
    return tab


def displayMenu():
    # O(1) function will always display a constant number of options which is 9
    print("---------------------------------------")
    print("1. Open Tab \n" + "2. Close Tab \n" + "3. Switch Tab \n" +
          "4. Display All Tabs \n" + "5. Open Nested Tab \n" +
          "6. Clear All Tabs \n" + "7. Save Tabs \n" + "8. Import Tabs \n" +
          "9. Exit")
    print("---------------------------------------")


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
                  closeTab(parent_tabs))
        elif choice == 3:
            print("the HTML code of the tab is: ")
            print(switchTab(parent_tabs))
        elif choice == 4:
            # j is used for title numbering
            j = 1
            for i in displayTabs(parent_tabs):
                print("Title ", j, " is: ", i)
                j += 1
        elif choice == 5:
            openNestedTab(openTab())
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
