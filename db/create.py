import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE goods( id INTEGER PRIMARY KEY, title TEXT, price REAL, desc TEXT, img BLOB)")
cursor.execute('''
  CREATE TABLE users(
      id INTEGER PRIMARY KEY,
      login TEXT UNIQUE,
      password TEXT,
      admin INTEGER                          
  )
''')

dataGoods = [
  (1, "Солнцезащитные очки", 300.00, "Защищают от солнца","/static/img/glasses1.jpg"),
  (2, "Медицинские очки", 4000.00, "Улучшают зрение","/static/img/glasses2.jpg"),
  (3, "Компьютерные очки", 7000.00, "Защищают от синего спектра","/static/img/glasses3.jpg"),
]

# 0 - это обычный клиент сайта
# 1 - это сотрудник сайта, компании
# 2 - главный менеджер
dataUsers = [
  (1, "Олег Анатольевич", "12345678", 1),
  (2, "Владимир Центровой", "admin", 2)
]
cursor.executemany("INSERT INTO goods VALUES (?, ?, ?, ?, ?)", dataGoods)
cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", dataUsers)
connection.commit()

connection.close()