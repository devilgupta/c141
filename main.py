import csv
from flask import Flask,jsonify,request
all_movies=[]
with open ("movies.csv",encoding="utf8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
liked_movies=[]
unliked_movies=[]
did_not_watch_movies=[]
app=Flask(__name__)

@app.route("/get-movie")
def get_movies():
    return jsonify({
        "data":all_movies[0],
        "status":"success"
    })
@app.route("/liked-movie",methods=["POST"])
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status":"success"
    })
@app.route("/unliked-movie",methods=["POST"])
def unliked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
        "status":"success"
    })
@app.route("/did-not-watch-movie",methods=["POST"])
def did_not_watch_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    did_not_watch_movies.append(movie)
    return jsonify({
        "status":"success"
    })

if __name__=="__main__":
    app.run()

