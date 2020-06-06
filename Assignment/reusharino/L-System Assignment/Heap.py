import heapq
import random

def randomList():
    listObj = [i for i in range(10)]
    random.shuffle(listObj)
    return listObj


def userInput():
    count = 0
    listObj = []
    while count < 10:
        n = int(input('Enter Number: '))
        listObj.append(n)
        count += 1
    return listObj


userDec = input("Type i for input or r for random: ")

if userDec == "i":
    useList = userInput()
elif userDec == "r":
    useList = randomList()


print(useList)
heapq.heapify(useList)
print(useList)
