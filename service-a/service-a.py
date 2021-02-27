from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello From Service A!"

app.run(host='localhost', port=3000)