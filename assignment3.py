# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 23:40:05 2023

@author: 1
"""
def Matrices():
    rows = eval(input("enter number of rows: "))
    columns = eval(input("enter number of columns: "))
    matrix_1 = []
    matrix_2 = []
    print("enter values of the first matrix")
    #fill the first matrix
    for i in range(rows):
        print("row: ", i)
        matrix_1.append([])
        for j in range(columns):
            print("column: ", j)
            value = eval(input("enter the value: "))
            matrix_1[i].append(value)
    print("enter values of the second matrix")
    #fill the second matrix
    for i in range(rows):
       print("row: ", i)
       matrix_2.append([])
       for j in range(columns):
           print("column: ", j)
           value = eval(input("enter the value: "))
           matrix_2[i].append(value)
    #retuen the 2 matrices as elements in a list beacause we cannot return 2 values from 1 function
    return [matrix_1,matrix_2]
    
def addMatrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):#i in range numbers of rows of matrix
        result.append([])
        for j in range(len(matrix1[0])):#j in range numbers of columns of matrix
            result[i].append(matrix1[i][j] + matrix2[i][j])
    return result
def checkRotation(matrix1, matrix2):
    transposed_matrix = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
    #the outer loop is created by i in range(len(matrix1[0])) to loop thrue column of matrix and the j in range(len(matrix1)) is the inner loop that goes thrue column of matrix   
    if transposed_matrix == matrix2:
        return True
    else:
        return False
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
            matrices = Matrices()#capture returned values
            print(addMatrices(matrices[0],matrices[1]))#pass the matrices to add function
        elif choice == 2:
            checkRotation()
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
            print("Invalid input!!")
            print("Please enter a valid option")
    
main()
        
