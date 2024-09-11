class Person():

    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def get_older(self,years):
        self.age += years

luka = Person("Luka",16,"Coding")
luka.get_older(4)

print(luka.name)
print(luka.age)
print(luka.hobby)


# try - except - finally

# wrapping


# def book_title(title):
#     return "Book title: " + title

# def info(title,func):
#     return func(title)

# print(info("Hobbit",book_title))

# pure and impure functions

# lambda

# lambda x: x + 5

# lambda name: "Hello " + name

# map

# def positive_checker(num):
#     return num > 5

# nums = [1,5,-3,2,-5,6,-8,0,2,1,26,0,6,-6,2]

# status = list(map(positive_checker, nums))

# print(status)

# filter

# nums = [1,5,-3,2,-5,6,-8,0,2,1,26,0,6,-6,2]

# status = list(filter(lambda num: num > 0, nums))

# print(status)

# def arguments(name,*names,**namess):
#     print(name)
#     for name in names:
#         print(name)
    
#     for i,v in namess:
#         print("for index","value:",v)



# arguments("luka",("ana","giorgi","erqww"),{"saxeli":"ana","value":"mama"})


class Dinosaur():
    def __init__(self,name,period,diet):
        self.name = name
        self.diet = diet
    
    def roar(self):
        return f"{self.name} roar! RAWHH!"
    
    def info(self):
        return f"{self.name} lived in {self.period} of time and was a {self.diet}"


    class TRex(Dinosaur):
        def __init__(self,name,period):
            super().__init__(name,period,"carnivore")
        
        def roar(self):
            return f"{self.name} was carnivore king of dinosaurs"
    
    class Triceratops(Dinosaur):
        def __init__(self,name,period):
            super().__init__(name,period,"herbivore")
        
        def charge(self):
            return f"{self.name} charges with its horns!"
    

t_rex = TRex("Tyrannosaurus Rex", "Cretaceous")
triceratops = Triceratops("Triceratops", "Cretaceous")

print(t_rex.roar())
print(t_rex.info())

print(triceratops.charge())
print(triceratops.info())

