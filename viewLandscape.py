# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
import plotly.graph_objects as go # https://plot.ly/python/3d-surface-plots/
# from mayavi import mlab

# Render map
def viewMap(map, factor=30):
    # map = [[j*factor for j in i] for i in map]
    viewMapPlotly(map)

def viewMapPlotly(map):
    fig = go.Figure(data=[go.Surface(
        z=map,
        x=[i for i in range(len(map))],
        y=[i for i in range(len(map[0]))]
    )])
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()

# def viewMapMiavi(map):
    # old mayavi code...
    # mlab.surf(map)
    # mlab.show()

# Function that reads a float csv
def readCSV(filename):
    res = []
    file = open(filename)
    for line in file.readlines():
        strings = line.strip().split(',')
        res.append([float(i) for i in strings])
    return res

if __name__ == '__main__':
    surf = readCSV('maps/raw/heightmap.csv')
    viewMap(surf)
