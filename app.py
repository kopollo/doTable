# import db
from flask import Flask, render_template, request

from cli import cli_bp
from routes import routes_bp

app = Flask(__name__)
app.register_blueprint(cli_bp)
app.register_blueprint(routes_bp)
app.config['SECRET_KEY'] = "sdddsdsd"

if __name__ == "__main__":
    app.run(debug=True)
