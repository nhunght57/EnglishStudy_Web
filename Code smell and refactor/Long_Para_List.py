__author__ = 'Nam Xuan'
import sys

class Draws_Rectangle:

     def The_Bigger(self , longerEdge1, shorterEdge1, longerEdge2, shorterEdge2, ):
         if (longerEdge1*shorterEdge1>longerEdge2*shorterEdge2):
           return 1
         else:
           return 2

     def Draw(self , longerEdge1, shorterEdge1, longerEdge2, shorterEdge2,):
         result = self.The_Bigger(longerEdge1, shorterEdge1, longerEdge2, shorterEdge2)
         print("Draws The Rectangle #" + result)

     def __init__(self):
         print("index of eaxh edge of two Rec")
         self.longerEdge1 = input()
         self.shorterEdge1 = input()
         self.longerEdge2 = input()
         self.shorterEdge2 = input()










