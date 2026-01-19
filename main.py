from flask import Flask, render_template
from db import getPokemonById,getAllPokemon
POKEMONS = {
    "Bulbasaur": {
        "id": "001",
        "type": "grass",
        "hp": "200"
    },
    "Charmander": {
        "id": "002",
        "type": "fire",
        "hp": "400"
    },
    "Squirtle": {
        "id": "003",
        "type": "water",
        "hp": "300"
    }
}

app=Flask(__name__)

@app.route("/")
def home():
    all = getAllPokemon()
    print("all pokemon",all)
    return render_template("index.html", pokemons=all)

@app.route("/<name>")
def check(name):
    pokemon=POKEMONS.get(name)
    if not pokemon:
        return "pokemon not found"
    return render_template("pokemon.html",name=name,pokemon=pokemon)

@app.route("/id/<int:id_n>")
def pokemonById(id_n):
    print(id_n)
    p= getPokemonById(id_n)
    if p:
        return render_template("p.html",pokemon=p)
    else:
        return "Invalid id ladke sahi dal"
if __name__ == "__main__":
    app.run(debug=True)