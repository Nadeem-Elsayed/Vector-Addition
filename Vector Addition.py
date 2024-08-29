import math

print("Welcome to the vector addition program, you can add as many vectors in real space as you want")
#make sure that a number is entered
while True:
    try:
        magnitude = float(input("Enter the magnitude of the vector"))
        break
    except:
        print("enter a number")

#make sure that the direction is correct
while True:
    try:
        angle = float(input("Enter the angle starting from the positive x axis. Ex: 56"))
        break
    except:
        print("enter a number")

#get x and y components of the vector

x = magnitude*math.cos(angle)
print(x)
y = magnitude*math.sin(angle)
print(y)
