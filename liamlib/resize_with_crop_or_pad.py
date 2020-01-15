import numpy as np


def _get_start_and_end(rm, size, random=False, rng=None):
    if rng is not None:
        start = rng.randint(0, rm)
    elif random:
        start = np.random.randint(0, rm)
    else:
        start = rm // 2
    end = start + size
    return start, end


def _get_placement(size, desired_size, random=False, rng=None):
    assert size <= desired_size
    if size == desired_size:
        return 0
    # otherwise size < desired_size
    if rng is not None:        
        i = rng.randint(0, desired_size - size)
        return i
    elif random:
        return np.random.randint(0, desired_size - size)
    else:
        return (desired_size - size) // 2
    

def resize_with_crop_or_pad(im, desired_size, dtype='uint8', random=False, rng=None):
    out = np.zeros(desired_size, dtype=dtype)
    h, w = desired_size
    if h < im.shape[0]:
        rm = im.shape[0] - h
        y0, y1 = _get_start_and_end(rm, h, random, rng)
        im = im[y0:y1]
    if w < im.shape[1]:
        rm = im.shape[1] - w
        x0, x1 = _get_start_and_end(rm, w, random, rng)
        im = im[:, x0:x1]
    y0 = _get_placement(im.shape[0], h, random, rng)
    y1 = y0 + im.shape[0]
    x0 = _get_placement(im.shape[1], w, random, rng)
    x1 = x0 + im.shape[1]
    out[y0:y1, x0:x1] = im
    return out
