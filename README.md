# PNG-to-RGB565_python_script

Python Script how to convert the PNG to RGB565 format

Usage:

python png2rgb565.py <image_file> <output_include_file>

e.g.
  python png2rgb565.py data\NRF52840_DK_ILI9341.png NRF52840_DK.h
  
## Default

The default byte order of RGB565 is targeted for the ILI9341 LCD display.
Thus, the swap is enabled.

```isSWAP = True

The script is same as the output file as 

https://littlevgl.com/image-to-c-array (with swap, RGB565 SWAP)

