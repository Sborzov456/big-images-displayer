# На MacOS нужно экспортировать одну переменную
import os
os.environ['DYLD_LIBRARY_PATH'] = '/opt/homebrew/lib'

import openslide
from openslide.deepzoom import DeepZoomGenerator
from openslide import OpenSlide, OpenSlideCache

def get_slide(options):
    osr = OpenSlide('/Users/sborzov/Работа/big-images-diplayer/server/svs/23-168-001.svs')
    return DeepZoomGenerator(osr, **options)
