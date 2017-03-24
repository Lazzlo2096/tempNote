# -*- coding: utf-8
# from flask import Flask
# from flask import render_template
from flask import Flask, render_template, request
from flask import redirect, url_for

# import db_layer_mySQL as db_layer
import db_layer_SQLite as db_layer






app = Flask(__name__)





@app.route("/")
def index():
	return render_template("index.html")


@app.route("/post_note", methods=["POST","GET"])
def post_note():
	if request.method == "POST":
		
		# try:
		title = request.form["ttl"]
		note = request.form["note"]

		if note!="":

			db_layer.insert(title, note)

			msg = "Record successfully added"
			return redirect(url_for('list'))
		else:
			msg = "The note should not be empty!"
			return render_template("result.html",msg = msg)



@app.route("/list")
def list():

	sql = "select * from notes"

	rows = db_layer.f(sql)

	# print rows

	return render_template("list.html",rows = rows)

	


if __name__=="__main__" :
	# app.run()
	app.run(debug = True)