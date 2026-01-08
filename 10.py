# write a program to check prime numbers

# first we take a user input
a = int(input("enter the number:"))

if a==1:
    print("it is not a prime number")
if a>1:
    for i in range(2,a):
        if a % i == 0:
            print("it is not a prime number")
            break
    else :
            print("it is a prime number")