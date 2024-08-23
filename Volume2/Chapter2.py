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