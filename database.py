# -*- coding: utf-8

import sqlite3  #pip install sqlite
#Создаёт базу данных


conn = sqlite3.connect("database.db") #If not exist then it create db

conn.execute("CREATE TABLE IF NOT EXISTS notes ("
  "id_note INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
  "title VARCHAR(45) NULL,"
  "text BLOB NOT NULL,"
  "date_of_creation DATETIME NOT NULL,"
  "date_of_removal DATETIME NULL)"
  )
print "Table created successfully";

conn.close()