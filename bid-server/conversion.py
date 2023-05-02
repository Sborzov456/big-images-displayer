# На MacOS нужно экспортировать одну переменную
import os
os.environ['DYLD_LIBRARY_PATH'] = '/opt/homebrew/lib'

from openslide.deepzoom import DeepZoomGenerator
from openslide import OpenSlide

def get_slide(path, options):
    osr = OpenSlide(path)
    return DeepZoomGenerator(osr, **options)
