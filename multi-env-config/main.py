from flask import send_from_directory, abort
from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/dev/service-a/config')
def configDevA():
    try:
        return send_from_directory('./svc-config/dev/service-a/', filename='dev-deployment.yaml')
    except FileNotFoundError:
        abort(404)


@app.route('/dev/service-b/config')
def configDevB():
    try:
        return send_from_directory('./svc-config/dev/service-b/', filename='dev-deployment.yaml')
    except FileNotFoundError:
        abort(404)


@app.route('/prod/service-a/config')
def configProdA():
    try:
        return send_from_directory('./svc-config/prod/service-a/', filename='prod-deployment.yaml')
    except FileNotFoundError:
        abort(404)


@app.route('/prod/service-b/config')
def configProdB():
    try:
        return send_from_directory('./svc-config/prod/service-a/', filename='prod-deployment.yaml')
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='localhost', debug=True, port=80)
