#!/usr/bin/env python

import argparse
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

def binterpret(filename,
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

if __name__ == "__main__":
    DEFAULT = 8
    parser = argparse.ArgumentParser(description='Read a QRcode as binary data')

    #Converting arguments
    parser.add_argument('filename', help="The image to interpret")
    parser.add_argument('-xblocks', type=int, help="The amount of squares in width.  Default is 8")
    parser.add_argument('-yblocks', type=int, help="The amount of squares in height. Default is 8")
    parser.add_argument('-offsetx', type=int, help="The x-offset in pixels")
    parser.add_argument('-offsety', type=int, help="The y-offset in pixels")
    parser.add_argument('-markx', type=int, help="The amount of squares of the markers in width. Default is 8.")
    parser.add_argument('-marky', type=int, help="The amount of squares of the markers in height. Default is 8.")
    parser.add_argument('-marginx', type=int, help="The margin at the right in pixels")
    parser.add_argument('-marginy', type=int, help="The margin at the bottom in pixels")
    parser.add_argument('--inverse', action='store_true', default=False, help="Inverse the binary data")

    #Flag arguments
    parser.add_argument('--ascii', action='store_true', default=False, help="Print the binary data as ascii")
        #Flag arguments
    parser.add_argument('--binary', action='store_true', default=False, help="Print the binary data as binary")

    args = parser.parse_args()

    xblocks = args.xblocks if args.xblocks != None else DEFAULT
    yblocks = args.yblocks if args.yblocks != None else DEFAULT
    markx = args.markx if args.markx != None else DEFAULT
    marky = args.marky if args.marky != None else DEFAULT
    offsetx = args.offsetx if args.offsetx != None else 0
    offsety = args.offsety if args.offsety != None else 0
    marginx = args.marginx if args.marginx != None else 0
    marginy = args.marginy if args.marginy != None else 0

    data = binterpret(
                        args.filename,
                        xblocks, yblocks,
                        offsetx, offsety,
                        marginx, marginy,
                        markx, marky,
                        args.inverse
                        )

    if args.binary:
        print data

    if args.ascii:
        d = [data[8*i:8*(i+1)] for i in range(len(data)/8)]
        d = [int(i, 2) for i in d]
        print "".join(chr(i) for i in d)
