from flask import Flask, render_template, request
import random, math

app = Flask(__name__)

@app.route("/")
def get_home():
    return render_template('contact.html')

@app.route("/sendemail", methods=["POST"])
def send_email():
    print(request.form["name"])
    return "GG"

app.run(debug=True)
# test