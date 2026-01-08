# write a program to print the triangle pattern 1 2 3
                                          #      4 5  
                                          #       6
number = 1
for i in range(3):
    print(" "* i ,end="")
    for j in range(3 - i):
      print(number, end=" ")
      number += 1
    print()
