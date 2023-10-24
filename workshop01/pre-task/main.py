#!/bin/python3

from flask import Flask, render_template
from waitress import serve
import random


app = Flask(__name__)


def select_phrase():
    # Randomly select from a set list of phrases
    phrase_options= [
        "Logic will get you from A to B. Imagination will take you everywhere.",
        "There are 10 kinds of people. Those who know binary and those who don't.",
        "There are two ways of constructing a software design. One way is to make it so simple that\
        there are obviously no deficiencies and the other is to make it so complicated that there\
        are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer.",
        "It is pitch dark. You are likely to be eaten by a grue."
    ]
    phrase_selected = random.choice(phrase_options)
    return phrase_selected


@app.route("/")
def index():
    phrase = select_phrase()
    return render_template("index.html", phrase=phrase)


#app.run(host="0.0.0.0", port=5001)
if __name__ == "__main__":
    serve(app, listen='*:8080')
