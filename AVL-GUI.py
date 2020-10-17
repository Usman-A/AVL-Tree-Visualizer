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
        self.width = 900
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
        self.delta = 30

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

    def error(self):
        self.canvas.create_text(self.width/2 - 100, self.height/2, anchor=W, text="Please make sure your input is a number", tags = "tree")

    #Testing preorderTraversal code
    #Tree is the tree that needs to be drawn
    #Pos is a boolean representing left or right, False is left. 
    def drawTree(self,tree,x,y,pos=None):
        #If the tree is null, exit.
        if (tree == None):
            return

        depth = tree.getDepth()

        #If it's the root node
        if (depth == 0):
            self.createNode(x,y,tree.data)
            x1 = x
            y1 = y

        #Otherwise            
        else:

            #Getting spacing between nodes, this is done using the parents tree height
            if (tree.parent.getHeight() > 0):
                height = tree.parent.getHeight() + 2
            else:
                height = 1

            if(tree.isLeaf()):
                scale = self.delta - 8
            else:
                scale = self.delta * height

            print("working on: ", tree.data, "depth|height: ", depth,"|",height,"--scale: ", scale, tree.isLeaf())


            #The new Y coordinate
            y1 = y + 2* self.delta

            #getting X coord based off of if node is parents left or right node
            if (not pos):
                x1 = x - scale
            else:
                x1 = x + scale

            print("creating: ", tree.data, "X1 is: ", x1)
            #Drawing current node    
            self.createNode(x1,y1,tree.data)

        #Recursively drawing rest of tree
        self.drawTree(tree.left,x1,y1,False)
        self.drawTree(tree.right,x1,y1,True)



    def display(self):

        #Deleting previously drawn tree
        self.canvas.delete("tree")

        #Making sure user input is an integer
        # try:
        userInput = int(self.userInput.get()) 

        # If this is the first entity in the tree, create the tree
        if (self.empty):
            self.avl_tree = AVL(userInput)
            self.empty = False
        # Otherwise insert in tree             
        else:
            self.avl_tree = self.avl_tree.insert(userInput)  
        
        print("number of kids", self.avl_tree.findDecendants(), "-------------------------------------------------------") 
        return self.drawTree(self.avl_tree,self.width/2, 30)
        # except:
        #     return self.error()       



Main()