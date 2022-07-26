from flask import Flask, render_template
from config import config


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("auth/login_and_register.html")


if __name__ == "__manin__":
    app.config.from_object(config['development'])
    app.run()
