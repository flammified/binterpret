#!/usr/bin/env python

import binterpret
import argparse

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
parser.add_argument('--binary', action='store_true', default=False, help="Print the binary data as binary")
parser.add_argument('--gui', action='store_true', default=False, help="Start the program with an GUI")

args = parser.parse_args()


if args.gui:
    gui = binterpret.GUI()
    gui.run()
    exit(1)

xblocks = args.xblocks if args.xblocks != None else DEFAULT
yblocks = args.yblocks if args.yblocks != None else DEFAULT
markx = args.markx if args.markx != None else DEFAULT
marky = args.marky if args.marky != None else DEFAULT
offsetx = args.offsetx if args.offsetx != None else 0
offsety = args.offsety if args.offsety != None else 0
marginx = args.marginx if args.marginx != None else 0
marginy = args.marginy if args.marginy != None else 0

data = binterpret.process_qr(
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
