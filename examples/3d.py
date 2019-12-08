import sys
sys.path.insert(0, './Subpixel')
from subpixel import array_to_pixels

import curses
import math
import graphics
import time

vertices = [[-0.5, -0.5, -0.5],
            [ 0.5, -0.5, -0.5],
            [ 0.5,  0.5, -0.5],
            [ 0.5,  0.5,  0.5],
            [ 0.5, -0.5,  0.5],
            [-0.5, -0.5,  0.5],
            [-0.5,  0.5,  0.5],
            [-0.5,  0.5, -0.5]]

#  vertices = [[-0.5, -0.5],
            #  [-0.5,  0.5],
            #  [ 0.5,  0.5],
            #  [ 0.5, -0.5]]

def rotate(vertices, angle, axis):
    #  rot_mat = [[math.cos(angle), -math.sin(angle)],
               #  [math.sin(angle),  math.cos(angle)]]
    
    c = math.cos(angle)
    s = math.sin(angle)
    x, y, z = axis

    rot_mat = [[c + x**2 * (1 - c), x*y * (1-c) - z*s, x*z * (1-c) + y*s],
               [y*x * (1-c) + z*s, c + y**2 * (1-c), y * z * (1-c) - x*s],
               [z*x * (1-c) - y*z, z*y * (1-c) + x * s, c + z**2 * (1-c)]]

    for i in range(len(vertices)):
        vertices[i] = [sum([r * v for r, v in zip(rot_mat[j], vertices[i])]) for j in range(len(rot_mat))]

def project(vertices):
    vertices_2d = []
    for vertex in vertices:
        x, y, z = vertex
        vertices_2d.append([x, y])
    return vertices_2d

def main(stdscr):
    curses.curs_set(0)

    win_height, win_width = stdscr.getmaxyx()
    pix_height = win_height*4 - win_height%4
    pix_width = win_width*2 - win_width%2

    arr = []
    for i in range(pix_height):
        row = []
        for j in range(pix_width):
            row.append(0)
        arr.append(row)

    last_frame = time.time()
    while True:
        # Clear the screen
        stdscr.refresh()
        stdscr.erase()
        for i in range(pix_height):
            for j in range(pix_width):
                arr[i][j] = 0

        # Project
        vertices_2d = project(vertices)

        # Draw
        graphics.draw_line(arr, vertices_2d[0], vertices_2d[1])
        graphics.draw_line(arr, vertices_2d[0], vertices_2d[5])
        graphics.draw_line(arr, vertices_2d[0], vertices_2d[7])
        graphics.draw_line(arr, vertices_2d[1], vertices_2d[2])
        graphics.draw_line(arr, vertices_2d[1], vertices_2d[4])
        graphics.draw_line(arr, vertices_2d[2], vertices_2d[3])
        graphics.draw_line(arr, vertices_2d[2], vertices_2d[7])
        graphics.draw_line(arr, vertices_2d[3], vertices_2d[4])
        graphics.draw_line(arr, vertices_2d[3], vertices_2d[6])
        graphics.draw_line(arr, vertices_2d[4], vertices_2d[5])
        graphics.draw_line(arr, vertices_2d[5], vertices_2d[6])
        graphics.draw_line(arr, vertices_2d[6], vertices_2d[7])

        # Render
        chars = array_to_pixels(arr)

        for i in range(win_height - 1):
            for j in range(win_width - 1):
                stdscr.addstr(i, j, chars[i][j])

        # Physics update
        #  axis = [1/math.sqrt(14), 2/math.sqrt(14), 3/math.sqrt(14)]
        axis = [2, 3, 1]
        norm = sum(map(lambda x: x**2, axis))
        axis = list([x/norm for x in axis])
        rotate(vertices, 0.03, axis)
        
        # Show FPS
        now = time.time()
        stdscr.addstr(0, 0, f'FPS: {int(1/(now - last_frame))}')
        last_frame = now

if __name__ == '__main__':
    curses.wrapper(main)
