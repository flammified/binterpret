import sys
import traceback
import argparse
from PIL import Image

def binterpret(filename, abx, aby, offsetx, offsety):
    try:
        img = Image.open(filename)
    except IOError:
        traceback.print_exc(file=sys.stdout)
        exit(3)
    blockx = img.size[0]/abx
    blocky = img.size[1]/aby

    binary_data = ""

    for y in range(0, aby):
        for x in range(0, abx):
            new_data = '1' if img.getpixel((offsetx + x * blockx + 2, offsety + y * blocky + 2))[0] < 128 else '0'
            binary_data += new_data
    print binary_data
    #print int(binary_data,2)

if __name__ == "__main__":

    DEFAULT = 8

    parser = argparse.ArgumentParser(description='Read a QRcode as binary data')
    parser.add_argument('filename', help="The image to interpret")
    parser.add_argument('-xblocks', type=int, help="The amount of squares in width.  Default is 8")
    parser.add_argument('-yblocks', type=int ,help="The amount of squares in height. Default is 8")
    parser.add_argument('-offsetx', type=int ,help="The x-offset in pixels")
    parser.add_argument('-offsety', type=int ,help="The y-offset in pixels")

    args = parser.parse_args()

    xblocks = args.xblocks if args.xblocks else DEFAULT
    yblocks = args.yblocks if args.yblocks else DEFAULT
    offsetx = args.offsetx if args.offsetx else 0
    offsety = args.offsety if args.offsety else 0

    binterpret(args.filename, xblocks, yblocks, offsetx, offsety)
