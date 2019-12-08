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

def draw_circle(pixels, center, radius):
    x = 0
    y = radius
    d = 3 - 2*radius

    _draw_mini_circle(pixels, center, [x, y])
    while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d += 10 + 4*(x - y)
        else:
            d += 6 + 4*x

        _draw_mini_circle(pixels, center, [x, y])

def _draw_mini_circle(pixels, center, offset):
    xc, yc = int(center[0]), int(center[1])
    x, y = int(offset[0]), int(offset[1])

    pixels[yc + y][xc + x] = 1
    pixels[yc + y][xc - x] = 1
    pixels[yc - y][xc + x] = 1
    pixels[yc - y][xc - x] = 1
    pixels[yc + x][xc + y] = 1
    pixels[yc + x][xc - y] = 1
    pixels[yc - x][xc + y] = 1
    pixels[yc - x][xc - y] = 1

def draw_ellipse(pixels, center, rx, ry):
    x = 0
    y = ry

    dx = 0
    dy = 2 * ry * rx**2

    d = ry**2 - ry * rx**2 + 1/4 * rx**2
    _draw_mini_ellipse(pixels, center, [x, y])
    while dx < dy:
        x += 1

        if d < 0:
            dx += 2 * ry**2
            d += ry**2 + dx
        else:
            y -= 1
            dx += 2 * ry**2
            dy -= 2 * rx**2
            d += dx - dy + ry**2

        _draw_mini_ellipse(pixels, center, [x, y])
        
    d = (ry**2 * (x + 1/2)**2) + (rx**2 * (y - 1)**2) - (rx**2 * ry**2)
    while y >= 0:
        y -= 1

        if d > 0:
            dy -= 2 * rx**2
            d += rx**2 - dy
        else:
            x += 1
            dx += 2 * ry**2
            dy -= 2 * rx**2
            d += dx - dy + rx**2

        _draw_mini_ellipse(pixels, center, [x, y])

def _draw_mini_ellipse(pixels, center, offset):
    xc, yc = int(center[0]), int(center[1])
    x, y = int(offset[0]), int(offset[1])
    
    pixels[yc + y][xc + x] = 1
    pixels[yc + y][xc - x] = 1
    pixels[yc - y][xc + x] = 1
    pixels[yc - y][xc - x] = 1
