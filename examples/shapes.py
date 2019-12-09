import sys
sys.path.insert(0, './Subpixel')
from subpixel import array_to_pixels

import curses
import math
import graphics
import time

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

        # Draw
        graphics.draw_circle(arr, [pix_width/6, pix_height/8], min(pix_width/6, pix_height/8))
        graphics.draw_square(arr, [pix_width/2, pix_height/8], min(pix_width/6, pix_height/8))
        graphics.draw_ellipse(arr, [5*pix_width/6 - 1, pix_height/4], pix_width/12, pix_height/4)
        graphics.draw_ellipse(arr, [pix_width/3, 3*pix_height/8], pix_width/3, pix_height/8)
        graphics.draw_polygon(arr, [pix_width/3, 5*pix_height/8 + 3], min(pix_width/4, pix_height/8), 3, angle_offset=-90)
        graphics.draw_polygon(arr, [2*pix_width/3, 5*pix_height/8 + 3], min(pix_width/4, pix_height/8), 7, angle_offset=13)
        graphics.draw_rectangle(arr, [pix_width/9, pix_height - 2], [2*pix_width/9, 3*pix_height/4])
        graphics.draw_rectangle(arr, [2*pix_width/3, 5*pix_height/6], [pix_width - 2, 11*pix_height/12])
        graphics.draw_polygon(arr, [pix_width/2, 7*pix_height/8], min(pix_width/6, pix_height/8), 5, angle_offset=-18)


        # Render
        chars = array_to_pixels(arr)

        for i in range(win_height - 1):
            for j in range(win_width - 1):
                stdscr.addstr(i, j, chars[i][j])

        # Show FPS
        now = time.time()
        stdscr.addstr(0, 0, f'FPS: {int(1/(now - last_frame))}')
        last_frame = now

if __name__ == '__main__':
    curses.wrapper(main)
