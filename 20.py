# write a program to print ṭable of a given no using class and object

# create class table
class Table :
    def  data(self):
        self.number = int(input("enter the number:"))

    def show(self):
        for i in range(1, 11):
            print(f"{self.number} x {i} = {self.number * i}")

# create object of class

Tanish = Table()
Tanish.data()   
Tanish.show()