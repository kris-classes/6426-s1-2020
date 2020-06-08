import random


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def buildHeap(arr, n):
    startIdx = n // 2 - 1

    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)


def printHeap(arr, n):
    print("List representation of Max Heap is:")

    for i in range(n):
        print(arr[i], end="\t")
    print()


if True:
    def randomList():
        listObj = [i for i in range(14)]
        random.shuffle(listObj)
        return listObj


    def userInput():
        count = 0
        listObj = []
        while count < 14:
            n = int(input('Enter Number: '))
            listObj.append(n)
            count += 1
        return listObj


    userDec = input("Type i for input or r for random: ")

    if userDec == "i":
        useList = userInput()
        print(f"Initial list is:{useList}\n")
    elif userDec == "r":
        useList = randomList()
        print(f"Initial list is:{useList}\n")

    n = len(useList)

    buildHeap(useList, n)

    printHeap(useList, n)

print("\nTree representation of Max Heap is:")

print(f"               ({useList[0]})")
print("              /    \\")
print("             /      \\")
print("            /        \\")
print("           /          \\")
print(f"         ({useList[1]})         ({useList[2]})")
print("         / \\           / \\")
print("        /   \\         /   \\")
print(f"      ({useList[3]})   ({useList[4]})     ({useList[5]})  ({useList[6]})")
print("      / \\   / \\     / \\    / \\")
print(f"    ({useList[6]})({useList[7]}) ({useList[8]})({useList[9]}) ({useList[10]})({useList[11]}) ({useList[12]})({useList[13]})")
