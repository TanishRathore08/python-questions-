# write a program to convert kilometers into miles

kilometers = float(input("enter kilometers:"))

# coversion factor: 1 km = 0.621371

conversion_factor = 0.621371

miles = kilometers*conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")
