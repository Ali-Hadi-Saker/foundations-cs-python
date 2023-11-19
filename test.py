# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 23:39:44 2023

@author: 1
"""


class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def Honk(self):
        print("my car of type", self.model, "and color",
              self.color, "and year", self.year, "goes beep beep")

    def getColor(self):
        return self.color

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model


def main():
    car1 = Car("read", "ferrari", "2010")
    car2 = Car("blue", "marcedes", "2020")
    car1.Honk()
    car2.getColor()
    print("car2 model is", car2.getModel())
    print("car2 color is", car2.getColor())
    car2.setModel("toyota")
    print("car2 model is", car2.getModel())


main()
