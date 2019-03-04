from mayavi import mlab


def viewMap(map, factor=100):
    map = [[j*factor for j in i] for i in map]
    mlab.surf(map)
    mlab.show()


if __name__ == '__main__':
    surf = []
    file = open('map.csv')
    for line in file.readlines():
        strings = line.strip().split(',')
        surf.append([float(i) for i in strings])
    viewMap(surf, 100)
