 # 1. parameterized constructor


                  # example no 1 

# creating a class
class person:

    # creating a parameterized constructor
    def __init__(self,name,occ,age,gender,city):
        self.name = name
        self.occ = occ
        self.age = age
        self.gender = gender
        self.city = city
    
   # crearing a object of the class

a = person("tanish","student",19,"male","gwalior")

# printing the attributes
print(f"{a.name} is a {a.occ}. he is {a.age} year old and he lives in {a.city} . he is {a.gender}")

#                     # example no 2

# creating a class
class car:

    # creating a parameterized constructor
    def __init__(self,brand,model,year,color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

# creating an object of the class
c = car("ford","mustang",2020,"red")

# printing the attributes
print(f"car brand is {c.brand} , model is {c.model} , year is {c.year} and color is {c.color}") 





# 2. default constructor

                # example no 1  

# # creating a class

class person:

    # creating a default constructor
    def __init__(self):
        self.name = "tanish"
        self.occ = "student"
        self.age = 19

# creating an object of the class
p = person()

# printing the attributes
print(f"{p.name} is a {p.occ}. he is {p.age} year old.")


                # example no 2

# # creating a class

class game:

    # creating a default constructor
    def __init__(self):
        self.title = "minecraft"
        self.genre = "sandbox"
        self.platform = "pc"

# # creating an object of the class
g = game()

# # printing the attributes
print(f"game title is {g.title} , genre is {g.genre} and platform is {g.platform}.")