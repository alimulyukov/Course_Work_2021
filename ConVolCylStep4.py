import math


print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0 \u00D7 radius\u00B2 \u00D7 height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")

file = open("data.txt","a") #w,r,a

name = input("\n\tWhat is your name: ")

radius = 1
height = 1

while (radius != 0 or height != 0):


	try: 
		radius = input("\n\tInput radius (cm): ")
		radius = int(radius)

		height = input("\n\tInput height (cm): ")
		height = int(height)
	except:
		print("\n\t\tNumeric Type Required")
		height = -1
		radius = -1
	
	if (radius >= 0 and height >= 0):

		volume = math.pi * radius * radius * height
		volume = round(volume,2)
		print("\n\t\tHi "+name+"!")
		print("\n\t\tGive a cylinder with:")
		print("\t\tRadius = "+str(radius))
		print("\t\tHeight = "+str(height))
		print("\t\tThe volume is: "+str(volume)+"\n")	
		file.write(str(volume)+"\n")
	else: 
		print("\n\t\tYou have entered an invalid value")


print("END PROGRAM")
file.close()
'''
1) User a try except structure to account for String inputs
	try:
		<try code block>
		<try code block>
		<try code block>
	except:
		<except code block>
2) Write information to file to be accessed later. 
'''
