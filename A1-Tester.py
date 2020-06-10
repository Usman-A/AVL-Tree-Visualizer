import random
#Module Imports
import sys
from importlib import import_module

def CheckHeight(tree):
    if tree is None:
        return -1
    else:
        return max(CheckHeight(tree.getLeft())+1,CheckHeight(tree.getRight())+1)

def CheckAVL(tree):
    if  CheckHeight(tree) > 0:
        l = 0 if tree.getLeft() is None else CheckHeight(tree.getLeft())+1
        r = 0 if tree.getRight() is None else CheckHeight(tree.getRight())+1
        b = l-r
        if abs(b) >= 2 or b != tree.getBalanceFactor():
            print(f"balance factor is {b} and tree claims it is {tree.getBalanceFactor()}")
            printTree(tree)
            return False
        else:
            return CheckAVL(tree.getLeft()) and CheckAVL(tree.getRight())
    else:
        return True

def printTree_(tree, prefix):
    print(f"{prefix}{tree.data}")
    if tree.getLeft() is not None:
        printTree_(tree.getLeft(),prefix+"-")
    if tree.getRight() is not None:
        printTree_(tree.getRight(),prefix+"-")

def printTree(tree):
    printTree_(tree,"")

def Test(lib, seed=0, size=10, rounds=10, verbose=False):
    random.seed(a=seed)

    # Test MyTree
    flag = True
    n = random.randint(0, size)
    try:
        tree = lib.MyTree(n)
    except:
        if verbose:
            print("Error: MyTree not creatable")
        flag = False
    

    h=1
    c=2
    for i in range(1,size):
        n = random.randint(n,n*2)
        try:
            tree = tree.insert(n)
        except:
            print(c)
            if verbose:
                print("Error: Tree not insertable")
            flag = False

        tH = tree.getHeight()
        if CheckHeight(tree) != tH:
            if verbose:
                print("Error: Tree height calculation incorrect")
            flag = False

        if tH != h:
            if verbose:
                print(f"Error: Tree height incorrect: Should be {h} but is {tH}")
            flag = False
            
        if i == c:
            h+=1
            c+=(2**h)

    del(tree)
    if verbose:
        if flag:
            print("Tree test complete.")
        else:
            print("Tree test failed.")
    # Tree works
    yield flag

    flag = True
    m = size*3
    n = random.randint(size, size*2)

    try:
        bst = lib.MyBST(n)
    except:
        if verbose:
            print("Error: MyBST not creatable")
        flag = False

    try:
        bst=bst.insert(n+1)
    except:
        if verbose:
            print("Error: BST not insertable")
        flag = False


    try:
        bst=bst.insert(n-1)
    except:
        if verbose:
            print("Error: BST not insertable")
        flag = False

    if bst.getHeight() != 1 or bst.getHeight() != CheckHeight(bst):
        if verbose:
            print("Error: BST height incorrect")
        flag = False
    
    try:
        bst=bst.insert(n+2)
        bst=bst.insert(n+3)
    except:
        if verbose:
            print("Error: BST not insertable")
        flag = False

    if bst.getHeight() != 3 or bst.getHeight() != CheckHeight(bst):
        if verbose:
            print("Error: BST height incorrect.")
        flag = False
    
    

    del(bst)
    bst= lib.MyBST(n)

    a = []
    for i in range(size):
        v = random.randint(0,m)
        bst= bst.insert(v)
        if not(v in a):
            a.append(v)
        
    for i in range(size):
        if len(a) >= size:
            m*=2
        v = random.randint(0,m)
        if (v in a) != (v in bst):
            if verbose:
                print("Error: BST Search incorrect")
            flag = False
    

    del(bst)

    if verbose:
        if flag:
            print("BST test complete.")
        else:
            print("BST test failed.")
    
    yield flag #BST works
    flag = True
    n=10
    try:
        avl = lib.MyAVL(n)
    except:
        if verbose:
            print("Error: MyAVL not creatable")
        flag = False
    first = avl
    try:
        avl = avl.insert(n+6)
    except:
        if verbose:
            print("Error: AVL not insertable #1")
        flag = False
    try:
        avl = avl.insert(n+12)
    except:
        if verbose:
            print("Error: AVL not insertable #2")
        flag = False

    if not(first is avl.getLeft()):
        if verbose:
            print("Error: AVL Rotation incorrect #1")
        flag = False

    try:
        second = avl.getRight()
        second
    except:
        if verbose:
            print("Error: AVL Node lost during rotation")
        flag = False

    try:
        avl=avl.insert(8)
        avl=avl.insert(6)
    except:
        if verbose:
            print("Error: AVL Node not insertable")
        flag = False

    if not(first is avl.getLeft().getRight()):
        if verbose:
            print("Error: AVL Rotation incorrect #2")
        flag = False
    
    if verbose:
        if flag:
            print("AVL Double Rotation test complete")
        else:
            print("AVL Double Rotation test failed")
    
    yield flag # Simple rotation correct

    flag = True
    try:
        avl=avl.insert(n-3)
    except:
        if verbose:
            print("Error: AVL Node not insertable")
        flag = False

    # Force rotations
    avl = avl.insert(n-2)
    avl = avl.insert(n-1)
    avl = avl.insert(n*2+4)
    avl = avl.insert(n*2+3)
   
    if not (first is avl.getRight().getLeft().getRight()):
        if verbose:
            print("Error: AVL Rotation incorrect #3")
        flag = False
    
    if verbose:
        if flag:
            print("AVL Double Rotation test complete")
        else:
            print("AVL Double Rotation test failed")
    yield flag # Rotation test complete

    flag = True
    for i in range(0, size):
        avl = avl.insert(random.randint(0,size))

    if not CheckAVL(avl):
        if verbose:
            print("Error: AVL Property not maintained across inserts")
        flag = False

    if verbose:
        if flag:
            print("AVL Property test complete")
        else:
            print("AVL Property test failed")

    yield flag # Big test complete
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Include at least a library name as an argument.")
        exit()
    name = sys.argv[1]
    if name.startswith(".\\"):
        name = name[2:]
    if name.endswith(".py"):
        name = name[:-3]
    module=import_module(name,package=__name__)
    print(f"Testing module {name} by {module.getName()}")    
    score=0
    for i in Test(module,seed=123456, size=1000, rounds=200, verbose=True):
        if i:
            score+=1

    print(f"Test result: {score}/5")
