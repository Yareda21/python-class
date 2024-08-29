# this is where you declare all the class

class Car:
    def __init__(self,Name,cylinder,color,brand) -> None:
        self.Name = Name
        self.cylinder = cylinder
        self.color = color
        self.brand = brand

vitz = Car("vitz","v3","transparent","toyota")
print(vitz.Name,vitz.cylinder,vitz.color,vitz.brand)

class Laptop:
    def __init__(self,name,Ram,storage,system_type,genreation,core,graphics) -> None:
        self.name = name
        self.Ram = Ram
        self.storage = storage
        self.system_type = system_type
        self.genreation = genreation
        self.core = core
        self.graphics = graphics

ASUS = Laptop("Asus","16","1TB","64 bit","12 generation","core i 7","iris x")
print(ASUS.name,ASUS.Ram,ASUS.storage,ASUS.system_type)

class Bottle:
    def __init__(self,brand,shape) -> None:
        self.brand = brand
        self.shape = shape

Ice_mountain = Bottle("Ice mountain","cylinder")

print(Ice_mountain.brand,Ice_mountain.shape)
      

        
        