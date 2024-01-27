from flask import Blueprint, render_template, jsonify
from flask import Flask, render_template, request

from dto import DayTableDTO
from db.repositories import DayTableRepository
from pydantic import json

routes_bp = Blueprint("routes", __name__)

data1 = [
    ['title', 'what have done', 'time'],
    ['cf', '- write two cycles in day', '30m'],
    ['doTable', '- test input data', '1h'],
]

headers = ['title', 'what have done', 'time']


@routes_bp.route("/")
def index():
    to_send = [headers]
    for line in DayTableRepository.get_all_records(1):
        to_send.append([line.title, line.done, line.time])
    return render_template("index.html", table=to_send)


@routes_bp.route("/tables/<user_id>")
def get_tables(user_id: int):
    data = DayTableRepository.get_all_records(user_id)
    response = {
        "records": []
    }
    response["records"].append(list(map(DayTableDTO.model_dump, data)))
    return jsonify(response)


# @routes_bp.route("/account/<username>", methods=["POST", "GET"])
# def account(username: str):
#     # if request.method == "POST":
#     #     print(request.form)
#     return render_template("account.html", username=username)


@routes_bp.route('/process', methods=['POST'])
def process():
    data = request.get_json()  # retrieve the data sent from JavaScript
    for line in data['records']:
        t = DayTableDTO.model_validate(line)
        DayTableRepository.add(t)

    return ""
