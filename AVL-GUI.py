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

        #Boolean stating that tree is empty
        self.empty = True

        #Storing initial coodrinate for first node
        self.x0 = self.width/2 - 20
        self.y0 = 10
        self.x1 = self.width/2 + 20
        self.y1 = 50
        self.delta = 20

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
        self.canvas.create_oval(x-r,y-r,x+r,y+r, tags = "tree")        
        self.canvas.create_text(x-6, y, anchor=W, text=data, tags = "tree")
        # print(self.avl_tree)

    def error(self):
        self.canvas.create_text(self.width/2 - 100, self.height/2, anchor=W, text="Please make sure your input is a number", tags = "tree")

    #Testing preorderTraversal code
    #Passing a tree, a boolean pos, left is false right is true
    def preOrderTrav(self,tree, pos):

        if (tree == None):
            return

        #Number of levels between initial and last, will help in calcuating the positions of he nodes
        depth = tree.getDepth()

        if (depth == 0):
            self.createNode(300,30,tree.data)
            return

        #X will be positive if going right, negative if going left
        #y will remain negative
        # scale movement by depth
        
        #create left
        if (not pos):
            self.createNode(x, tree.data)ls
        else:
            self.createNode(x,y,tree.data)
        self.preOrderTrav(tree.left, False)
        self.preOrderTrav(tree.right,True)



    def display(self):

        #Deleting previously drawn tree
        self.canvas.delete("tree")

        #Making sure user input is an integer
        try:
            userInput = int(self.userInput.get()) 

            # If this is the first entity in the tree, create the tree
            if (self.empty):
                self.avl_tree = AVL(userInput)
                self.empty = False
            # Otherwise insert in tree             
            else:
                self.avl_tree = self.avl_tree.insert(userInput)  

            # drawNode -- This should later be changed to call a drawTree function
            if (userInput == 12):
                self.preOrderTrav(self.avl_tree)   
            
            return self.createNode(300,30, userInput)
        except:
            return self.error()       




Main()