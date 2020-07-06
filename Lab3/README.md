# Lab 3 - Implement a binary max-heap data structure.

## Task 1 - Implement a priority queue using the heapq module

Make all the tests pass and fix your code until pylint gives a 10.00/10 rating.

```shell
pytest -xv heap_priority_queue_tests.py
pylint heap_priority_queue.py
```

## Task 2 - Questions - Answer these here.


Q: What is the worst-case time complexity for push() in a naïve priority queue?
A:O(log (n))

Q: What is the worst-case time complexity for peek() in a naïve priority queue?
A:O(log (n))

Q: What is the worst-case time complexity for pop() in a naïve priority queue?
A: O(1)

A PriorityQueue can also be implemented using a Heap data structure (you are not required to implement this in this lab).

Q: What is the worst-case time complexity for push() in a heap priority queue?
A: O(log (n))

Q: What is the worst-case time complexity for peek() in a heap priority queue?
A:  O(log (n))

Q: What is the worst-case time complexity for pop() in a heap priority queue?
A: O(n)

Q: Is an array sorted from smallest to largest a min-heap?
A: yes

Q: Is an array sorted from largest to smallest a min-heap?
A: no

Q: Is an array sorted from smalest to largest a max-heap?
A: No

Q: Is an array sorted from largest to smallest a max heap?
A: Yes

