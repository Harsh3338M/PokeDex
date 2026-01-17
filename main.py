from flask import Flask, render_template
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
    
    return render_template("index.html", pokemons=list(POKEMONS.keys()))
@app.route("/<name>")
def check(name):
    pokemon=POKEMONS.get(name)
    if not pokemon:
        return "pokemon not found"
    return render_template("pokemon.html",name=name,pokemon=pokemon)

if __name__ == "__main__":
    app.run(debug=True)