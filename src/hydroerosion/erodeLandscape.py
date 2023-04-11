#! /home/miko/python/HydroErosion/env/bin/python3

import random
from utilities import mean

#  from viewLandscape import viewMap

def getDeltaHeight(map, x, y):
    deltaHeight = []
    for i in [-1, 0, 1]:
        deltaHeight.append([])
        for j in [-1, 0, 1]:
            if (
                (x + i >= len(map))
                or (x + i < 0)
                or (y + j >= len(map[0]))
                or (y + j < 0)
            ):
                # out of bounds. make sure doesn't get picked
                deltaHeight[i + 1].append(10000)
            else:
                deltaHeight[i + 1].append(map[x + i][y + j] - map[x][y])
                if abs(i + j) == 2 and i != 0:  # weight corners less
                    deltaHeight[i + 1][j + 1] *= 0.65  # 1/sqrt(2)

    return deltaHeight


# Perform actual erosion operation on map
def erodeMap(map, rockmap, iter=400000, carry=0.15):

    hydrationMap = [[0] * len(row) for row in map]

    for i in range(iter):
        if i % 50000 == 0:
            print("Eroding Drop: " + str(i))

        # set up initial vars and xy positions for droplet
        x = random.randint(0, len(map) - 1)
        y = random.randint(0, len(map[0]) - 1)

        # print(str(x) + ":" + str(y))

        for time in range(25):  # drop lifespan = 25
            # find lowest surrounding point
            deltaHeight = getDeltaHeight(map, x, y)
            d_x = 0
            d_y = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if deltaHeight[i + 1][j + 1] < deltaHeight[d_x][d_y]:
                        d_x = i
                        d_y = j
            fu_x = x + d_x
            fu_y = y + d_y

            # Perform droplet move
            ch_height = map[x][y] - map[fu_x][fu_y]  # get base delta height
            rockMult = 1  # get multiplier due to bedrock
            if map[x][y] - carry * ch_height < rockmap[x][y]:
                rockMult = 0.1
                rockmap[x][y] = map[x][y] - carry * ch_height * rockMult
            map[x][y] -= carry * ch_height * rockMult
            map[fu_x][fu_y] += carry * ch_height

            x = fu_x
            y = fu_y

            # set hydrationMap
            hydrationMap[x][y] += 1

    return (map, hydrationMap)
