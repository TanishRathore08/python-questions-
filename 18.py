# wap to print riverse of the given string also convert the string to uppercase and lowercase

string = input("Enter a string: ")  
a=string[::-1]
print(a)

print("Uppercase:", string.upper())
print("Lowercase:", string.lower())