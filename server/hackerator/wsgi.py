from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
application = Flask(__name__)
bootstrap = Bootstrap(application)

@application.route("/")
def hello():
    return "Hackeratorn says no!"

@application.route("/toggle/<id>")
def toggle(id):
    return "Toggle" + id

@application.route("/status/<id>")
def status(id):
    return "status" + id


if __name__ == "__main__":
    application.run()
