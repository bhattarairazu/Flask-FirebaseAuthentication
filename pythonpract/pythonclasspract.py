class Parrot:
    # class attribute
    species = "birds"

    #instance variabels
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #methods inside class i.e class methods
    def sing(self,song):
        return "{} sings {}".format(self.name,song)


# instance the parrot class
blu = Parrot("Blu",10)
woo = Parrot("hh",23)

## accessing the class attributes
print("Blue is a {}".format(blu.__class__.species))

# accessing instance attributes
print("{} is {} years old".format(blu.name,blu.age))

print(blu.sing("hello world"))

# Inheritacne demonstration
class Birds:
    def __init__(self):
        print("BIrd ready")

    def whoisThis(self):
        print("Bird")

    def run(self):
        print("Run bird")

# inheriting birds to the penguin
class Penguin(Birds):
    def __init__(self):
        # calling birds init method
        super().__init__()
        print("Penguin is ready")
    
    def swim(self):
        print("penguind swiming")

pen = Penguin()
pen.swim()
pen.whoisThis()
pen.run()


print("Encapsulation in pyton")

# __ or _ denotes privated variable in python i.e double undersore or single underscore

class Computer:
    def __init__(self):
        self.__maxprice = 100
    
    def sell(self):
        print(f"Selling price is {self.__maxprice}")

    def setMaxPrie(self,price):
        self.__maxprice = price
    
c = Computer()
c.sell()

c.__maxprice = 300 # it does not set 300 as max price cuase max price is private and cann't be accessed from the instance variable
c.sell()

c.setMaxPrie(3)
c.sell()