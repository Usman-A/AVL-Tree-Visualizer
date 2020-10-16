# Importing tkinter for gui
from tkinter import * 
# Importing AVL Tree from my trees file
from trees import *

class Main:
    def __init__(self):
        #Creating a window
        window = Tk() 

        #Adding a title to the window, and setting attributes
        window.title("AVL Tree")
        self.width = 600
        self.height = 600
        self.canvas = Canvas(window, width = self.width, height = self.height,bg="white")
        self.canvas.pack()

        # Creating a window and adding labels
        frame1 = Frame(window)
        frame1.pack()

        #Creating I/O for inserting into the AVL tree.
        Label(frame1, text = "Enter a value:").pack(side = LEFT,padx=10)
        self.userInput = StringVar()

        #Creating a button to take value
        Entry(frame1, textvariable = self.userInput, justify = RIGHT).pack(side = LEFT, padx=20)
        Button(frame1, text = "Insert", command = self.display).pack(side = RIGHT)

        window.mainloop() 

    #Creating a node from user input
    #draws a circle with a number in it
    def createNode(self,x,y,data):
        r = 20
        self.canvas.create_oval(x-r,y-r,x+r,y+r)
        self.canvas.create_text(x-6, y, anchor=W, text=data, tags = "tree")

    def display(self):
        #Deleting previous tree
        self.canvas.delete("tree")
        userInput = (self.userInput.get()) 
        return self.createNode(300,30, userInput)


Main()