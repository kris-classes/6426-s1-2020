#DSA Revision exercises

###Creating a Stack class 

```python
class Stack:
    def __init__(self):
        self.myStack = []

    def push(self, item):
        self.myStack.append(item)

    def pop(self):


    def __repr__(self):
        print("This is information for dev")
        for i in range(len(self.myStack)):
            print(str(i) + " element on Stack is  " + str(self.myStack[i]))

print("Stack Revision")
newStack = Stack()
```


##### Q1. Add a line to the pop function of the Stack class above to make it work.


##### Q2. Create a function inside the class which returns the length of the list myStack. Call the function outside the class definition and print the value.


##### Q3. Push values to the stack so that the stack looks like 
######['Hello', age, 'YourName']


##### Q4. Create a \_\_repr__ function which would print out in this format
######Hello YourName, your age is age. 
######e.g. Hello Bob, your age is 21.


##### Q5. Pop the Stack twice and push values so that when the \_\_repr__ function is called it will print out
###### Hello Mark Zuckerberg, your age is 35.


##### Q6. Create a get function inside the class which would return the value of the stack on a specific index.
###### Hint : The function takes in a index parameter and stack value of index.


##### Q7. Print the element in index 0 of the stack list using the get function
