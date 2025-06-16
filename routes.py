from flask import Blueprint, request, jsonify
from models import Hero, Power, HeroPower
from extensions import db


routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return jsonify({"message": "POST request received at /"}), 200
    return jsonify({"message": "Welcome to the Superheroes API"}), 200

@routes.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{
        "id": h.id,
        "name": h.name,
        "super_name": h.super_name
    } for h in heroes]), 200

@routes.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [
            {
                "id": hp.id,
                "strength": hp.strength,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "power": {
                    "id": hp.power.id,
                    "name": hp.power.name,
                    "description": hp.power.description
                }
            } for hp in hero.hero_powers
        ]
    }), 200

@routes.route("/powers")
def get_powers():
    powers = Power.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description} for p in powers])

@routes.route("/powers/<int:id>")
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify({"id": power.id, "name": power.name, "description": power.description})

@routes.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({"errors": ["validation errors"]}), 400

    power.description = description
    db.session.commit()

    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })

@routes.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.get_json()
    strength = data.get("strength")
    hero_id = data.get("hero_id")
    power_id = data.get("power_id")

    if strength not in ['Strong', 'Weak', 'Average']:
        return jsonify({"errors": ["validation errors"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["validation errors"]}), 400

    hp = HeroPower(strength=strength, hero=hero, power=power)
    db.session.add(hp)
    db.session.commit()

    return jsonify({
        "id": hp.id,
        "hero_id": hp.hero_id,
        "power_id": hp.power_id,
        "strength": hp.strength,
        "hero": {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        },
        "power": {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
    }), 201
