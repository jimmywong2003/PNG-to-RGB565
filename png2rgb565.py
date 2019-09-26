#!/usr/bin/python

import sys
import os

from PIL import Image
from PIL import ImageDraw

#isSWAP = False
isSWAP = True

def main():

    len_argument = len(sys.argv)
    filesize = 0
    if (len_argument != 3):
      print ("")
      print ("Correct Usage:")
      print ("\tpython png2rgb565.py <png_file> <include_file>")
      print ("")
      sys.exit(0)

    try:
        im=Image.open(sys.argv[1])
        #print ("/* Image Width:%d Height:%d */" % (im.size[0], im.size[1]))
    except:
        print ("Fail to open png file ", sys.argv[1])
        sys.exit(0)

    image_height = im.size[1]
    image_width = im.size[0]

    try:
        outfile = open(sys.argv[2],"w")
    except:
        print ("Can't write the file %s" % sys.argv[2])
        sys.exit(0)

    print ("/* Image Width:%d Height:%d */" % (im.size[0], im.size[1]), file=outfile)
    print ("const static uint16_t image[] = {", file=outfile)

    pix = im.load()  #load pixel array
    for h in range(image_height):
        for w in range(image_width):
            if ((h * 16 + w) % 16 == 0):
                print (" ", file=outfile)
                print ("\t\t", file=outfile, end = '')

            if w < im.size[0]:
                R=pix[w,h][0]>>3
                G=pix[w,h][1]>>2
                B=pix[w,h][2]>>3

                rgb = (R<<11) | (G<<5) | B

                if (isSWAP == True):
                    swap_string_low = rgb >> 8
                    swap_string_high = (rgb & 0x00FF) << 8
                    swap_string = swap_string_low | swap_string_high
                    print ("0x%04x," %(swap_string), file=outfile, end = '')
                else:
                    print ("0x%04x," %(rgb), file=outfile, end = '')
            else:
                rgb = 0
        #
    print ("", file=outfile)
    print ("};", file=outfile)

    outfile.close()

    print ("PNG file \"%s\"" % sys.argv[1], "converted to \"%s\"" % sys.argv[2])

if __name__=="__main__":
  main()
