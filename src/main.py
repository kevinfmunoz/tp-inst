import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return send_file('index.html')
    except FileNotFoundError:
        return "Error: El archivo 'index.html' no se encontró.", 404


def main():
    app.run(port=int(os.environ.get('PORT', 80)))


if __name__ == "__main__":
    main()

