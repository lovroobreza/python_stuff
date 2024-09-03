from flask import Flask
import random, math

app = Flask(__name__)

jackpot = math.ceil(random.random() * 9)

@app.route("/hello")
def getNumber_2():
    print('PRINTED')
    return f"main"

@app.route("/<int:number>")
def getNumber(number):
    print(jackpot)
    if number == jackpot:
        return f"{number} returned!!"
    else:
        return f"sucker"



app.run(debug=True)