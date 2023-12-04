from flask import Flask, render_template, request
from db.models import getALLGoods, getRangeGoods

app = Flask(__name__)

@app.route("/")
def mainPage():
  return render_template("index.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/goods", methods=["GET", "POST"])
def goods():
  if request.method =="GET":
    return render_template("goods.html", goods=getALLGoods())
  elif request.method == "POST":
    minPrice = request.form["min"]
    maxPrice = request.form["max"]
    return render_template("goods.html", goods=getRangeGoods(minPrice, maxPrice))

app.run(debug=True)

