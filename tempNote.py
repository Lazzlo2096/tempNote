# -*- coding: utf-8
from flask import Flask
from flask import render_template

import MySQLdb






app = Flask(__name__)





@app.route("/")
def index():
	return render_template("index.html")





@app.route("/list")
def list():

	# соединяемся с базой данных
	conn = MySQLdb.connect(host="localhost", user="lazzlo", passwd="password",
	 db="db_notes", charset="utf8")

	# формируем курсор
	cursor = conn.cursor()

	sql = "select * from db_notes.notes"
	cursor.execute(sql)

	rows = cursor.fetchall()

	conn.close()

	return render_template("list.html",rows = rows)

   # con = sql.connect("database.db")
   # con.row_factory = sql.Row
   
   # cur = con.cursor()
   # cur.execute("select * from students")
   
   # rows = cur.fetchall();
   # return render_template("list.html",rows = rows)



if __name__=="__main__" :
	app.run()