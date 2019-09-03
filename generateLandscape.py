import noise
from utilities import writeCSV, normalizeNoiseMap

def generateNoiseMap(length, width, scale=190, roughness=5, shift=2.0):
    octaves = roughness
    persistence = .5
    lacunarity = shift
    map = [[noise.pnoise2(i/scale, j/scale,
        octaves=octaves,
        persistence=persistence,
        lacunarity=lacunarity,
        repeatx=length,
        repeaty=width,
        base=0
    ) for i in range(width)] for j in range(length)]
    return map

def generateTerrainMaps(x=150, y=150):
    heightmap = normalizeNoiseMap(generateNoiseMap(x,y), 0, 1)
    rockmap = normalizeNoiseMap(generateNoiseMap(x, y, roughness=8), 0, 1)
    # for i in range(x):
    #     for j in range(y):
    #         if rockmap[i][j] > 0:
    #             rockmap[i][j] /= (2/3)
    #         if heightmap[i][j] < rockmap[i][j]:
    #             rockmap[i][j] = heightmap[i][j]
    return (heightmap, rockmap)

if __name__ == '__main__':
    heightmap, rockmap = generateTerrainMaps(300, 200)
    writeCSV(heightmap, './maps/raw/heightmap.csv')
    writeCSV(rockmap, './maps/raw/rockmap.csv')
