
# # public access modifier

# class Public_Class:
#     def __init__(self,name,age):
#         self.name = name      # public variable
#         self.age = age        # public variable
        
# a= Public_Class("Alice",30)
# print(f"Name: {a.name}, Age: {a.age}")  # accessing public variables outside the class


# private access 

# class student:
#     def __init__(self,name,age):
#         self.__name = name      # private variable
#         self.__age = age        # private variable

#     def __funname(self):

#         self.y=34
#         print(self.y)

# class subject(student):
#     pass

# obj = student("Bob",25)
# obj2= subject


# print(obj.__age)   # these all are  not accessible outside the class
# print(obj.__name)

# print(obj2.__name)
# print(obj2.__age)


# protected access modifier

class student:
    def __init__(self,name,age):
        self._name = name      # protected variable
        self._age = age        # protected variable

    def _funname(self):
       return "Hello"
    
class subject(student):
   
   pass

obj = student()
obj2= subject()

print(obj._name)        # accessing protected variable outside the class
print(obj._age) 
print(obj._funname())   

print(obj2._name)        # accessing protected variable outside the class
print(obj2._age) 
print(obj2._funname())