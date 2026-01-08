# wap to find factoriyal using recurssion

# a = int(input("enter the no:"))

def factorial(a):
    if(a==1 or a==0):
        return 1
    else:
        return (a * factorial(a-1))

print(factorial(4))

