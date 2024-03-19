import numpy as np

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


def erodeWithDrop(map, rockmap, hydrationMap, x, y, carry):
    """Perform actual erosion operation on map"""
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
        new_x = x + d_x
        new_y = y + d_y

        # Perform droplet move
        ch_height = map[x][y] - map[new_x][new_y]  # get base delta height
        rock_mult = 1  # get multiplier due to bedrock
        if map[x][y] - carry * ch_height < rockmap[x][y]:
            rock_mult = 0.1
            rockmap[x][y] = map[x][y] - carry * ch_height * rock_mult
        map[x][y] -= carry * ch_height * rock_mult
        map[new_x][new_y] += carry * ch_height

        x = new_x
        y = new_y

        # set hydrationMap
        hydrationMap[x][y] += 1


def erodeMap(heightmap, rockmap, iterate=400, carry=0.2):
    hydrationMap = [[0] * len(row) for row in heightmap]
    for i in range(iterate):
        for x in range(len(heightmap)):
            for y in range(len(heightmap[0])):
                erodeWithDrop(heightmap, rockmap, hydrationMap, x, y, carry)

    return (heightmap, hydrationMap)


if __name__ == '__main__':
    # benchmark
    heightmap = np.random.randint(1,10,(5,5))
    rockmap = np.zeros((5,5))
    print(heightmap)
    (final, hydration) = erodeMap(heightmap, rockmap, iterate=10)
    print(hydration)
