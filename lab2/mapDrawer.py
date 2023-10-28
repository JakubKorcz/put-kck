import colorsys

import numpy as np
from matplotlib import pyplot as plt


def main():
    data = readFile()
    drawMap(data)


def readFile():
    with open("demFiles/big.dem", "r") as file:
        data = []
        line = file.readline()
        values = line.split()
        data.append(int(values[0]))
        data.append(int(values[1]))
        data.append(int(values[2]))

        heights = []
        for line in file:
            values = line.split()
            row = [float(value) for value in values]
            heights.append(row)
        data.append(heights)
    return data


def drawMap(data):
    width_map = data[0]
    height_map = data[1]
    distance_between_points = data[2] / 100
    heights = data[3]

    min_height = np.min(heights)
    max_height = np.max(heights)

    map = np.zeros((height_map, width_map, 3))

    for i in range(height_map):
        for j in range(width_map):
            height = heights[i][j]
            if j == 0:
                color = gradient_hsv(getMapVal(min_height, max_height, height), 0)
            else:
                neigh_height = heights[i][j - 1]
                diff = neigh_height - height
                color = gradient_hsv(getMapVal(min_height, max_height, height), getTgVal(diff, distance_between_points))
            map[i][j] = color

    plt.figure(figsize=(8, 8))
    plt.imshow(map)

    plt.savefig('mapa.pdf')


def getTgVal(height, base):
    tgAlfa = height / base
    if tgAlfa > 0.25 or tgAlfa < -0.25:
        return 1
    else:
        return 4 * tgAlfa


def getMapVal(min_height, max_height, height):
    return (height - min_height) / (max_height - min_height)


def gradient_hsv(v, tga):
    if tga >= 0:
        return hsv2rgb(1 / 3 - 1 / 3 * v, 1, 1 - tga)
    else:
        return hsv2rgb(1 / 3 - 1 / 3 * v, 1 + tga, 1)


def hsv2rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s, v)


if __name__ == '__main__':
    main()
