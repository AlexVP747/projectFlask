from flask import Flask, render_template, request, session, redirect
from db.models import getALLGoods, getRangeGoods, getUser, addGoods, deleteGoods
from os import path
import json

app = Flask(__name__)
app.secret_key = "secret key"

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

@app.route("/admin", methods=["GET", "POST"])
def adminPage():
  # Перенаправление пользователя, если он не зарегистрирован
  if "login" not in session:
    return redirect("/admin/login")
  
  if request.method == "GET":
    return render_template("admin.html", login=session["login"], goods=getALLGoods())
  elif request.method == "POST":
    idGoods = request.form["id"]
    title = request.form["title"]
    price = request.form["price"]
    desc = request.form["desc"]

    photo = request.files["photo"]

    absPath = path.join("static", "apploads", photo.filename)

    addGoods(idGoods, title, price, desc, absPath)
    photo.save(absPath)

    return render_template("admin.html", login=session["login"], goods=getALLGoods())

@app.route("/admin/login", methods=["GET", "POST"])
def adminLoginPage():
  if request.method == "GET":
    return render_template("adminLogin.html")
  elif request.method == "POST":
    login = request.form["login"]
    password = request.form["password"]

    user = getUser(login, password)

    if user:
      session["login"] = user[1]
      return redirect("/admin")
    else:
      return render_template("adminLogin.html", error="Логин или пароль введены неправильно")

@app.route("/deleteGoods", methods=["POST"])
def apiDeleteGoods():
    id = request.json
    deleteGoods(int(id))
    return json.dumps(getALLGoods())

app.run(debug=True)

