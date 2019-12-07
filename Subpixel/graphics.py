import utils

def global_to_screen(point, width, height):
    return [utils.remap(point[0], -1, 1, 0, width), utils.remap(point[1], -1, 1, 0, height)]

def draw_line(pixels, p1, p2):
    w, h = len(pixels[0]), len(pixels)

    p1_scrn = global_to_screen(p1, w, h)
    p2_scrn = global_to_screen(p2, w, h)

    x1, y1 = p1_scrn
    x2, y2 = p2_scrn

    dx = x2 - x1
    dy = y2 - y1

    if abs(dy) < abs(dx):
        if x1 > x2:
            _draw_line_dec(pixels, p2_scrn, p1_scrn)
        else:
            _draw_line_dec(pixels, p1_scrn, p2_scrn)
    else:
        if y1 > y2:
            _draw_line_inc(pixels, p2_scrn, p1_scrn)
        else:
             _draw_line_inc(pixels, p1_scrn, p2_scrn)

def _draw_line_dec(pixels, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1
    y_inc = 1

    if dy < 0:
        y_inc *= -1
        dy *= -1

    D = 2*dy - dx
    y = int(y1)

    for x in range(int(x1), int(x2)+1):
        try:
            pixels[y][x] = 1
        except IndexError:
            pass
        if D > 0:
            y += y_inc
            D -= 2*dx
        D += 2*dy

def _draw_line_inc(pixels, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1
    x_inc = 1

    if dx < 0:
        x_inc *= -1
        dx *= -1

    D = 2*dx - dy
    x = int(x1)

    for y in range(int(y1), int(y2) + 1):
        try:
            pixels[y][x] = 1
        except IndexError:
            pass
        if D > 0:
            x += x_inc
            D -= 2*dy
        D += 2*dx