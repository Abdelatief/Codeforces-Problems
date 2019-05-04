# http://codeforces.com/contest/490/problem/A
n = input()
childInputList = list(map(int, input().split()))
indexList = list(enumerate(childInputList))
container = []
bigContainer = []
while len(indexList) > 0:

    for i in range(len(indexList)):
        item = indexList[i]
        if item[1] == 1:
            container.append(item)
            indexList.remove(item)
            break

    for i in range(len(indexList)):
        item = indexList[i]
        if item[1] == 2:
            container.append(item)
            indexList.remove(item)
            break

    for i in range(len(indexList)):
        item = indexList[i]
        if item[1] == 3:
            container.append(item)
            indexList.remove(item)
            break

    if len(container) == 3:
        indicies = [i + 1 for i, x in container]
        bigContainer.append(indicies)
        container.clear()
    else:
        break
print(len(bigContainer))
for item in bigContainer:
    print(item[0], item[1], item[2])