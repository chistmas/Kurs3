from LZW import LZW
import os

compressor = LZW('imag.png')
compressor.compress()

decompressor = LZW('CompressedFiles\\imagCompressed.lzw')
decompressor.decompress()