from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

movies = {
 "results": [
      {
        "title": "Blade Runner",
        "Spaceid": "tt0083658",
        "Poster": "http://l.yimg.com/eb/ymv/us/img/hv/photo/movie_pix/warner_brothers/blade_runner/bladerunner_4discboxart.jpg"
      },
      {
        "title": "Cool Hand Luke",
        "Spaceid": "tt0061512",
        "Poster": "http://l.yimg.com/eb/ymv/us/img/hv/photo/movie_pix/warner_brothers/cool_hand_luke/coolhandluke_dvd.jpg"
      },
      {
        "title": "Heat",
        "Spaceid": "tt0113277",
        "Poster": "http://l.yimg.com/eb/ymv/us/img/hv/photo/movie_pix/paramount_pictures/clueless/heat_smallposter.jpg"
      },
      ]
}

app = Flask(__name__)
## los metodos iran luego de esta linea

@app.route("/")
def hello():
    print("verga wey")
    return json.dumps(movies)
#<int:task_id>

@app.route("/all/")
def getall():
    return json.dumps(movies)
if __name__ == "__main__":
    app.run(debug=True,port=1234)
