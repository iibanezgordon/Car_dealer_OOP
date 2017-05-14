# -*- coding: utf-8 -*-
"""
Created on Sun May 14 11:24:25 2017

@author: iibanez
"""


from abc import ABCMeta, abstractmethod

class Vehicle(object):
    '''
    Abstract Vehicle Class, which defines the basic attributes and methods
    of a vehicle.
    
    Atributes:
        wheels: number of wheels 
        Km: number of km
        make: String with the vehicle brand
        model: String with vehicle model
        year: an Int with the year of production.
        sold_on: showing the date the vehicle was sold, or None otherwise
    '''
    
    __metaclass__ = ABCMeta
    
    base_sale_price = 0  #This is an abstract class, and the base price is 0
    wheels = 0
      
    def __init__(self, Km, make, model, year, sold_on):
          self.Km = Km
          self.make = make
          self.model = model
          self.year = year
          self.sold_on = sold_on
          

        
      
    def sale_price(self):
          '''
          Return the sale price for this vehicle as a Float
          The money WE ask for it
          '''
          
          if self.sold_on is not None:
              print 'The Vehicle is already sold'
              return 0.0 #Already sold...
          else:
              return self.wheels * 5000.0
        
    def purchase_price(self):
          '''
          Return the Purchase Price of the Vehicle as a float
          The money WE offer for it
          '''
          if self.sold_on is None:
              print ' The car is part of our fleet'
              return 0.0  #We already have the car
          else:
              return self.base_sale_price -(0.1 *self.Km)
      
    @abstractmethod
    def vehicle_type(self):
            '''
            Return a String with the Vehicle type
            '''
            pass
        
class Car(Vehicle):
    '''
    Car Class, descendant from Vehicle.
    
    Atributes:
        wheels: number of wheels 
        Km: number of km
        make: String with the vehicle brand
        model: String with vehicle model
        year: an Int with the year of production.
        sold_on: showing the date the vehicle was sold, or None otherwise
        
    '''
    base_sale_price = 8000.0  #This is an abstract class, and the base price is 0
    wheels = 4
    
    def __str__(self):
        return ('Car %s %s from the year %i with %i km' %(self.make, self.model
                                                          , self.year, self.Km))
    
    def vehicle_type(self):
            '''
            Return a String with the Vehicle type
            '''
            return 'car'    

class Truck(Vehicle):
    '''
    Car Class, descendant from Vehicle.
    
    Atributes:
        wheels: number of wheels 
        Km: number of km
        make: String with the vehicle brand
        model: String with vehicle model
        year: an Int with the year of production.
        sold_on: showing the date the vehicle was sold, or None otherwise
        
    '''
    base_sale_price = 10000.0  #This is an abstract class, and the base price is 0
    wheels = 4
    
    def __str__(self):
        return ('Truck %s %s from the year %i with %i km' %(self.make, self.model
                                                          , self.year, self.Km))
    
    def vehicle_type(self):
            '''
            Return a String with the Vehicle type
            '''
            return 'Truck'    
          
class Bike(Vehicle):
    '''
    Car Class, descendant from Vehicle.
    
    Atributes:
        wheels: number of wheels 
        Km: number of km
        make: String with the vehicle brand
        model: String with vehicle model
        year: an Int with the year of production.
        sold_on: showing the date the vehicle was sold, or None otherwise
        
    '''
    base_sale_price = 4000.0  #This is an abstract class, and the base price is 0
    wheels = 2
    
    def __str__(self):
        return ('Motorcycle %s %s from the year %i with %i km' %(self.make, self.model
                                                          , self.year, self.Km))
    
    def vehicle_type(self):
            '''
            Return a String with the Vehicle type
            '''
            return 'Bike'              
          
            
            
            
            
            
            