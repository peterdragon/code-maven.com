from flask import Flask, abort
import datetime

app = Flask(__name__)

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "Some general exception", 500


@app.errorhandler(ZeroDivisionError)
def server_error(err):
    app.logger.exception(err)
    return "Cannot divide by 0", 500


@app.route("/")
def main():
    app.logger.info("main route")
    return "Hello " + str(datetime.datetime.now())

@app.route("/crash")
def crash():
    app.logger.info("crash route")
    raise Exception("just crash")

@app.route("/calc")
def calc():
    app.logger.info("calc route")
    a = 0
    b = 3 / a
