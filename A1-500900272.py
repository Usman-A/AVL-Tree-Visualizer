from collections import deque
import random


def getName():
    return "Asad, Usman"


class MyTree():

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

    def findDecendants(self):

        if (self == None):
            return 0
        # going to use traversal example from lecture to count the number of decendants
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

    def updateHeight(self):
        leftHeight = -1
        rightHeight = -1
        if(self.left != None):
            leftHeight = self.left.getHeight()
        if(self.right != None):
            rightHeight = self.right.getHeight()
        if (self.isLeaf()):
            # print("is leaf")
            self.height = 0
        else:
            self.height = (1 + max(leftHeight, rightHeight))
            # print(self.data, "height", self.height)

    def updateAll(self, tree):
        if (tree != None):
            # print ("updating", tree.data, self.isLeaf())
            tree.updateHeight()
            # print("PASSING                          " ,tree.parent)
            if(tree.parent == None):
                return tree
            return tree.updateAll(tree.parent)

    def isFull(self):
        if self.left != None and self.right != None:
            return True

    def isComplete(self, tree):

        if (tree == None or tree.isLeaf()):
            return True

        if (tree.isFull()):
            return tree.isComplete(tree.left) and tree.isComplete(tree.right)

        return False

    def isLeaf(self):
        # print("lil tecca", self.left, self.right)
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

        # print("inhee data:",data, "ls:",leftSize,"rs:",rightSize)

        # for adding first child
        if (totalKids == 0):
             # icnrease hieght here
            tree.left = MyTree(data, tree)
            tree.updateAll(tree)
            # print("put-left", data)
            return tree
        elif (totalKids == 1):
            tree.right = MyTree(data, tree)
            tree.updateAll(tree)
            # print("put-right", data)
            return tree

        # goal is to fill up left first

        # print("LEFT",    leftSize,leftHeight,"| RIGHT", rightSize,rightHeight)

        if (leftSize > rightSize):
            # check if left is full, if not insert somewhere
            if(tree.left.isFull()):
                tree.insert(data, tree.right)
            else:
                tree.insert(data, tree.left)
        else:
            if(leftSize == rightSize):
                tree.insert(data, tree.left)

        # print("going to return",type(tree),type(self), tree)
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


class MyBST(MyTree):
    def __init__(self, data, parent=None):
        # Initialize this node, and store data in it
        super().__init__(data, parent)

    # Insert data into the tree, descending from this node
    # Ensure that the tree remains a valid Binary Search Tree
    # Return this node after data has been inserted

    def insert(self, data, tree=None):
        if (tree == None):
            tree = self
        # print("Current Insertion: input  compareTo", data, tree.data )
        if(data < tree.data):
            if (tree.left == None):
                tree.left = MyBST(data, tree)
                # print("put-Keft", data)
                tree.updateAll(tree)
                # print("put-left", data)
                return tree
            else:
                # print("passing left")
                tree.insert(data, tree.left)
        else:
            if(tree.right == None):
                tree.right = MyBST(data, tree)
                # print("put-Right", data, "mydad", tree.data)
                tree.updateAll(tree)
                # print("put-right", data)
                return tree
            else:
                # print ("passing right")
                tree.insert(data, tree.right)
        return tree

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


class MyAVL(MyBST):
    def __init__(self, data, parent=None):
        # Initialize this node, and store data in it
        super().__init__(data, parent)
        self.insertFLag = None
        pass

    def updateTree(self):
        # i think i might need to update all balance factors and shit
        print("Noooo")

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
        pass

    # FLag is used to figure out if it is a left left case or left right
    # or the otherway around using right values
    # flag == false, means left
    # flag == right, means right
    def checkBalance(self, tree):
        # print("Balancing: ", tree)
        if (tree != None):
            bf = tree.getBalanceFactor()
            if (abs(bf) >= 2):
                # narrowing down cases, check if left or right heavy
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
    def insert(self, data, tree=None, inserted=False, final=None):
        if(data == "balance" and tree == None):
            # print("here", data)
            return final
        if (tree == None):
            tree = self
        if(not inserted):
            # print(data)
            if(data < tree.data):
                if (tree.left == None):
                    tree.left = MyAVL(data, tree)
                    flag = False
                    return tree.insert("balance", tree.left, True, flag)
                else:
                    return tree.insert(data, tree.left, False)
            else:
                if(tree.right == None):
                    tree.right = MyAVL(data, tree)
                    flag = True
                    return tree.insert("balance", tree.right, True, flag)
                else:
                    return tree.insert(data, tree.right, False)
        else:
            # We've reached the top, and now it is time to return the tree
            if(tree.parent == None):
                tree.updateHeight()
                if abs(tree.getBalanceFactor()) > 1:
                    tree.checkBalance(tree)
                return tree.insert("balance", tree.parent, True, tree)
            else:
                tree.updateHeight()
                if abs(tree.getBalanceFactor()) > 1:
                    tree.checkBalance(tree)
                return tree.insert("balance", tree.parent, True)

    def checkTree(self, tree):
        if (tree.parent != None):
            return tree.checkTree(tree.parent)
        if(tree.parent == None):
            return tree

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


# print("AVL test")
# print("------------------")
# tree = MyAVL(15)
# root = tree.insert(17)
# root = tree.insert(16)
# print(root)

# root = tree.insert(18)
# root = tree.insert(40)
# root = tree.insert(20)
# print(root)
# print("+++++++++++++++")
# # root.left.leftRotate()
# # # print(root)
# # # print(root.left)
# # root.rightRotate()
# # print(root.parent)
# # print(root.left)
# # root.leftRotate()
# # print(root.parent)
# # print(root.getHeight())
# print("------------------")
# # ##
# # left left insertion, single rotate right
# ## right right insertinon, single rotate left


# # # l = [16,22,8,6,7,8,9,24,23]

# avl = MyAVL(10)
# a = avl.insert(16)
# a = a.insert(22)

# a = a.insert(8)
# a= a.insert(6)
# # # print("root", a, "SHOULD BE none ->", a.parent )
# # # print("++++")
# # # print(a.left)

# # # a = a.insert(6)
# # # print(a, "oko")
# # print("-----------")
# a = a.insert(7)
# a = a.insert(8)
# a = a.insert(9)
# a = a.insert(24)
# a = a.insert(23)
# print(a.right.left)
# # # print("gddddddddddd")

# ##BST TEST
# tree = MyBST(15)
# a=tree.insert(10)
# b=tree.insert(13)
# c=tree.insert(9)
# tree.insert(18)
# tree.insert(16)
# tree.insert(15)
# tree.insert(8)
# tree.insert(15)
# tree = tree.insert(20)
# print(tree.left)
# print(tree)
# print(tree.right)
# print(tree.right.left)
# print(type(tree))
# # print(3 in tree)
# # tree.insert(3)
# # print(3 in tree)
# # af = tree.insert(33)
# # tta = tree.insert(33)


# print("====================---")
# print (12 in tree)


# print("sametype", type(af) == type(tta), af, "|", tta)
# # print(6 in tree)

# print(type(a) == type (b) == type(c))


# test = MyTree(10)

# a=test.insert(2)
# b=test.insert(4)

# test.insert(1)
# test.insert(9)

# test.insert(11)
# test.insert(14)
# test.insert(111)
# test.insert(222)
# test.insert(33)
# test.insert(44)
# test.insert(55)
# test.insert(66)
# test.insert(77)
# test.insert(88)

# print("complete test", test.isComplete(test))
# print(test.left.left)
# print(test.left)
# print(test.left.right)
# print(test)
# print(test.right.left)
# print(test.right)
# print(test.right.right)

# current = test.left.left
# print (a)

# print(type(a),type(b))
# print("height", test.right.getHeight())
# #testing imported queue
# test = deque()
# print(type (test))
# test.append(2)
# test.append(3)
# print(test)
# print(test.count(2))
# print(len(test), "h")
# test.append(44)
# print(len(test), "h")
