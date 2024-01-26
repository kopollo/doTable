from flask import Blueprint, render_template
from flask import Flask, render_template, request

from models_pydantic import DayTable
import db.db as db

routes_bp = Blueprint("routes", __name__)

data1 = [
    ['title', 'what have done', 'time'],
    ['cf', '- write two cycles in day', '30m'],
    ['doTable', '- test input data', '1h'],
]

headers = ['title', 'what have done', 'time']


@routes_bp.route("/")
def index():
    data = db.get_user_table(user_id=1)
    to_send = [headers]
    for line in data:
        to_send.append([line.title, line.done, line.time])
    # print(data[0])
    return render_template("index.html", table=to_send)

# @routes_bp.route("/account/<username>", methods=["POST", "GET"])
# def account(username: str):
#     # if request.method == "POST":
#     #     print(request.form)
#     return render_template("account.html", username=username)


@routes_bp.route('/process', methods=['POST'])
def process():
    data = request.get_json()  # retrieve the data sent from JavaScript
    for line in data['records']:
        t = DayTable.model_validate(line)
        # print(t)
        db.add_table(t.model_dump())

    return ""
