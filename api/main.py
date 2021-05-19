from flask import Flask, jsonify, request
import csv

all_mov = []

with open('movies.csv') as f:
  reader = csv.reader(f)
  data = list(reader)
  all_mov = data[1:]
liked_mov = []
disliked_mov = []
not_watched = []

app = Flask(__name__)


@app.route('/get-movie')
def get_movie_data():
  return jsonify({
      "data": all_mov[0],
      "status": "success"
  })


@app.route('/like', methods=["POST"])
def like_movie():
  global all_mov
  movie = all_mov[0]
  all_mov = all_mov[1:]
  liked_mov.append(movie)
  return jsonify({
      "status": "success"
  })


@app.route('/dislike', methods=["POST"])
def dislike_movie():
  global all_mov
  movie = all_mov[0]
  all_mov = all_mov[1:]
  disliked_mov.append(movie)
  return jsonify({"status": "success"})


@app.route('/not-watched', methods=["POST"])
def not_watched_movie():
  global all_mov
  movie = all_mov[0]
  all_mov = all_mov[1:]
  not_watched.append(movie)
  return jsonify({"status": "success"})


if __name__ == '__main__':
  app.run()
