# This is a secrat code generator

from coding import *
from Decode import *
import random as rn

# Welcome Screen
intro = "'Welcome to the Secret Code Generator'"
print(intro.center(50))
das = '______________________________________'
print(das.center(50))


print()
print("For making Secret Code: Type '1'")
print("For Decoding Secrate Code: Type '2'")
print()
X = int(input("Enter: "))

# This part will make Secrate code
if X == 1:
    coding()
# This part will Decode the Secrate code
elif X == 2:
   decode()

# This will exit the program
else:
  print("Exit")
  