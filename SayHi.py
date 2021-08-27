# Write a class called Dog that has two properties: name and age. Write a constructor that takes three arguments self, name and age and set these to the object properties.
# Now write a function sayHI(dog) where dog is the dog class object that returns a Hi, my name is <dog’s name> and I am <age> years old!

# sayHi(d1) # Hi, my name is Dot and I am 4 years old!
# sayHi(d2) # Hi, my name is Elf and I am 3 years old!




class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def SayHello(self):
        return "Hello, my name is " + self.name + " and I am " + str(self.age) + " years old!"


def SayHi(Object):
    res = "Hi, my name is "
    res += Object.name
    res += " and I am "
    res += str(Object.age)
    res += " years old!"

    return res

m=Dog("Dot", 4)
print(SayHi(m))
print(m.SayHello())

