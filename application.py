from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/a", methods=['GET', 'POST'])
def sentiment():
    return render_template("sentiment.html")

@app.route("/soumettre", methods=['GET', 'POST'])
def hello():
    print('nono is the best')
    return ' '

