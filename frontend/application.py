from flask import Flask, jsonify, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
	return render_template("login.html")	

@app.route("/login_post", methods=["POST"])
def login_post():
	print request
	print request.json
	session['user_id'] = request.json
	return '{}'

@app.route("/role")
def role():
	return render_template("role.html")

@app.route("/skills", methods=["GET", "POST"])
def skills():
	if request.method == 'GET':
		return render_template("skills.html")
	else:
		skills = request.form.getlist('skill')
		session['skills'] = skills
		return render_template("user_info.html")

@app.route("/user_info", methods=["GET", "POST"])
def user_info():
	if request.method == 'POST':
		return render_template("login.html")
	else:
		return render_template("user_info.html")

