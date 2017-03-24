# -*- coding: utf-8
import MySQLdb



def f(sql):
	# соединяемся с базой данных
	conn = MySQLdb.connect(host="localhost", user="lazzlo", passwd="password",
	 db="db_notes", charset="utf8")

	# формируем курсор
	cursor = conn.cursor()

	cursor.execute(sql)

	rows = cursor.fetchall()

	conn.close()

	return rows