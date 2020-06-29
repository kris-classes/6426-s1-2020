### A paragraph documenting issues you encountered in the design or implementation of your chosen data structure/algorithm.
the problem I spend the most time fixing is to keep track of the current node that are checking relative to the original list. Without searching list each time to get the index, I need to find a way to calculate which node is being check.
### Briefly explain the strengths and weaknesses of your data structure or algorithm with respect to resource consumption. Under what conditions does it perform the best or worst?
One of the main advantages of a binary search is that the data that needs to be search are halved after each check, which mean the size of the list that searching through are halfed each time as well. But binary search can only perform in a sorted list.
### List a real-world application of your chosen data structure or algorithm.
any data base can use binary search to look for an item as long as the data base is sorted.
### A sentence or two on the asymptotic worst-case time and space complexity of your chosen data structure/algorithm.
since I implemented the binary search with recurion, the worst-case time and space complexity should be O(log n), else if the the binary search is implemented with iteration is O(1)
