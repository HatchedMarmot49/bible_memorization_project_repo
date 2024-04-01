from flask import Flask, render_template, jsonify, send_from_directory, json


app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "Luke"
    return render_template("index.html", name=name)

@app.route("/verses.html")
def verses():
    f = open("mock_db.json", "r")
    db = json.load(f)
    return render_template("verses.html", db=db)

@app.route("/memorize.html")
def memorize():
    return render_template("memorize.html")

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)