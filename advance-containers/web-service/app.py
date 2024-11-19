# web-service/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    with open('config.txt', 'r') as file:
        message = file.read()
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
