import sqlite3

def getALLGoods():
  connection = sqlite3.connect("base.db")
  cursor = connection.cursor()

  cursor.execute("SELECT * FROM goods")
  result = cursor.fetchall()

  connection.close()

  return result

def getRangeGoods(minPrice, maxPrice):
  connection = sqlite3.connect("base.db")
  cursor = connection.cursor()

  cursor.execute("""
      SELECT *
      FROM goods
      WHERE price > ? AND price < ?                            
""", (minPrice, maxPrice))
  result = cursor.fetchall()

  connection.close()

  return result

# Создаем функцию поиска пользователя в базе данных
def getUser(login, password):
  connection = sqlite3.connect("base.db")
  cursor = connection.cursor()

  cursor.execute("""
      SELECT *
      FROM users
      WHERE login = ? AND password = ?                                              
  """, (login, password))
  result = cursor.fetchone()

  connection.close()

  return result