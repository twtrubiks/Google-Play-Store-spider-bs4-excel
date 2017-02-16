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


class University(db.Model):
    __tablename__ = 'University'

    Id = db.Column(db.Integer, primary_key=True)
    County = db.Column(db.String(64))
    University = db.Column(db.String(64))


if __name__ == '__main__':
    manager.run()
