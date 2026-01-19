import sqlite3



def getPokemonById(id):
    conn = sqlite3.connect('pokedex.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    print("finding id:",id)
    query = "SELECT * FROM pokemon WHERE id = ?"
    cursor.execute(query, (id,))
    r= cursor.fetchone()

    conn.close()
    if r is not None:

        print(r)
        return r
    print("nahi mil rha bhai")
    return None


def getAllPokemon():
    conn = sqlite3.connect('pokedex.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query= "SELECT name,id FROM pokemon"
    cursor.execute(query)
    r= cursor.fetchall()
    conn.close()
    print(r)
    return r


