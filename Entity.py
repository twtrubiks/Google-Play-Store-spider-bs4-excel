from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class GooglePlay(db.Model):
    __tablename__ = 'GooglePlay'

    Id = db.Column(db.Integer, primary_key=True)
    App = db.Column(db.String(128))
    Link = db.Column(db.String(128))
    Autor= db.Column(db.String(64))
    Rate = db.Column(db.Integer)
    Download = db.Column(db.String(64))
    Publish= db.Column(db.DateTime)
    Item = db.Column(db.String(32))


if __name__ == '__main__':
    manager.run()
