from app import create_app,app
from extensions import db
from models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    p1 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    db.session.add_all([h1, p1])
    db.session.commit()

    hp1 = HeroPower(strength="Strong", hero_id=h1.id, power_id=p1.id)
    db.session.add(hp1)
    db.session.commit()

    print("Seed data added successfully!")
