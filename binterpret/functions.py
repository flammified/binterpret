from PIL import Image
import sys
import traceback

def in_rect(x, y, rect):
    if x >= rect[0][0] and y>=rect[0][1] and x < rect[1][0] and y < rect[1][1]:
        return True
    return False

def string_reverse(s):
    if s == '0':
        return '1'
    return '0'

def process_qr(
                filename,
                abx, aby,
                offsetx=0, offsety=0,
                marginx=0, marginy=0,
                msizex=8, msizey=8,
                inverse=False):

    img = Image.open(filename)

    blockx = (img.size[0] - offsetx - marginy)/abx
    blocky = (img.size[1] - offsety - marginx)/aby

    binary_data = ""

    for y in range(0, aby):
        for x in range(0, abx):

            if msizex != 0 and msizey != 0:
                #The three markings in the corner
                if in_rect(x, y, [(0,0), (msizex,msizey)]):
                    continue
                if in_rect(x, y, [(abx - msizex, 0), (abx,msizey)]):
                    continue
                if in_rect(x, y, [(0,aby - msizey), (msizex,aby)]):
                    continue

            to_add = '1' if not inverse else '0'
            pixel_red = img.getpixel((offsetx + x * blockx, offsety + y * blocky))[0]
            new_data = to_add if pixel_red < 128 else string_reverse(to_add)
            binary_data += new_data

    return binary_data
