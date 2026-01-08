
# getter in python

#      1. example of getter and setter

# defining a class

class myclass:
    def __init__(self,value):
        self.value = value 
    
    def show(self):
        print(f"value is {self.value}")

    @property
    def ten_value(self):
        return self.value * 10
    
    @ten_value.setter
    def ten_value(self, unwanted_value):
        self.value = unwanted_value 

    
# # creating an object of the class

obj = myclass(25)

obj.ten_value = 50  # accessing the setter method
print(obj.ten_value)  # accessing the getter method
obj.show()  # calling the method    



#                   2. example of getter and setter

class temperature:
    def __init__(self,celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, fahrenheit):
        self._celsius = (fahrenheit - 32) * 5/9

a = temperature(37)
a.celsius = 15  # accessing the setter method
print(a.celsius,"celsius")  # accessing the getter method







