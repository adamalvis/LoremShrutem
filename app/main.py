from flask import Flask, render_template, send_file

from .image import PlaceholderImage

app = Flask(__name__)


@app.route('/')
def hello():
  return render_template('index.html')


@app.route('/<int:width>/<int:height>', methods=['GET',])
def get_image(width: int, height: int):
  image = PlaceholderImage()
  image.crop(width, height)
  return send_file(image.get_file(), mimetype='image/jpg')
