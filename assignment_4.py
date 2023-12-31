# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 09:28:59 2023

@author: 1
"""


def displayMenu2():
    # display this menu if user choose choice 1
    print("\n--------------------------------------")
    print("a. Add Node\n" + "b. Display Nodes\n" +
          "c. Search for & Delete Node\n" + "d. Return to main")
    print("--------------------------------------")


class Node:
    # class node hold data and the next of the node
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    # class linked list hold head pointer and all needed behaviors
    def __init__(self):
        self.head = None
        self.tail = None  # tail help to add a new node (for optimization)
        self.size = 0

    def size(self):

        return self.size

    def addNode(self, value):
        # O(1) just adding to the end of LL using tail pointer
        node = Node(value)  # create the object node
        # check if LL is empty
        if self.size == 0:
            # Head and tail pointing to the first node
            self.head = node
            self.tail = node
            self.size += 1
        else:
            # add the new node to the end of LL
            self.tail.next = node
            self.tail = node
            self.size += 1
        print("We succefuly add the new node", node.info)

    def addNode3(self, value):
        # 2nd add node function used for add vertex
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print("adding", new_node.info)

    def removeNode(self, value):
        # remove Node function used to remove vertex
        if not self.size:
            print("list empty")
        else:
            current = self.head
            prev = current
            while current:
                if current.info != value and current:
                    prev = current
                    current = current.next
                if current.info == value:
                    prev.next = current.next
                    self.size -= 1

    def displayNode(self):
        # O(n) n number of nodes in the LL
        if self.size == 0:
            # check if LL is empty
            print(" the Linked List is empty")
        else:
            current = self.head
            while current:
                print(current.info, end=" --> ")
                current = current.next

    def searchDelete(self, value):
        # O(n) n is the number of nodes
        if self.size == 0:
            print("Nothing to delete list is empty")
        else:
            # handeling when delete the first node
            current = self.head
            if current.info == value:
                self.head = current.next
                self.size -= 1  # decrement size of LL
            else:
                prev = current  # create previous varaible
                # search for value in the LL
                while current.info != value and current:
                    prev = current
                    current = current.next
                if current.info == value:
                    prev.next = current.next
                    self.size -= 1  # decrement size of LL
                else:
                    print("the value you are lokking for doesn t exist in the list ")


def singlyLL():
    choice_2 = 0
    # while loop to check the user choice
    # if your choose 'd' loop will be break and the code go back to the main function
    LL = LinkedList()  # create an instance LL of linked list class
    while choice_2 != 'd':
        displayMenu2()
        choice_2 = input("Peek your choice from the list: ").lower()
        if choice_2 == 'a':
            new_node = input("enter the value of new node: ")
            LL.addNode(new_node)
        elif choice_2 == 'b':
            LL.displayNode()
        elif choice_2 == 'c':
            remove_value = input("Enter the value you want to remove: ")
            LL.searchDelete(remove_value)
        elif choice_2 == 'd':
            print("Return back to main Menu")
        else:
            print("Invalid input!!" + "Try again:")


def checkPalindrom():
    # O(n/2) n is the number of char in the string
    # convert string to a list
    queue = list(input("Enter your string: ").lower())
    # make all char lower
    while len(queue) > 1:
        # check until number of char is higher than 1
        if queue.pop(0) != queue.pop(-1):
            # pop function to remove first and last element
            return False
    return True


def displayMenu3():
    # display this menu if user choose choice 3
    print("\n--------------------------------------")
    print("a. Add a student\n" + "b. Interview a student\n"
          + "c. Return to main")
    print("--------------------------------------")


class Student:
    def __init__(self, name, midterm_grade, final_grade, attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.attitude = attitude

    def __str__(self):
        # string function print the object student with corresponding characteristics
        return "Name: " + self.name + ", midterm grade: " + str(self.midterm_grade) + "/100" + ", final grade: " + str(self.final_grade) + "/100" + ", attitude: " + self.attitude
    # create get methode for student class


class Node2:
    def __init__(self, student):
        self.student = student
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None  # initiate head pointer
        self.size = 0

    def displayNode(self):
        current = self.head
        while current != None:
            print(current.student)
            current = current.next

    def enqueue(self, student):
        node = Node2(student)
        if self.size == 0:  # if the list is empty
            self.head = node
            self.size += 1
        else:
            current = self.head
            previous = current
            if student.attitude and (student.final_grade > self.head.student.final_grade) or (student.final_grade == self.head.student.final_grade and student.midterm_grade > self.head.student.midterm_grade):
                # when adding a student with good attitude and first node is bad attitude
                node.next = self.head
                self.head = node
                self.size += 1
            else:
                # need to recheck this part
                while current is not None and (student.attitude and (student.final_grade < current.student.final_grade or (student.final_grade == current.student.final_grade and student.midterm_grade < current.student.midterm_grade))) or (not student.attitude and student.final_grade < current.student.final_grade):
                    previous = current
                    current = current.next
                previous.next = node
                node.next = current
                self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("No student to interview ")
        elif self.size == 1:
            print("Interview student", self.head.student)
            self.head = None
            self.size -= 1
        else:
            print("Interview student", self.head.student)
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1


def priorityQueue():
    displayMenu3()
    choice_3 = 0
    while choice_3 != 'c':
        choice_3 = input("Enter your choice: ").lower()
        if choice_3 == 'a':
            pq = PriorityQueue()
            # O(n) n number of students user that want to add
            add_new_student = True
            # check if user want to add student
            while add_new_student:
                name = input("enter name: ")
                midterm_grade = int(input("enter midterm grade: "))
                final_grade = int(input("enter final grade: "))
                attitude = input("enter student attirude: ")
                student = Student(name, midterm_grade, final_grade, attitude)
                pq.enqueue(student)
                repeat = input("do you want to add more student ? ").lower()
                # loop to handle inavlid input
                while repeat != 'yes' and repeat != 'no':
                    repeat = input(" enter 'yes' or 'no': ").lower()
                if repeat.lower() == 'yes':
                    add_new_student = True
                else:
                    add_new_student = False
            pq.displayNode()
        elif choice_3 == 'b':
            pq = PriorityQueue()
            pq.dequeue()
        elif choice_3 == 'c':
            print("Going back to Main Menu")
        else:
            print("Invalid input!!\n" + "Please enter a valid choice a or b")


def calcule(s):
    # O(n) n is the number of element in stack
    cur = 0  # cuurent number
    op = '+'  # operator
    stack = []

    def arithmeticCalcule(op, num):
        # arithmetic function take operator and number as parameter
        # add result to stack
        # we will sum all elements of stack at the end
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop() * num)
        else:
            if num != 0:
                stack.append(int(stack.pop() / num))
            else:
                stack.append(0)
    for i in range(len(s)):
        if s[i].isdigit():
            # check if the element is int if yes put it as current parameter
            cur = int(s[i])
        elif s[i] == '(':
            # when ( add the op to the stack
            stack.append(op)
            cur = 0  # to start calcule inside()
            op = '+'  # start operation by adding
        elif s[i] in ['+', '-', '*', '/', ')']:
            arithmeticCalcule(op, cur)
            if s[i] == ')':
                cur = 0
                # when facing ')'
                while isinstance(stack[-1], int):
                    # keep calculating and adding result to cuurent until stack[-1] != int
                    # stack[-1] will be op adding when '('
                    cur += stack.pop()
                op = stack.pop()
                # giving op its value befor '('
                arithmeticCalcule(op, cur)
            cur = 0  # start again with cur = 0 and op = s[i]
            op = '+'
    arithmeticCalcule(op, cur)  # calcule last digit
    return sum(stack)


def displayMenu_5():
    # display this menu if user choose choice 5
    print("\n--------------------------------------")
    print("a. Add vertex\n" + "b. Add edge\n"
          + "c. Remove vertex\n" + "d. Remove edge\n" + "e. Display vertices with a degree of X or more: \n" +
          "f. Return to main")
    print("--------------------------------------")


class Graph:
    # i choose AL cause we start with empty graph (no vertex and edges)
    # add vertex and edges when user ask to
    def __init__(self):
        self.adj_list = {}
        # keys of dict are the vertex
        # element pointing to LL

    def addVertex(self, vertex):
        # O(1)
        if vertex not in self.adj_list:
            self.adj_list[vertex] = LinkedList()
            print(vertex, "successfully added")
            return
        else:
            print(vertex, "Vertex already exist")

    def addEdge(self, vertex_1, vertex_2):
        # O(1) adding a node
        if vertex_1 in self.adj_list and vertex_2 in self.adj_list:
            self.adj_list[vertex_1].addNode3(vertex_2)
            self.adj_list[vertex_2].addNode3(vertex_1)
            print("Edge btween", vertex_1, "and", vertex_2, "added")

        elif vertex_1 not in self.adj_list and vertex_2 in self.adj_list:
            print(vertex_1, "does not exist")

        elif vertex_2 not in self.adj_list and vertex_1 in self.adj_list:
            print(vertex_2, "does not exist")

        else:
            print(vertex_1, "and", vertex_2, "does not exist")

    def displayGraph(self):
        # O(n^2) looping over all vertecies O(n) and calling function display node which is O(n)
        # where n is the number of vertecies
        if self.adj_list == {}:
            print("Graph is empty!")
        else:
            for vertex in self.adj_list:
                print(vertex, end=" --> ")
                self.adj_list[vertex].displayNode()
                print("\n")

    def removeVertex(self, value):
        # O(n) n number of nodes
        if self.adj_list == {}:
            print("Graph is empty!")
        else:
            for key in self.adj_list.keys():
                if key == value:
                    self.adj_list.pop(value)
                self.adj_list[key].removeNode(value)
            print(value, "vertex is deleted")

    def removeEdges(self, vertex_1, vertex_2):
        # O(n) n is the number of node in the ll
        if vertex_1 in self.adj_list and vertex_2 in self.adj_list:
            # check if the 2 vertecies exist so edge exist
            self.adj_list[vertex_1].removeNode(vertex_2)
            self.adj_list[vertex_2].removeNode(vertex_1)
            print("Edge between", vertex_1, "and", vertex_2, "removed")
        else:
            print("edge does ot exist!!")

    def displayDegree(self, n):
        # O(n) n is the number of vertecies exist
        for key in self.adj_list.keys():
            # looping in each LL
            if self.adj_list[key].size >= n:
                # check if number of element >= n
                print("vertex:", key, "has degre of", self.adj_list[key].size)


def graph():
    graph = Graph()
    choice_5 = 0
    while choice_5 != 'f':
        displayMenu_5()
        choice_5 = input("Choose your choice from the list above: ").lower()
        if choice_5 == 'a':
            repeat = True
            while repeat:
                vertex = input("Enter vertex you would like to add ")
                graph.addVertex(vertex)
                add_more = input("Would you like to add more vertex: ")
                while add_more != 'yes' and add_more != 'no':
                    add_more = input("Enter 'yes' or 'no': ")
                if add_more == 'yes':
                    repeat = True
                else:
                    repeat = False
            graph.displayGraph()  # display graph wehn user finish adding

        elif choice_5 == 'b':
            repeat = True
            while repeat:
                vertex_1 = input(
                    "Enter vertex 1 you would like to add edge to: ")
                vertex_2 = input(
                    "Enter vertex 2 you would like to add edge to: ")
                graph.addEdge(vertex_1, vertex_2)
                add_more = input("Would you like to add more edges: ")
                while add_more != 'yes' and add_more != 'no':
                    add_more = input("Enter 'yes' or 'no': ")
                if add_more == 'yes':
                    repeat = True
                else:
                    repeat = False
            graph.displayGraph()
        elif choice_5 == 'c':
            value = input("Enter the vertex you want to remove: ")
            graph.removeVertex(value)
        elif choice_5 == 'd':
            vertex_1 = input("Enter first vertex of the edge: ")
            vertex_2 = input("Enter second vertex of the edge: ")
            graph.removeEdges(vertex_1, vertex_2)
        elif choice_5 == 'e':
            n = int(input("Enter degree of vertex you want to desplay: "))
            graph.displayDegree(n)
        elif choice_5 == 'f':
            print("Going back to Main menu")
        else:
            print("Invalid input!!")


def displayMenu():
    print("--------------------------------------")
    print("1. Singly Linked List\n" + "2. Check if Palindrome\n" +
          "3. Priority Queue\n" + "4. Evalute an Inflix Expression\n" + "5. Graph\n" + "6. Exit")
    print("--------------------------------------")


def main():

    user_name = input("Please enter your name: ")
    print("\nWelcome to our programme", user_name)
    choice = 0
    limit = 0  # limit for wrong input
    while choice != 6 and limit != 4:
        displayMenu()
        choice = int(input("Please enter your choice from the list above: "))
        if choice == 1:
            singlyLL()
            limit = 0  # reset limits
        elif choice == 2:
            limit = 0  # reset limits
            result = checkPalindrom()
            if result:
                print("Your string is palindrome")
            else:
                print("Your string is not palindrome")
        elif choice == 3:
            limit = 0  # reset limits
            priorityQueue()
        elif choice == 4:
            limit = 0  # reset limits
            s = input("Enter you equation: ")
            result = calcule(s)
            print("Result of your equation is: ", result)
        elif choice == 5:
            limit = 0  # reset limits
            graph()
        elif choice == 6:
            print("You are exiting")
        else:
            print("Please enter a valid choice")
            limit += 1

    print("You did exit the programme")


main()
