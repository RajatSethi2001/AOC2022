def typeWrapper(data, type):
    for i in range(len(data)):
        data[i] = type(data[i])
    return data

def readFile(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
        return data
        