def remap(x, x_start, x_end, y_start, y_end):
    return y_start + (y_end - y_start) * ((x - x_start) / (x_end - x_start))
