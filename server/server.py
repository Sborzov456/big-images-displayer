from flask import Flask
from flask import make_response
from flask_cors import CORS
from conversion import get_slide
from io import BytesIO
from configuration import *

app = Flask(__name__)
CORS(app)

@app.route('/<path:path>.dzi')
def dzi(path):
    slide = get_slide(BASE_DIR + path, SLIDE_CONFIG)
    response = make_response(slide.get_dzi('jpeg'))
    response.mimetype = 'application/xml'
    return response


@app.route('/<path:path>_files/<int:level>/<int:col>_<int:row>.<format>')
def tile(path, level, col, row, format):
    slide = get_slide(BASE_DIR + path, SLIDE_CONFIG)
    tile = slide.get_tile(level, (col, row))
    buf = BytesIO()
    tile.save(buf, format.lower())
    response = make_response(buf.getvalue())
    response.mimetype = 'image/%s' % format
    return response


if __name__ == '__main__':
    app.run(port=8000, debug=True)


