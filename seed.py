from app import app, db 
from models import Hero, Power, HeroPower  

with app.app_context():
   
    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()

  
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")

   
    power1 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    power2 = Power(name="super strength", description="gives the wielder super-human strengths")

    
    hp1 = HeroPower(hero=hero1, power=power1, strength="Strong")
    hp2 = HeroPower(hero=hero2, power=power2, strength="Average")

 
    db.session.add_all([hero1, hero2, power1, power2, hp1, hp2])
    db.session.commit()

    print("Seed data added successfully!")
