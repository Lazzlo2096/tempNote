# -*- coding: utf-8
import sqlite3



def f(sql):
	# соединяемся с базой данных
	conn = sqlite3.connect("database.db")
	conn.row_factory = sqlite3.Row

	# формируем курсор
	cursor = conn.cursor()

	cursor.execute(sql)

	rows = cursor.fetchall()

	# print(rows)

	conn.close()


	# rows = [rows[s] for s in rows] #преобразование из словаря в список



	return rows

def insert(title, note):

	# print("insert function!!!!!!!!!",title, note)

	# try:
	conn = sqlite3.connect("database.db")
	cursor = conn.cursor()
	cursor.execute(
		"INSERT INTO notes (title,text,"
		"date_of_creation)"
		" VALUES (?,?, CURRENT_TIMESTAMP)", (title, note)
		)

	conn.commit()

	conn.close()

	# except Exception as e:
		# raise e
	# finally:
		# pass