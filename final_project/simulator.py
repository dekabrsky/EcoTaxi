from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from final_project.app import Record
import random

app_client = Flask(__name__)
app_client.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app_client.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app_client)

authors = ['Audi 90', 'Mercedes S600', 'Kia Rio', 'VW Polo']


def main():
    for i in range(100):
        author = authors[random.randint(0, 3)]
        lat = random.uniform(50, 60)
        lon = random.uniform(50, 60)
        co2 = random.uniform(0.5, 0.9)

        task = Record(author, lat, lon, co2)
        db.session.add(task)
        db.session.commit()


if __name__ == '__main__':
    main()
