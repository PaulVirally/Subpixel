def put_pixel(pixels, point, value):
    try:
        pixels[int(point[1])][int(point[0])] = value
    except IndexError:
        pass

def draw_line(pixels, p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    if abs(dy) < abs(dx):
        if x1 > x2:
            _draw_line_dec(pixels, p2, p1)
        else:
            _draw_line_dec(pixels, p1, p2)
    else:
        if y1 > y2:
            _draw_line_inc(pixels, p2, p1)
        else:
            _draw_line_inc(pixels, p1, p2)

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
        put_pixel(pixels, [x, y], 1)
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
        put_pixel(pixels, [x, y], 1)
        if D > 0:
            x += x_inc
            D -= 2*dy
        D += 2*dx

def draw_rectangle(pixels, bottom_left, top_right):
    width = top_right[0] - bottom_left[0]

    bottom_right = [bottom_left[0] + width, bottom_left[1]]
    top_left = [top_right[0] - width, top_right[1]]

    draw_line(pixels, bottom_left, bottom_right)
    draw_line(pixels, bottom_right, top_right)
    draw_line(pixels, top_right, top_left)
    draw_line(pixels, top_left, bottom_left)

def draw_square(pixels, center, size):
    w, h = len(pixels[0]), len(pixels)
    center = global_to_screen(center, w, h)

    bottom_left = [center[0] - size//2, center[1] - size//2]
    top_right = [center[0] + size//2, center[1] + size//2]

    draw_rectangle(pixels, bottom_left, top_right)

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

    put_pixel(pixels, [xc + x, yc + y], 1)
    put_pixel(pixels, [xc - x, yc + y], 1)
    put_pixel(pixels, [xc + x, yc - y], 1)
    put_pixel(pixels, [xc - x, yc - y], 1)
    put_pixel(pixels, [xc + y, yc + x], 1)
    put_pixel(pixels, [xc - y, yc + x], 1)
    put_pixel(pixels, [xc + y, yc - x], 1)
    put_pixel(pixels, [xc - y, yc - x], 1)

def draw_ellipse(pixels, center, rx, ry):
    # Swap the x and y coordinates of the inputs, because it works
    center = [center[1], center[0]]
    rx, ry = ry, rx

    x = 0
    y = ry

    dx = 0
    dy = 2 * ry * rx**2

    d = ry**2 - (ry * rx**2) + (1/4 * rx**2)
    _draw_mini_ellipse(pixels, center, [x, y])
    while dx < dy:
        x += 1

        if d < 0:
            dx += 2 * ry**2
            d += dx + ry**2
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
    
    put_pixel(pixels, [yc + y, xc + x], 1)
    put_pixel(pixels, [yc + y, xc - x], 1)
    put_pixel(pixels, [yc - y, xc + x], 1)
    put_pixel(pixels, [yc - y, xc - x], 1)
