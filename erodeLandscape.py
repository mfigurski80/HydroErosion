import random
import viewLandscape

# Read a float csv
def readCSV(filename):
    res = []
    file = open(filename)
    for line in file.readlines():
        strings = line.strip().split(',')
        res.append([float(i) for i in strings])
    return res
# Write to a csv
def writeCSV(data, filename):
    string = ''
    for i in data:
        for j in i:
            string += str(j) + ','
        string = string[0:-1] # remove trailing comma
        string += '\n'
    # write to file
    file = open(filename, 'w')
    file.write(string)
    file.close()

def mean(list):
    # really python. u gonna make me do this...
    return sum(list)/len(list)

# Perform actual erosion operation on map
def erodeMap(map, iter=10000, carry=.5):
    for i in range(iter):

        # set up initial vars and xy positions for droplet
        x = random.randint(0,len(map)-1)
        y = random.randint(0,len(map[0])-1)

        # print(str(x) + ":" + str(y))

        for time in range(10):
            # find lowest surrounding point
            fu_x = x
            fu_y = y
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if x+i < len(map) and y+j < len(map) and map[x+i][y+j] < map[fu_x][fu_y]:
                        fu_x = x+i
                        fu_y = y+j

            ch_height = map[x][y] - map[fu_x][fu_y]
            map[x][y] -= carry * ch_height
            map[fu_x][fu_y] += carry * ch_height

            x = fu_x
            y = fu_y


    return map

if __name__ == '__main__':
    map = readCSV('map.csv')
    newmap = erodeMap(map, 50000)
    writeCSV(newmap, 'erodedmap.csv')
    viewLandscape.viewMap(newmap, 100)
