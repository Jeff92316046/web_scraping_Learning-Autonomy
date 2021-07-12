from flask import Flask
import json
app = Flask(__name__)


file = '5_27_1.json'

app.config['JSON_AS_ASCII'] = False

with open(file, encoding='utf-8') as fh:
    data = json.load(fh)


@app.route("/")
def anime():
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
