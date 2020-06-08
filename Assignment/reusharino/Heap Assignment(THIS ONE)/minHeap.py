import heapq
import random


def randomList():
    listObj = [i for i in range(15)]
    random.shuffle(listObj)
    return listObj


def userInput():
    count = 0
    listObj = []
    while count < 15:
        n = int(input('Enter Number: '))
        listObj.append(n)
        count += 1
    return listObj


def buildHeap(listObj):
    heapObj = []
    heapq.heapify(heapObj)
    for i in range(len(listObj)):
        heapq.heappush(heapObj, listObj[i])
        # print(listObj[i])
        heapq.heapify(heapObj)
        # print(heapObj)
    return heapObj


def printHeap(arr, n):
    print("List representation of Max Heap is:")

    for i in range(n):
        print(arr[i], end="\t")
    print()


userDec = input("Type i for input or r for random: ")

if userDec == "i":
    useList = userInput()
    print(f"Initial list is:{useList}\n")
    heapq.heapify(useList)
elif userDec == "r":
    useList = randomList()
    print(f"Initial list is:{useList}\n")
    useList = buildHeap(useList)

n = len(useList)

printHeap(useList, n)

print("\nTree representation of Min Heap is:")

print(f"                ({useList[0]})")
print("              /    \\")
print("             /      \\")
print("            /        \\")
print("           /          \\")
print(f"         ({useList[1]})          ({useList[2]})")
print("         / \\          / \\")
print("        /   \\        /   \\")
print(f"      ({useList[3]})   ({useList[4]})    ({useList[5]})    ({useList[6]})")
print("      / \\   / \\    / \\    / \\")
print(
    f"   ({useList[7]})({useList[8]}) ({useList[9]})({useList[10]}) ({useList[11]})({useList[12]}) ({useList[13]})({useList[14]})")
