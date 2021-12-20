import random
from tkinter import *

again = True

while again:
    print("1.roll the dice      2.Exit")
    user=int(input("Kindly press any of above "))
    if user==1:
        number=(random.randint(1,6))
        print(number)

    else:
        break
print("Please type 1 to play")