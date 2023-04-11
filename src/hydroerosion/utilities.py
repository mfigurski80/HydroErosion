# Utilities file


def normalizeNoiseMap(map, minV=0, maxV=1):
    curMinV = min([min(i) for i in map])
    curMaxV = max([max(i) for i in map])
    targetDiff = maxV - minV
    return [[ (i - curMinV) / (curMaxV - curMinV) * targetDiff + minV for i in row] for row in map]

def readCSV(filename):
    res = []
    file = open(filename)
    for line in file.readlines():
        strings = line.strip().split(',')
        res.append([float(i) for i in strings])
    file.close()
    return res

def writeCSV(data, filename):
    string = ''
    for i in data:
        for j in i:
            string += str(j) + ','
        string = string[0:-1] # remove trailing comma
        string += '\n'
    # write to file
    file = open(filename, 'w')
    file.write(string)
    file.close()

def mean(list):
    # really python. u gonna make me do this...
    return sum(list)/len(list)

def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])
