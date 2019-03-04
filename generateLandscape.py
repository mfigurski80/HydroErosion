import noise

def generateNoiseMap(length, width):
    scale = 140
    octaves = 3
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

if __name__ == '__main__':
    map = generateNoiseMap(500,500)
    # print(map)
    string = ''
    for i in map:
        for j in i:
            string += str(j) + ','
        string = string[0:-1] # remove trailing comma
        string += '\n'
    # print(string)

    # write to file
    file = open('map.csv','w')
    file.write(string)
    file.close()
