# Assignment 1
## Task 3: Analysis and commentary 
### Nour Alaraj

#### 1. A paragraph documenting issues you encountered in the design or implementation of your chosen data structure/algorithm.

The understanding of how Pyxel works was a little bit challenging, but with the help of the examples provided it got easier. Generating data randomly was also challenging, the code had to change so the tree would be different each time the user press “new tree”. 

#### 2. Briefly explain the strengths and weaknesses of your data structure or algorithm with respect to resource consumption. Under what conditions does it perform the best or worst?

Binary tree strength is that it filters the unnecessary data while performing operations.
Binary tree weakness is that some operations will not be good when it is not balanced.
Depth-first-search performs the worst on a binary tree when the height of the tree is O(n) in terms of memory usage.
Depth-first-search performs the best on a binary tree when the height is O(logn).
But in terms of time, it is always O(n) since we have to visit all the nodes anyway. 

#### 3. List a real-world application of your chosen data structure or algorithm.

Maze-generation, topological sorting, finding connected components, to test if a graph is bipartite and path finding.

#### 4. A sentence or two on the asymptotic worst-case time and space complexity of your chosen data structure/algorithm.

Worst and best case time is always O(n) for In-order, Pre-order, Post-order traversal on binary search tree, when we are traversing the entire tree this is because we are visiting all the nodes.
Worst case space is O(n) when the tree is not balanced this is because we have to keep track of all the nodes up to the leaf. The height of the tree is not O(logn). 

#### Bibliography:

Tree Traversals (Inorder, Preorder and Postorder) retrieved from:
 https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

Tree Traversals retrieved from:
https://en.wikipedia.org/wiki/Tree_traversal

