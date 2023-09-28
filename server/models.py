from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(metadata=metadata)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'))

class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    def __repr__(self):
        return f"Animal(name='{self.name}', species='{self.species}')"


class Zookeeper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    animals = db.relationship('Animal', backref='zookeeper')

    def __repr__(self):
        return f"Zookeeper(name='{self.name}', birthday='{self.birthday}')"

class Animal(db.Model):
    __tablename__ = 'animals'

class Enclosure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(50), nullable=False)
    open_to_visitors = db.Column(db.Boolean, nullable=False)
    animals = db.relationship('Animal', backref='enclosure')

    def __repr__(self):
        return f"Enclosure(environment='{self.environment}', open_to_visitors={self.open_to_visitors})"
