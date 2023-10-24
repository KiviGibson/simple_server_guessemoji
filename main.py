from flask import Flask, request
from flask_cors import CORS
import random
list = []
app = Flask(__name__)
CORS(app)


@app.route("/get")
def func():
    num = random.randint(0, len(list)-1)
    return list[num][::2] + [num]


@app.route("/answer", methods=['POST'])
def answer():
    print(request.get_json())
    return {"isSuccess": list[int(request.get_json()["num"])][1].replace("_", " ") == request.get_json()["answer"].lower()}

with open("test.txt", encoding="utf-8") as file:
    for line in file:
        list.append(line.lower().strip().split(" "))

app.run("localhost", 25565)
