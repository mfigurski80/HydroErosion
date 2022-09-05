import plotly.graph_objects as go # https://plot.ly/python/3d-surface-plots/
from utilities import readCSV, normalizeNoiseMap, dim
from mayavi import mlab

# Render map
def viewMap(map):
    viewMapMayavi(map)

def viewMapPlotly(map):
    fig = go.Figure(data=[go.Surface(
        z=map,
        x=[i for i in range(len(map))],
        y=[i for i in range(len(map[0]))]
    )])
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()

def viewMapMayavi(map, factor=40):
    # print(sum([sum(i)/len(i) for i in map])/len(map))
    map = normalizeNoiseMap(map, 0, factor)
    # map = [[j*factor for j in i] for i in map]
    # print(sum([sum(i)/len(i) for i in map])/len(map))
    mlab.surf(map)
    mlab.show()

if __name__ == '__main__':
    surf = readCSV('./maps/processed/erodedmap.csv')
    # surf = readCSV('./maps/raw/heightmap.csv')
    viewMap(surf)
