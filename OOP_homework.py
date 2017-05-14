# -*- coding: utf-8 -*-
"""
Created on Sun May 14 17:21:09 2017

@author: iibanez
"""
from math import sqrt, pi
class Line(object):
    '''
    Class that accepts bi-dimensional line coordinates as tuples, to define
    a line trigonometrically
    Parameters:
        coor1: tuple with coordinates of point A
        coor2: tuple with coordinates of point B
        xdiff: float with the length of the line's horizontal proyection
        ydiff: float with the length of the line's vertical proyection
    methods:
        distance: calculates trigonometric length of the line
        slope: calculates the slope of the line.
    '''
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.xdiff = float(self.coor2[0] - self.coor1[0])
        self.ydiff = float(self.coor2[1] - self.coor1[1])
        
    def distance(self):
        return sqrt((self.xdiff**2)+(self.ydiff**2))
    
    def slope(self):
        return (self.ydiff/self.xdiff)
    
class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (pi*(self.radius**2)*self.height)
    
    def surface_area(self):
        return (2*pi*(self.radius*self.height))+(4*pi*(self.radius**2))
 
    
line1 = Line((3,2),(8,10))
print line1.distance()
print line1.slope()

cil1 = Cylinder(2,3)
print cil1.volume()
print cil1.surface_area()