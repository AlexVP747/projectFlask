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