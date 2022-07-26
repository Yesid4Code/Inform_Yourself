from flask import Flask, render_template
from config import config


app = Flask(__name__)


if __name__ == "__manin__":
    # app.run(port = 3000, debug = True)
    app.config.from_object(config['development'])
    app.run()
