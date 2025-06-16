from extensions import db
from sqlalchemy.orm import validates

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan")
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
        }
class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', backref='power', cascade="all, delete-orphan")
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "power_id": self.power_id,
            "hero_id": self.hero_id,
            "power": self.power.to_dict()
        }
    @validates('strength')
    def validate_strength(self, key, value):
        assert value in ['Strong', 'Weak', 'Average'], "Strength must be Strong, Weak, or Average"
        return value
