
# #  first create a base class

# # class manager:
# #     def __init__(self,name,id,salary):
# #         self.name = name
# #         self.id = id
# #         self.salary = salary

# #     def display(self):
# #         print(f"Manager Name: {self.name}, ID: {self.id}, Salary: {self.salary}")

# # class employee(manager):    # then create a derived class using the base class attributes/
# #     def show_language(self):
# #         print("the deault programming language is python")

# # # create an object for base class

# # base_obj = manager("tanish",1,150000)
# # base_obj.display()

# # # create an object for derived class

# # derived_obj = employee("rahul",2,120000)
# # derived_obj.display()
# # derived_obj.show_language()










# # #                  single inheritance 

# # # Base class
# # class Animal:
# #     def __init__(self, name, age, color):
# #         self.name = name
# #         self.age = age
# #         self.color = color

# #     def eat(self):
# #         print(f"{self.name} is eating.")

# #     def sleep(self):
# #         print(f"{self.name} is sleeping.")


# # # Derived class (Cat)
# # class Cat(Animal):
# #     def __init__(self, name, age, color, breed):
# #         super().__init__(name, age, color)   # Calling base class constructor
# #         self.breed = breed

# #     # Cat-specific methods
# #     def meow(self):
# #         print(f"{self.name} says Meow!")

# #     def scratch(self):
# #         print(f"{self.name} is scratching the furniture.")

# #     def purr(self):
# #         print(f"{self.name} is purring happily.")


# # # Creating a Cat object
# # my_cat = Cat("gudiya", 2, "White", "Persian")

# # # Calling methods
# # my_cat.eat()       # Inherited from Animal
# # my_cat.sleep()     # Inherited from Animal
# # my_cat.meow()      # Cat specific
# # my_cat.scratch()   # Cat specific
# # my_cat.purr()      # Cat specific





# #               multuple inheritance

# # Base class 1

# class data_science:
    

#     def __init__(self,tools,duration):
#         self.tools = tools
#         self.duration = duration
    
#     def show(self):
#         print("python is a programming language")


# # Base class 2


# class  Web_development:
    
#     def __init__(self,frameworks,duration):
#         self.frameworks = frameworks
#         self.duration = duration

#     def show(self):
#         print("javascript is a programming language")

# # Derived class

# class  full_stack(Web_development,data_science):

#     def __init__(self,tools,duration,frameworks):
#         data_science.__init__(self,tools,duration)
#         Web_development.__init__(self,frameworks,duration)


# object = full_stack(["numpy","pandas"],6,["react","angular"])
# object.show()   # method resolution order is from left to right so it will call data_sc
# print(full_stack.mro())   

# # what is mro (method resolution order)===            ye check krna h ki agar multiple inheritance me same name ke method h to konsa call hoga .



#              multilevel inheritance

# Base class

# class animal:

#     def __init__(self,name,age,color):
#         self.name = name
#         self.age = age
#         self.color = color
    
#     def eat(self):
#         print("animal is eating")


# # Derived class 1

# class dog(animal):
#     def __init__(self,name,age,color,breed):
#         dog.__init__(name,age,color)
#         self.breed = breed

#     def bark(self):
#         print("dog is barking")


# # Derived class 2

# class puppy(dog):
#     def __init__(self,name,age,color,breed,toy):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.breed = breed
#         self.toy = toy

#     def weep(self):
#         print("puppy is weeping")
    

# object creation
# puppy_obj = puppy("tommy",1,"brown","bulldog","ball")
# print(f"Puppy Name: {puppy_obj.name}, Age: {puppy_obj.age}, Color: {puppy_obj.color}, Breed: {puppy_obj.breed}, Toy: {puppy_obj.toy}")
# puppy_obj.weep()
# puppy_obj.bark()
# puppy_obj.eat()





#   hybrid inheritance 

# base class

class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print("i am a human")

# derived class 1

class student(human):
    def __init__(self,name,age,roll_no):
        human.__init__(self,name,age)
        self.roll_no = roll_no

    def display(self):
        print("i am a student")

# derived class 2

class employee(human):  
    def __init__(self,name,age,emp_id):
        human.__init__(self,name,age)
        self.emp_id = emp_id

    def info(self):
        print("i am an employee")

# derived class 3

class working_student(student,employee):
    def __init__(self,name,age,roll_no,emp_id,company):
        student.__init__(self,name,age,roll_no)
        employee.__init__(self,name,age,emp_id)
        self.company = company

    def details(self):
        print("i am a working student")

# object creation
ws_obj = working_student("alice",22,101,5001,"TechCorp")
print(f"Name: {ws_obj.name}, Age: {ws_obj.age}, Roll No: {ws_obj.roll_no}, Employee ID: {ws_obj.emp_id}, Company: {ws_obj.company}")
ws_obj.details()        
ws_obj.display()
print(working_student.mro())



#   hierarchical inheritance

# base class

class company:
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def info(self):
        print("this is a company") 

# derived class 1

class manager(company):
    def __init__(self,name,location,dept):
        company.__init__(self,name,location)
        self.dept = dept

    def display(self):
        print("this is a manager")

# derived class 2
class manager2(company):
    def __init__(self,name,location,team_size):
        company.__init__(self,name,location)
        self.team_size = team_size

    def show(self):
        print("this is another manager")

# derived class 3
class intern( manager,manager2):
    def __init__(self,name,location,duration):
        company.__init__(self,name,location)
        self.duration = duration

    def details(self):
        print("this is an intern") 



# object creation
company_obj = company("TechCorp","New York")
intern_obj = intern("TechCorp","New York",6)
manager_obj= manager("BizInc","Chicago","Sales")
manager2_obj = manager2("InnovateLtd","San Francisco",10)
print(f"Intern Company: {intern_obj.name}, Location: {intern_obj.location}, Duration: {intern_obj.duration} months")