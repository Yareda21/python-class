# this is where you declare all the class

class Person:
      def __init__(self, name, gender, age, color, height):
            self.name = name
            self.gender = gender
            self.age = age
            self.color=color
            self.height=height




micky = Person("Micky", "Male", 21, "Black", 1.30)


#  car, laptop, bottle
class Car:
      def __init__(self, name, cylinder,brand,colour,hp):
            self.name=name
            self.cylinder=cylinder
            self.brand=brand
            self.colour=colour
            self.hp=hp
            
bugatti=Car("bugatti","v16","bugatti","black","1500hp")
print(bugatti.name,bugatti.cylinder,bugatti.brand,bugatti.colour,bugatti.hp)



class Laptop:
      def __init__(self,brand,storage,ram,bc):
            self.brand=brand
            self.storage=storage
            self.ram=ram
            self.bc=bc

dell=Laptop("dell","1tb","12gb","25000mah")
print(dell.brand,dell.storage,dell.ram,dell.bc)



class Bottle:
      def __init__(self,shape,brand):
            self.shape=shape
            self.brand=brand



voss=Bottle("circular","voss")
print(voss.shape,voss.brand)
      
            



            