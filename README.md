Binterpret
=========

Binterpret is a little tool that interprets QR codes as pure binary data instead of other formats.
A black square is a one and a white square a zero. There is an argument that reverses it.
It was made as part of an Geocaching puzzle, but I figured it was a handy tool nonetheless.

Usage
======

```
➜  binterpret git:(master) python binterpret.py -h
usage: binterpret.py [-h] [-xblocks XBLOCKS] [-yblocks YBLOCKS]
                     [-offsetx OFFSETX] [-offsety OFFSETY] [-markx MARKX]
                     [-marky MARKY] [-marginx MARGINX] [-marginy MARGINY]
                     [--inverse] [--ascii] [--binary] [--gui]
                     filename

Read a QRcode as binary data

positional arguments:
  filename          The image to interpret

optional arguments:
  -h, --help        show this help message and exit
  -xblocks XBLOCKS  The amount of squares in width. Default is 8
  -yblocks YBLOCKS  The amount of squares in height. Default is 8
  -offsetx OFFSETX  The x-offset in pixels
  -offsety OFFSETY  The y-offset in pixels
  -markx MARKX      The amount of squares of the markers in width. Default is
                    8.
  -marky MARKY      The amount of squares of the markers in height. Default is
                    8.
  -marginx MARGINX  The margin at the right in pixels
  -marginy MARGINY  The margin at the bottom in pixels
  --inverse         Inverse the binary data
  --ascii           Print the binary data as ascii
  --binary          Print the binary data as binary
  --gui             Experimental GUI mode
```
