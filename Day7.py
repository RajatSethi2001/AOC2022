from utils import readFile, typeWrapper

data = readFile("input.txt")

class Node:
    def __init__(self):
        self.bytes = 0
        self.name = None
        self.parent = None
        self.subdirs = {}
    
    def bytes(self):
        return self.bytes
    
    def parent(self):
        return self.parent
    
    def name(self):
        return self.name
    
    def subdirs(self):
        return self.subdirs

tree = Node()
tree.name = "/"
curDir = tree

for line in data:
    line = line.replace("$ ", "")
    command = line.split(" ")

    if command[0] == "cd":
        if command[1] == "..":
            curDir = curDir.parent
        elif command[1] == "/":
            curDir = tree
        else:
            curDir = curDir.subdirs[command[1]]

    elif command[0] == "ls":
        pass
    elif command[0] == "dir":
        curDir.subdirs[command[1]] = Node()
        curDir.subdirs[command[1]].name = command[1]
        curDir.subdirs[command[1]].parent = curDir
    else:
        tempDir = curDir
        while tempDir.parent is not None:
            tempDir.bytes += int(command[0])
            tempDir = tempDir.parent
        tempDir.bytes += int(command[0])

nodeList = [tree]
currentSpace = tree.bytes
deleteMin = 70000000
while len(nodeList) > 0:
    node = nodeList.pop(0)
    if (70000000 - currentSpace) + node.bytes >= 30000000 and node.bytes < deleteMin:
        deleteMin = node.bytes
    for subdir in node.subdirs.values():
        nodeList.append(subdir)

print(currentSpace)
print(deleteMin)



    
