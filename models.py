from app import db
from sqlalchemy.orm import validates

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan")


class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', backref='power', cascade="all, delete-orphan")


class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'))

    @validates('strength')
    def validate_strength(self, key, value):
        assert value in ['Strong', 'Weak', 'Average'], "Strength must be Strong, Weak, or Average"
        return value
