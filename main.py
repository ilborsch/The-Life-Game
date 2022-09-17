from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)

@app.route("/")
def home():
    GameOfLife(25, 25)
    return render_template("index.html")

@app.route("/live")
def live():
    game = GameOfLife()
    if game.count:
        game.form_new_generation()
    game.count += 1
    return render_template("live.html",
                           life=game,)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

