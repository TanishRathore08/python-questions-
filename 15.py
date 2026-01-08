# write a program to print multiplication table of a given number n.

a = int(input("Enter the multiplication table number: "))

for i in range(1,11):
    print(f"{a} x {i} = {a*i}")