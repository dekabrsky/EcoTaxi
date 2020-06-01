from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Text)
    time = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    co2 = db.Column(db.Float)
    rec_str = (str(id) + ';' + author + ';' + str(time) + ';' +
               str(latitude) + ';' + str(longitude) + ';' + str(co2))

    def __init__(self, author, lat, lon, co2):
        self.author = author
        self.latitude = lat
        self.longitude = lon
        self.co2 = co2
        self.time = datetime.now()

    def __repr__(self):
        return '<Content %s>' % self.rec_str


db.create_all()


@app.route('/')
def records_list():
    tasks = Record.query.all()
    return render_template('list.html', tasks=tasks)


@app.route('/task', methods=['POST'])
def add_refactor():
    author = request.form['author']
    lat = request.form['lat']
    lon = request.form['lon']
    co2 = request.form['co2']
    if not author or not lat or not lon or not co2:
        return 'Error'

    task = Record(author, lat, lon, co2)
    db.session.add(task)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run()
