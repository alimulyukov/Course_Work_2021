import math


print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03c0\u00d7 radius\u00B2 * heigth")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")
#Input 
#What inputs are needed to calculate the volume of a cylinder?
name = input("\n\tWhat is your name: ")

radius = input("\n\tInput radius (cm): ")
radius = int(radius)

height = input("\n\tInput height (cm) ")
height = int(height)
#Process 
#What foemula is used to claculate the volume of a cylinder?
#V = pi * r * r * h
volume = math.pi * radius * radius * height
volume = round(volume,2)

#Output 
#What is important about the output?
print("\n\t\tHi "+name+"!")
print("\n\t\tGive a cylinder with:")
print("\t\tRadius = "+str(radius))
print("\t\tHeight = "+str(height))
print("\t\tthe volume is: "+str(volume)+"\n")

#1) Built in constant for PI in the math module Done 
#2) Round th eoutput usind the round function in the standart library module Done
#3) Refine the output to make it "nicer" Done
#4) Esacape code Done
#    \n - new line 
#    \t - tab 
#    \u<code> - unicode 
#5) Setup special charaters Done \
