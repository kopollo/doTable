# import db
from flask import Flask, render_template, request

from cli import cli_bp
from models_pydantic import DayTable
import db.db as db

app = Flask(__name__)
app.register_blueprint(cli_bp)
app.config['SECRET_KEY'] = "sdddsdsd"

data1 = [
    ['title', 'what have done', 'time'],
    ['cf', '- write two cycles in day', '30m'],
    ['doTable', '- test input data', '1h'],
]

data2 = [
    ['title', 'what have done', 'time'],
    ['buy naggest', '- write two cycles in day', '10m'],
    ['read', '- read 123 pages', '2h'],
]


@app.route("/")
def index():
    return render_template("index.html", table1=data1)


@app.route("/account/<username>", methods=["POST", "GET"])
def account(username: str):
    # if request.method == "POST":
    #     print(request.form)
    return render_template("account.html", username=username)


@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()  # retrieve the data sent from JavaScript
    # print()
    for line in data['records']:
        # print(json.dumps(line))
        t = DayTable.model_validate(line)
        # print(t)
        db.add(t.model_dump())
        # print(t)

    return ""
    # return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=True)
