#!/bin/python3
# https://en.wikipedia.org/wiki/Barnsley_fern
import random, math
width, height = 2048, 1024 
screen_buf = [[0 for _ in range(width)] for _ in range(height)]

def translate_to_buffer(x, y):
    # scale then truncate to get indices, then map to screen space
    return width//2 + math.trunc(x * 200), height - (math.trunc(y * 100))


x_n, y_n = 0, 0
max_it = 1_000_000
for i in range(max_it):
    r  = random.random()
    x_n1, y_n1 = 0, 0
    if r < 0.01:
        x_n1 = 0
        y_n1 = 0.16 * y_n
    elif r < 0.86:
        x_n1 = (0.85 * x_n) + (0.04 * y_n)
        y_n1 = (-0.04 * x_n) + (0.85 * y_n) + 1.6

    elif r < 0.93:
        x_n1 = (0.2 * x_n) + (-0.26 * y_n)
        y_n1 = (0.23 * x_n) + (0.22 * y_n) + 1.6
        
    else:
        x_n1 = (-0.15 * x_n) + (0.28 * y_n)
        y_n1 = (0.26 * x_n) + (0.24 * y_n) + 0.44
    x_n, y_n = x_n1, y_n1
    buf_x, buf_y = translate_to_buffer(x_n, y_n)
    screen_buf[buf_y][buf_x] = 1

with open("fern.ppm", "w") as file:
    file.write("P3\n")
    file.write(f"{width} {height}\n")
    file.write("255\n")
    for i in range(height):
        for j in range(width):
            if screen_buf[i][j] == 1:
                file.write("0 255 0 ")
            else:
                file.write("255 255 255 ")
        file.write("\n")
