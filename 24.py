# write a program to identify the given number is even or odd using class and object

class Number:
    def check_even_odd(self,num):
        if num % 2 == 0:
            print("even number:",num)
        else:
            print("odd number:",num)

# create object 

obj = Number()

number = int(input("enter the number:"))

# calling object 
obj.check_even_odd(number)
