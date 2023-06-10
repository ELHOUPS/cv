from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route('/more')
def more():
    return render_template("more.html", title="more about !! ")
@app.route('/education')
def education():
    return render_template("education.html", title=" éducation Resume")

@app.route('/experience')
def experience():
    return render_template("experience.html", title=" éxpereience Resume")
