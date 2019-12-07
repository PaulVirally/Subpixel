import math

def mask_to_pixel(mask):
    '''
    Given a mask [a, b, c, d, e, f, g, h]

    a b
    c d
    e f
    g h

    Get the pixel associated with that mask

    Example:
    mask([1, 0, 0, 1, 1, 0, 0, 1])
    The mask looks like this:
    
    1 0
    0 1
    1 0
    0 1

    The output is:
    ⢕
    '''
    # Convert the mask to this mask
    # a' d'
    # b' e'
    # c' f'
    # g' h'
    braille_mask = [mask[0], mask[2], mask[4], mask[1], mask[3], mask[5], mask[6], mask[7]]
    weights = [2**x for x in range(8)]
    
    val = int(sum(m * w for m, w in zip(braille_mask, weights)))
    offset = int('2800', 16)

    return chr(offset + val)

def array_to_pixels(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])

    # Initialize masks filled with 0s
    masks = []
    for i in range(math.ceil(num_rows/4)):
        masks_row = []
        for j in range(math.ceil(num_cols/2)):
            masks_row.append([0, 0, 0, 0, 0, 0, 0, 0])
        masks.append(masks_row)

    for i in range(num_rows):
        for j in range(num_cols):
            masks[i//4][j//2][2*(i%4) + (j%2)] = arr[i][j]

    pixels = [list(map(mask_to_pixel, row)) for row in masks]
    return pixels
