from collections import deque
import random


def getName():
    return "Asad, Usman"

## This class is used to create a binary tree, where there is a parent node that can have a max of 2 children.
#  The tree inserts new data in a way that it enforces that it is a full binary tree (aka 'complete' binary tree), 
#  filling the tree up from left to right
class Tree():

    #In this implementation tree's are initiated with data, we can't have an empty tree. 
    def __init__(self, data, parent=None):
        # Initialize this node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.descendents = 0
        self.parent = parent

    def getLeft(self):
        # Return the left child of this node, or None
        return self.left

    def getRight(self):
        # Return the right child of this node, or None
        return self.right

    def getData(self):
        # Return the data contained in this node
        return self.data

    ## This method is used to find the number of children that a specific node has
    def findDecendants(self):

        if (self == None):
            return 0
        queue = deque()
        queue.append(self)
        # Number of kids, set to -1 since self is going to be counted, and it shouldn't be
        count = -1
        while(len(queue) != 0):
            popped = queue.popleft()
            count += 1
            if (popped.getLeft() != None):
                queue.append(popped.getLeft())
            if (popped.getRight() != None):
                queue.append(popped.getRight())
        return count

    #This method is used to update the height of node in a tree
    def updateHeight(self):
        leftHeight = -1
        rightHeight = -1
        if(self.left != None):
            leftHeight = self.left.getHeight()
        if(self.right != None):
            rightHeight = self.right.getHeight()
        if (self.isLeaf()):
            self.height = 0
        else:
            self.height = (1 + max(leftHeight, rightHeight))

    #This updates the height of every node in the tree
    def updateAll(self, tree):
        if (tree != None):
            tree.updateHeight()
            if(tree.parent == None):
                return tree
            return tree.updateAll(tree.parent)

    #Checks if both left and right branches of a tree have data
    def isFull(self):
        if self.left != None and self.right != None:
            return True

    #Checks if the specific tree is complete or not.
    def isComplete(self, tree):
        if (tree == None or tree.isLeaf()):
            return True

        if (tree.isFull()):
            return tree.isComplete(tree.left) and tree.isComplete(tree.right)

        return False

    def isLeaf(self):
        if self.left == None and self.right == None:
            return True

    def insert(self, data, tree=None):
        # Insert data into the tree, descending from this node
        # Ensure the tree remains complete - every level is filled save for the last, and each node is as far left as possible
        # Return this node after data has been inserted

        if (tree == None):
            tree = self

        totalKids = tree.findDecendants()
        leftSize = 0
        rightSize = 0
        leftHeight = -1
        rightHeight = -1

        if (tree.left != None):
            leftSize = tree.left.findDecendants()
            leftHeight = tree.left.getHeight()

        if(tree.right != None):
            rightSize = tree.right.findDecendants()
            rightHeight = tree.right.getHeight()

        # for adding first child
        if (totalKids == 0):
            tree.left = Tree(data, tree)
            tree.updateAll(tree)
            return tree
        elif (totalKids == 1):
            tree.right = Tree(data, tree)
            tree.updateAll(tree)
            # print("put-right", data)
            return tree

        # goal is to fill up left first
        if (leftSize > rightSize):
            # check if left is full, if not insert somewhere
            if(tree.left.isFull()):
                tree.insert(data, tree.right)
            else:
                tree.insert(data, tree.left)
        else:
            if(leftSize == rightSize):
                tree.insert(data, tree.left)

        #returning the node that has been added
        return(tree)

    def __str__(self):

        l = ""
        m = ""
        r = ""

        if (self.left != None):
            l = self.left.data

        if(self.data != None):
            m = self.data

        if(self.right != None):
            r = self.right.data

        return (str(l) + " " + str(m) + " " + str(r))

    def getHeight(self):
        # Return the height of this node
        return self.height



## Creating a Binary Search Tree, this tree extends the initial tree we made above
class BST(Tree):

    #In this implementation tree's are initiated with data, we can't have an empty tree. 
    def __init__(self, data, parent=None):
        # Initialize this node, and store data in it
        super().__init__(data, parent)

    #Inserts nodes into the tree maintaing a propper order where leftNode < parentNode < rightNode
    # returns the created node
    def insert(self, data, tree=None):

        if (tree == None):
            tree = self

        #If data being inserted is smaller than parent, insert on left
        if(data < tree.data):
            #if left tree is empty, add current data and update tree's height
            if (tree.left == None):
                tree.left = BST(data, tree)
                tree.updateAll(tree)
                return tree
            #other wise keep going left
            else:
                tree.insert(data, tree.left)

        else:
            #If the right tree is empty, add the current data and update the tree's height
            if(tree.right == None):
                tree.right = BST(data, tree)
                tree.updateAll(tree)
                return tree
            #otherwise keep going down
            else:
                tree.insert(data, tree.right)

        return tree

    #This method checks if the given element is present in the tree
    def __contains__(self, data, tree=None):
        # Returns true if data is in this node or a node descending from it
        if (tree == None):
            tree = self
        if (data < tree.data):
            if (tree.left != None):
                # print("recursing here,",tree.left)
                return tree.__contains__(data, tree.left)
            return False
        elif (tree.data == data):
            return True
        else:
            if (tree.right != None):
                return tree.__contains__(data, tree.right)
            return False
        return False

    def __str__(self):
        l = ""
        m = ""
        r = ""

        if (self.left != None):
            l = self.left.data

        if(self.data != None):
            m = self.data

        if(self.right != None):
            r = self.right.data

        return (str(l) + " " + str(m) + " " + str(r))

#This AVL tree extends the previous binary search tree
# An AVL tree is a version of a binary search tree, 
# what it does is it try's to maintain a balance as elements are inserted.
# Try's to keep the tree as complete as possible, so it doesn't become too heavy 
# on the left or right side. 
class AVL(BST):
    def __init__(self, data, parent=None):
        # Initialize this node, and store data in it
        super().__init__(data, parent)
        

    # This method is used to figure out if the left branch or right branch is balanced.
    # Balance is determined by comparing the heights of the left and right branches of the tree.
    # the maximum difference in height between the two branches is 1. Otherwise the tree needs to be balanced
    # Positive means leanig towards left.
    # Negative means leaning towards right
    def getBalanceFactor(self):
        # Return the balance factor of this node
        left = -1
        right = -1
        if (self.left != None):
            left = self.left.getHeight()
        if (self.right != None):
            right = self.right.getHeight()
        return (left - right)
        

    # Using the balance factors of the tree's we can figure out what type of rotation needs to be done
    # inorder to balance the tree's. 
    def checkBalance(self, tree):
        if (tree != None):
            #Get's the tree's balance factor
            bf = tree.getBalanceFactor()
            if (abs(bf) >= 2):
                # narrowing down cases, check if left or right heavy
                # positive balance factor means leaning towards left
                if(bf > 0):
                    bal = 0
                    if (tree.left != None):
                        bal = tree.left.getBalanceFactor()
                    if(bal > 0):
                        # ROTATE RIGHT
                        tree.rightRotate()
                    if(bal < 0):
                        #DOUBLE ROTATION
                        tree.left.leftRotate()
                        tree.rightRotate()
                # negative balance factor means leaning towards right                        
                elif (bf < 0):
                    bal = 0
                    if (tree.right != None):
                        bal = tree.right.getBalanceFactor()
                    if(bal < 0):
                        tree.leftRotate()
                    if(bal > 0):
                        tree.right.rightRotate()
                        tree.leftRotate()

    # Insert data into the tree, descending from this node
    # Ensure that the tree remains a valid AVL tree
    # Return the node in this node's position after data has been inserted
    # Using the parameters 'tree'. 'inserted' and 'final' to help with the recursion later on 
    def insert(self, data, tree=None, inserted=False, final=None):
         
        #Check's if the tree is balanced after the insertion, 
        # if so, it returns the root node of the tree
        if(data == "balance" and tree == None):
            return final

        # If a tree hasn't been passed, uses self as the tree to work on.     
        if (tree == None):
            tree = self

        #Check's if the data element has been inserted, if it isn't it try's to insert it      
        if(not inserted):
            
            # If data being inserted is smaller than parent, insert on left
            if(data < tree.data):
                if (tree.left == None):
                    tree.left = AVL(data, tree)
                    #Insert the data into the tree, set data to "balance", and inserted to true
                    #so we can work on balancing the tree after the insertion
                    return tree.insert("balance", tree.left, True)
                else:
                    #Keep going left since right spot for data hasn't been found
                    return tree.insert(data, tree.left, False)
            # If data being inserted is greater than parent, insert on right                    
            else:
                if(tree.right == None):
                    tree.right = AVL(data, tree)
                    return tree.insert("balance", tree.right, True)
                else:
                    return tree.insert(data, tree.right, False)
                    
        # Data has been inserted, now we have to check if the AVL balance is being maintained                    
        else:
            #Update the height after insertion of new data
            tree.updateHeight()                        

            #Checks if current node is the root of the tree
            if(tree.parent == None):
                #check if the tree is balanced, if it isn't balance it, then return root node
                if abs(tree.getBalanceFactor()) > 1:
                    tree.checkBalance(tree)
                #Note this return statement is being given data for the 'final' parameter
                # up above we have a statement that terminates the rescursion if a final is not null                    
                return tree.insert("balance", tree.parent, True, tree)
            else:
                #check if the tree is balanced, if it isn't balance it, then call function on parent                
                if abs(tree.getBalanceFactor()) > 1:
                    tree.checkBalance(tree)
                return tree.insert("balance", tree.parent, True)

    # Rotating a tree to the left
    def leftRotate(self):

        parent = self.parent
        current = self

        newTop = current.right
        # setting old Top's right node to as the old left node
        if (newTop != None):
            temp = newTop.left
            if(temp != None):
                temp.parent = current
            current.right = temp
        # linked the nodes
            current.parent = newTop
            newTop.left = current
            newTop.parent = parent

            if (parent != None):
                if (parent.right == current):
                    parent.right = newTop
                elif (parent.left == current):
                    parent.left = newTop

            current.updateAll(current)

    # Rotating a tree to the Right
    def rightRotate(self):

        parent = self.parent
        current = self

        newTop = current.left
        # setting old Top's left node to as the old right node
        if (newTop != None):
            temp = newTop.right
            if (temp != None):
                temp.parent = current
            current.left = temp
            current.parent = newTop
            newTop.right = current
            newTop.parent = parent

            if (parent != None):
                if (parent.left == current):
                    parent.left = newTop
                elif (parent.right == current):
                    parent.right = newTop

            current.updateAll(current)

