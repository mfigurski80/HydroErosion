from mayavi import mlab


surf = []
file = open('map.csv')
for line in file.readlines():
    strings = line.strip().split(',')
    surf.append([float(i)*100 for i in strings])

# print(surf)

mlab.surf(surf)
mlab.show()
