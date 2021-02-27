from flask import Flask, send_file, send_from_directory, safe_join, abort

app = Flask(__name__)

@app.route('/dev/service-a/config')
def config(env, service):
    with open('./app/svc-config/dev/service-a/deployment.yaml', 'r') as f:
            return render_template('content.html', text=f.read())

app.run(host='localhost', port=8080)