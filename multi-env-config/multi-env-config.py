from flask import send_file, send_from_directory, safe_join, abort

app = Flask(__name__)

app.config["SERVICE_CONFIG"] = "/app/svc-config"

@app.route('/<string:env>/<string:service>/config')
def config(env, service):
    try:
        return send_from_directory(app.config["SERVICE_CONFIG"], filename="/<string:env>/<string:service>/deployment.yaml", as_attachment=True)
    except FileNotFoundError:
        abort(404)

app.run(host='localhost', port=8080)