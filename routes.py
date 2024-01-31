from flask import Blueprint, jsonify, render_template, request, url_for

from dto import DayTableDTO
from db.repositories import DayTableRepository

routes_bp = Blueprint("routes", __name__)

# data1 = [
#     ['title', 'what have done', 'time'],
#     ['cf', '- write two cycles in day', '30m'],
#     ['doTable', '- test input data', '1h'],
# ]

headers = ['title', 'what have done', 'time']


@routes_bp.route("/")
def index():
    return render_template("index.html")


@routes_bp.route("/tables")
def get_tables():
    user_id = request.args.get('user_id', type=int)
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
    for record in data['records']:
        t = DayTableDTO.model_validate(record)
        DayTableRepository.add(t)

    return ""
