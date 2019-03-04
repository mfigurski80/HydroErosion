
def generateNoiseMap(height, width, smooth=10):
    def Noise(x, y):
        n = x + y * 57
        n = (n<<13) ^ n
        return ( 1.0 - ( (n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0)

    def Smooth_Noise(x, y, smooth = 5 ):
        corners = (Noise(x - 1, y - 1) + Noise(x + 1, y - 1) + Noise(x - 1, y + 1) + Noise(x + 1, y + 1) ) / 16
        sides   = (Noise(x - 1, y) + Noise(x + 1, y) + Noise(x, y - 1)  + Noise(x, y + 1) ) /  8
        center  =  Noise(x, y) / 4
        return corners + sides + center

    map = [[(Smooth_Noise(x,y,smooth)+1)/2 for y in range(width)] for x in range(height)]
    return map

if __name__ == '__main__':
    map = generateNoiseMap(200,200)
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
