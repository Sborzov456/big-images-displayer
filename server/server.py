from flask import Flask
from flask import make_response
from flask_cors import CORS
from conversion import get_slide
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "home"

@app.route('/<path:path>.dzi')
def dzi():
    slide = get_slide({'tile_size': 254, 'overlap': 1, 'limit_bounds': True})
    resp = make_response(slide.get_dzi('png'))
    resp.mimetype = 'application/xml'
    return resp


@app.route('/<path:path>_files/<int:level>/<int:col>_<int:row>.<format>')
def tile(level, col, row, format):
    slide = get_slide({'tile_size': 254, 'overlap': 1, 'limit_bounds': True})
    format = format.lower()
    tile = slide.get_tile(level, (col, row))
    buf = BytesIO()
    tile.save(buf, format)
    resp = make_response(buf.getvalue())
    resp.mimetype = 'image/%s' % format
    return resp


if __name__ == '__main__':
    app.run(port=8000, debug=True)