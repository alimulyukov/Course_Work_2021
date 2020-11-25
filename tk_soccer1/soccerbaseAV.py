import tkinter as tk
import webbrowser

def learnMoreEPL(*args):

	#Code block of a function
	print("learnMore")
	webbrowser.open("https://www.premierleague.com/matchweek/5672/blog")


def learnMoreSeriaA(*args):

	#Code block of a function
	print("learnMore")
	webbrowser.open("http://www.legaseriea.it/en/")

def search(*args):
	print("search")
	x = searchBar.get()
	print(x)

def currentteamspositions(*args):

	print("EPL Table")
	webbrowser.open("https://www.premierleague.com/tables")

root = tk.Tk()


labelSearchBar = tk.Label(root, text = "More information on teams")
searchBar = tk.Entry(root,width = 30)

display1 = tk.Label(root,text = "EPL.jpg")

btn1 = tk.Button(root,text = "LEARN MORE - EPL",command = learnMoreEPL)
btn2 = tk.Button(root,text = "Current team's positions",command = currentteamspositions)

display = tk.Text(root,width = 30, height = 10)

display.config(state = tk.DISABLED)

labelSearchBar.grid(row = 0, column = 0, columnspan = 2)
searchBar.grid(row = 1, column = 0, columnspan = 2)
display1.grid(row = 2, column = 0, columnspan = 2)
btn1.grid(row = 3, column = 0, columnspan = 2)
btn2.grid(row =4, column = 0, columnspan = 2)


root.bind("<Return>",search)
root.mainloop() 
print("End Program")