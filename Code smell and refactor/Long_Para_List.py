__author__ = 'Nam Xuan'
import sys

class Draws_Rectangle:


     def The_Bigger(self , Rec1, Rec2 ):
         if (Rec1.get_LongerEdge * Rec1.get_ShorterEdge>Rec2.get_LongerEdge*Rec2.get_shorterEdge):
           return 1
         else:
           return 2

     def Draw(self , Rec1, Rec2):
         result = self.The_Bigger(Rec1, Rec2)
         print("Draws The Rectangle #" + result)


class Rectangle:
    LongerEdge = 0
    ShorterEdge = 0
    def get_LongerEdge(self):
        return self.LongerEdge
    def get_ShorterEdge(self):
        return  self.ShorterEdge
    def __init__(self):
        self.LongerEdge = input()
        self.ShorterEdge = input()








