import noise

def generateNoiseMap(length, width):
    scale = 190
    octaves = 4
    persistence = 0.5
    lacunarity = 2.0
    map = [[noise.pnoise2(i/scale, j/scale,
        octaves=octaves,
        persistence=persistence,
        lacunarity=lacunarity,
        repeatx=length,
        repeaty=width,
        base=0
    ) for i in range(width)] for j in range(length)]
    return map

def writeCSV(data, filename):
    string = ''
    for i in data:
        for j in i:
            string += str(round(j,6)) + ','
        string = string[0:-1] # remove trailing comma
        string += '\n'
    # write to file
    file = open(filename, 'w')
    file.write(string)
    file.close()

if __name__ == '__main__':
    heightmap = generateNoiseMap(150,150)
    writeCSV(heightmap, './maps/raw/heightmap.csv')
