# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:58:10 2023

@author: 1
"""

from urllib.request import urlopen
# urllib.request library for opening URLs
import json
# import json module

parent_tabs = {}
# dict contain all opend tabs, can be access by all functions
nested_tab = {}
# dict contain nested tabs user want to open, can be access by all functions


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
        while repeat != 'no' and repeat != 'yes':
            print("Please enter a valid input 'yes' or 'no': ")
            repeat = input("do you want to add a new Tab ??: ")
            # while loop to check if user want to add a new tab or no
        if repeat.lower() == 'no':
            add_newTab = False
        elif repeat.lower() == 'yes':
            add_newTab = True
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
    dict_1 = {}
    # dict to create nested tab
    list_parent_key = list(tab.keys())
    # adding keys of parent dict to a list
    if index <= len(list_parent_key):
        # checking if the index is smaller or equal to number of Tabs => you can implement a nested tab
        for i in range(len(list_parent_key)):
            # searching for the corresponding tab to the index
            if index == i + 1:
                # adding the title of parent dict as a key for nested dict
                key_1 = list_parent_key[i]
                nested_title = input("enter your nested title: ")
                nested_url = input("enter your nested URL: ")
                # adding nested title and url as values in dict_1
                dict_1[nested_title] = nested_url
                # adding parent title as key and dict_1 as value to the nested tab
                nested_tab[key_1] = dict_1
                return nested_tab
    else:
        print("index of tab does not exist!!")


def clearAllTabs(tab):
    # O(n) n is the number of opened tabs
    # adding the keys of parent dict to a list
    key_list = list(tab.keys())
    # iterating thru the length of list and removing each key with corresponding value
    for i in range(len(key_list)):
        del tab[key_list[i]]
    return tab


def saveTabs(parent_tabs, nested_tab):
    # O(n^2) where n is the number of tabs
    # in worst case senario there is a nested tab in every tab
    file_path = input("enter your file path to save tabs in it ")
    # https://youtu.be/Vrg5ZT3dTLc?si=Ai4yi9TGkWm1gKH0
    with open(file_path + '\midterm.json', 'w') as f:
        # open function the first parameter is the location which we are writing to (taken from user)
        # the file path should finish by /name.json
        # 'w' parameter index of write
        # as alias and f for file
        json.dump(parent_tabs, f)
        # first parameter is the json data  and second parameter is the writer f
    return parent_tabs


def importTabs():
    # o(n^2) in worst case there is a nested tab in each tab (n is the number of tabs)
    # https://youtu.be/IQCx2P3aclA?si=13j1fxwAvQDgL4WY helping of how to import json file
    load_file = input("enter file path to load your file:  ")
    # file path of loaded file given by user
    with open(load_file, 'r') as f:
        # open file location , r for read
        file = json.load(f)
    # load json data from file
    tabs = file.get('tabs', [])
    # get the list of tabs and if file is empty get function return empty list
    for item in tabs:
        # how to use get methode(https://stackoverflow.com/questions/35669227/get-method-for-nested-json-doesnt-work)
        title = item.get('title', '')
        # getting title if doesnt exist return empty string
        url = item.get('url', '')
        # getting url if dosent exist return empty string
        parent_tabs[title] = url
        # adding the title of each tab with the corresponding url
        nested_tab[title] = item.get('nested_tabss', [])
        # adding the nested tabs to nested tabs dictionary
        # NOTE!!! the key of each element should be written same as in get function or the function will return ' '
    return parent_tabs, nested_tab


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
            openTab()
            for key, value in parent_tabs.items():
                print("Title of tab is: ", key,
                      "and the corresponding URL is: ", value)
        elif choice == 2:
            closeTab(parent_tabs)
            print("The list of tabs after modification is: ")
            for key, value in parent_tabs.items():
                print("Title of tab is: ", key,
                      "and the corresponding URL is: ", value)

        elif choice == 3:
            print("the HTML code of the tab is: ", switchTab(parent_tabs))

        elif choice == 4:
            displayTabs(parent_tabs)
            # j is used for title numbering
            j = 1
            # i iterate thru list of parentTabs titles
            for i in parent_tabs:
                print("Title ", j, " is: ", i)
                # checking if the title of parent tab exist as a key in nested tab
                for key, value in nested_tab.items():
                    if key == i:
                        print("with nested tab", key, value)
                j += 1
        elif choice == 5:
            print("your nested Tab is: ", openNestedTab(parent_tabs))
        elif choice == 6:
            print("All Tabs are closed: ", clearAllTabs(parent_tabs))
        elif choice == 7:
            # saveTabs function take parent and nested tabs as parameter and save them in a file using JSON format
            saveTabs(parent_tabs, nested_tab)
        elif choice == 8:
            result = importTabs()
            print("the open tabs are: ", result[0])
            print("the nested tabs are: ", result[1])
        elif choice == 9:
            print("You are exiting")
        else:
            print("Inavalid input !! \n" + "Try again")
    print("You did exit the program")


main()
