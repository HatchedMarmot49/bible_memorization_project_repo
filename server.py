from flask import Flask, render_template, jsonify, send_from_directory, json
from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

with open('config.json') as f:
    config = json.load(f)
    db_username = config['DB_USERNAME']
    db_password = config['DB_PASSWORD']
    db_host = config['DB_HOST']
    db_name = config['DB_NAME']

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

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

@app.route('/test_db')
def test_db():
    try:
        # Execute a simple SELECT query to test the connection
        result = db.session.execute(text('SELECT * FROM book'))

        # Check if the query executed successfully
        if result.fetchone():
            rows = result.fetchall()
            print(rows[0])
            return jsonify(message='Database connection successful: ' + rows[0][1])
        else:
            return jsonify(message='Database connection failed')
    except Exception as e:
        return jsonify(message=f'Database connection failed: {str(e)}')

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)