# AVL-Tree-Visualizer
Visualization of an AVL, shows how the tree gets balanced after each insertion 

## Running the program

Running the program is very straightforward, clone the repo, and run the python file. You need to have the `tkinter` python package installed on your system.

### Windows 
### `py.exe .\AVL-GUI.py`

### Linux
### `python3 ./AVL-GUI.py`

## Coming soon
Currently if the tree get's too large, it is drawn out of the frame, I will be adding an expandable frame in the future. 

## trees.py
This file contains classes for three different types of trees:
* `Tree()` creates a binary tree that stays 'complete' through insertion
* `BST()` a binary search tree
* `AVL()` an AVL tree (a self balancing binary search tree)

All three of these tree's are initialized with a starter value. This means that there can never be a completely empty tree. In this implementation, we are only focused on inserting into the tree. 

### Example trees
Here is an example of creating a BST. After insertion `Tree()` and `BST()`  return the inserted node, so you can assign the insertion to a variable if you want a pointer to the inserted node. However, `AVL()` returns a pointer to the root node. I have done it this way because the root node can change depending on insertions and how the tree is rotated.

* BST
    ``` 
    tree = BST(11)
    a = tree.insert(10)
    tree.insert(13)
    tree.insert(12)
    tree.insert(9)
    ```

* AVL Tree
    ```
    tree = AVL(5)
    tree = tree.insert(2)
    tree = tree.insert(6) 
    ```


The tree's have some functions that allow you to fetch spefic data about them like `getHeight()`, or `isLeaf()`. Since this file isn't intended to be used directly by the user, I have left out documentation for these methods. However there is limited documentation for these methods in the code itself. 
