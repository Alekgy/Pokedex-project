from email.mime import image
from importlib.resources import open_binary
from flask import Flask, render_template, request, url_for, redirect
import json

from pokedex import UserForm, pokemon_elegido

app = Flask(__name__)
ruta = "./datos/pokedex.json"
app.config['SECRET_KEY'] = 'SUPER SECRETO'

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/pokemon/', methods=['GET', 'POST'])
def obtener_pokemons():
    login_form = UserForm()
    if request.method == 'POST':
        id_pokemon = request.form['pokemon_id']
        

        return redirect(url_for('resultado', id_pokemon=id_pokemon))


    return render_template('pokemon.html', login_form=login_form)


@app.route('/pokemon/resultado/<int:id_pokemon>', methods=['GET', 'POST'])
def resultado(id_pokemon):
    try:
        assert int(id_pokemon), "El id debe ser un número entero"
        assert id_pokemon > 0, "El id debe ser mayor a 0"
        assert id_pokemon < 810, "El id debe ser menor a 809"
    except AssertionError as error:
        return render_template('error.html', error=error)
    pokemon_info = pokemon_elegido(id_pokemon)
    
    if id_pokemon < 10:
        id_pokemon = f"00{id_pokemon}"
    elif id_pokemon < 100:
        id_pokemon = f"0{id_pokemon}"

    
    img_poke = f"images/{id_pokemon}.png"
    return render_template('resultado.html', img_poke=img_poke, pokemon_info=pokemon_info)
