# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:29:20 2017

@author: iibanez
"""

class Animal(object):
    def __init__(self):
        print 'Animal created'
    def eat(self):
        print 'Eating...'
    def whoamI(self):
        print 'animal  ' 
        
        
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ' Dog Created '
        
    def whoamI(self):
        print ' Animal Dog'
    def bark(self):
        print 'Woof'
        
class Simian(object):
    intelligence = True
    def __init__(self,name,species, armed = False):
        self.name = name
        self.species = species
        self.armed = armed
    def saysomething(self):
        print 'Uh Uh Uh Uh!'
    def whoamI(self):
        print 'Hi, my name is %s' %self.name
    def giveittome(self):
        if self.armed:
            return "weapon"
        else:
            return "banana"
        
class Gorilla(Simian):
    def __init__(self, name, species, armed = True):
        Simian.__init__(self, name,species, armed)
        print 'Gorilla maguilla'
    def saysomething(self):
        print 'uarrrrrgh!!!!'
        
    
    
    
    
        
class Book(object):
    def __init__(self, title, Author, pages ):
        print ' A Book is created'
        self.title = title
        self.Author = Author
        self.pages = pages
    def __str__(self):
        return "Title  %s Author: %s  Pags:  %s" %(self.title, self.Author, self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print ' A Book is destroyed '

#calzon = Animal()
#
#calzon.eat()
#calzon.whoamI()
#
#piripi = Dog()
#piripi.bark()
#piripi.whoamI()
#piripi.eat()
#
toston = Book("Jim Boton y Lucas el Maquinista", "un pavo",45)
print toston
#print len(toston)
#del(toston)
#mojo =Simian('Mojo','Chimpanzee')
#print mojo.intelligence
#print mojo.armed
#mojo.saysomething()
#mojo.whoamI()
#print mojo.giveittome()
#
#trojo = Gorilla('pampino', 'Gorilla')
#trojo.saysomething()
#print trojo.name
#print trojo.species
#print trojo.giveittome()
#print trojo.whoamI()

