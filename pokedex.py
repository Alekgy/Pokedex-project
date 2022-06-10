from email.mime import image
from flask import Flask, render_template, request
import pandas as pd
import json
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField


class UserForm(FlaskForm):
    pokemon_id = StringField('Selecciona un ID.')
    submit = SubmitField('Buscar')

def cargar_datos(ruta):
    with open(ruta, "r") as ruta:
        resultado = pd.read_json(ruta)
    return resultado

def pokemon_elegido(id_pokemon):
    dict = "./datos/pokedex.json"
    pokemon = cargar_datos(dict)
    for i, row in pokemon.iterrows():
        if row["id"] == id_pokemon:
            return row
        elif row["name"] == "english":
            return row

