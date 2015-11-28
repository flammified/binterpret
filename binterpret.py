import sys
import traceback
import argparse
from PIL import Image

def binterpret(filename, abx, aby):
    try:
        img = Image.open(filename)
    except IOError:
        traceback.print_exc(file=sys.stdout)
        exit(3)
    blockx = img.size[0]/abx
    blocky = img.size[1]/aby
    print blockx, blocky

if __name__ == "__main__":

    DEFAULT = 8

    parser = argparse.ArgumentParser(description='Read a QRcode as binary data')
    parser.add_argument('filename', help="The image to interpret")
    parser.add_argument('-xblocks',   help="The amount of squares in width.  Default is 8")
    parser.add_argument('-yblocks',  help="The amount of squares in height. Default is 8")

    args = parser.parse_args()

    xblocks = args.xblocks if args.xblocks else DEFAULT
    yblocks = args.yblocks if args.yblocks else DEFAULT

    binterpret(args.filename, xblocks, yblocks)
