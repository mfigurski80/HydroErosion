from mayavi import mlab

# Render map
def viewMap(map, factor=100):
    map = [[j*factor for j in i] for i in map]
    mlab.surf(map)
    mlab.show()

# Function that reads a float csv
def readCSV(filename):
    res = []
    file = open(filename)
    for line in file.readlines():
        strings = line.strip().split(',')
        res.append([float(i) for i in strings])
    return res

if __name__ == '__main__':
    surf = readCSV('map.csv')
    viewMap(surf, 100)
