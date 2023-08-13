from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class URLmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    short = db.Column(db.String(255), nullable=False)
    visits = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/urls', methods=['GET'])
def urls():
    url_list = URLmodel.query.all()
    return render_template('urls.html',
                           urls=url_list)


@app.route('/<string:short>', methods=['GET'])
def generated(short: str):
    pass


if __name__ == '__main__':
    app.run(debug=True)