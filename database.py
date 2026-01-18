from flask_sqlalchemy import SQLAlchemy 
import requests

def seed_database():

    for i in range(1, 152):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        response = requests.get(url)
        data = response.json()

        types_list = [t['type']['name'] for t in data['types']]
        types_string = ', '.join(types_list)

        new_pokemon = pokemon(
            id = data['id'],
            name = data['name'].capitalize(),
            type = types_string,
            image_url = data['sprites']['front_default'],
            ability = ', '.join([a['ability']['name'] for a in data['abilities']])

            stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
            hp = stats.get('hp', 0)
            attack = stats.get('attack', 0)
            defence = stats.get('defense', 0)
            special_attack = stats.get('special-attack', 0)
            special_defence = stats.get('special-defense', 0)
            speed = stats.get('speed', 0)
            total = sum(stats.values())
        )
        db.session.add(new_pokemon)
    db.session.commit()
db = SQLAlchemy()

class pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
    ability = db.Column(db.String(400), nullable=False)

    hp = db.column(db.integer)
    attack = db.column(db.integer)
    defence = db.column(db.integer)
    special_attack = db.column(db.integer)
    special_defence = db.column(db.integer)
    speed = db.column(db.integer)
    total = db.column(db.integer)

    def __repr__(self):
        return f"<Pokemon {self.name}>"