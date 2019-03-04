from mayavi import mlab


surf = []
file = open('map.csv')
for line in file.readlines():
    strings = line.strip().split(',')
    surf.append([float(i)*40 for i in strings])

# surf = [[1,0.5037149130366743],[2,0.5037149130366743],[3,0.5037149130366743]]
print(surf)

mlab.surf(surf)
mlab.show()
