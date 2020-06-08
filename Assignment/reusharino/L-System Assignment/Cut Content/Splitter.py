n = 200


outputList = [n]

# Binary tree
def Splitter(n, output):
    branches = 1
    axioms = 1
    while n > 1:
        n = n // 2
        axioms += 1
        branches = axioms * 2

        print(axioms, branches)
        output.append([axioms, branches, n])

    return axioms, branches, output


Splitter(n, outputList)

print(outputList)
