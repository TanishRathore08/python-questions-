# wap to find thr greatest number of three  numbers using nested if condition

a= int(input("enter a:"))
b= int(input("enter b:"))
c= int(input("enter c:"))

if a>b:
    #b is smaller
    if a>c :
        large = a
    else:
        large = c
else:
    if b>c:
        large = b
    else :
        large = c

print("the greatest number",a,b,c,"is", large)
        
