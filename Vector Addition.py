import math

print("Welcome to the vector addition program, you can add as many vectors in real space as you want")
#make sure that a number is entered
while True:
    try:
        magnitude = float(input("Enter the magnitude of the vector: "))
        break
    except:
        print("enter a number")

#make sure that the direction is correct
while True:
    try:
        #gets the angle and converts to radians
        angle = math.radians(float(input("Enter the angle starting from the positive x axis in degrees: ")))
        break
    except:
        print("enter a number")

#get x and y components of the vector
run_x = magnitude*math.cos(angle)
run_y = magnitude*math.sin(angle)

#///////////////////////adding more vectors
go_on = "y"
while go_on == "y":
    print("add another vector")
    #make sure that a number is entered
    while True:
        try:
            magnitude = float(input("Enter the magnitude of the vector: "))
            break
        except:
            print("enter a number")

    #make sure that the direction is correct
    while True:
        try:
            #gets the angle and converts to radians
            angle = math.radians(float(input("Enter the angle starting from the positive x axis in degrees: ")))
            break
        except:
            print("enter a number")

    #get x and y components of new vector
    new_x = magnitude*math.cos(angle)
    new_y = magnitude*math.sin(angle)

    #set the running x and y components, this gives us the running total
    run_x =  run_x + new_x
    run_y = run_y + new_y
    magnitude = round(math.sqrt(run_x**2 + run_y**2),4) #pythagorean theorem
    angle = round(math.degrees(math.atan2(run_y, run_x)),2)

    #if statements for weird cases
    if (magnitude==0):
        angle = 0
    if (angle<0):
        angle = angle +360
    print ("total magnitude is: " + str(magnitude), "and the angle is: " + str(angle))
    
    #check if the user wants to continue adding vectors
    while True:
        go_on = input("Do you want to add more vectors? (y/n): ")
        if go_on.lower() == ("y"):
            break
        elif go_on.lower() == "n":
            break
        else:
            print("That is not one of the options. Try again")
            