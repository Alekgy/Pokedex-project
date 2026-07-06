from flask import Flask, render_template, request, url_for, redirect
from pokedex import obtener_todos_los_tipos, pokemons_por_tipo, pokemon_elegido

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPER SECRETO'

@app.route('/', methods=['GET', 'POST'])
@app.route('/pokemon/', methods=['GET', 'POST'])
def obtener_pokemons():
    if request.method == 'POST':
        busqueda = request.form.get('busqueda_pokemon', '').strip()
        
        if not busqueda:
            return redirect(url_for('obtener_pokemons'))
        
        from pokedex import cargar_datos
        datos_pokemon = cargar_datos()
        
        id_encontrado = None
        
        # CASO 1: El usuario escribió un ID (ej: "4" o "004")
        if busqueda.isdigit():
            id_buscado = int(busqueda)
            for poke in datos_pokemon:
                if poke["id"] == id_buscado:
                    id_encontrado = poke["id"]
                    break
                    
        else:
            nombre_buscado = busqueda.lower()
            for poke in datos_pokemon:
                # poke["name"] es un diccionario con: {'english': '...', 'japanese': '...', etc.}
                # Recorremos todos los valores de ese diccionario de nombres
                for idioma, nombre_en_idioma in poke["name"].items():
                    if nombre_en_idioma.lower() == nombre_buscado:
                        id_encontrado = poke["id"]
                        break
                if id_encontrado:
                    break
        
        # Si encontramos el Pokémon, redirigimos a su vista de resultado
        if id_encontrado:
            return redirect(url_for('resultado', id_pokemon=id_encontrado))
        else:
            # Si no existe, mandamos a la pantalla de error que ya tienes configurada
            return render_template('error.html', error=f"No se encontró ningún Pokémon con el término: '{busqueda}'")

    # Si es una petición GET normal, muestra los tipos como antes
    tipos = obtener_todos_los_tipos()
    return render_template('pokemon.html', tipos=tipos)

# Ruta para la lista de Pokémon filtrada por el tipo seleccionado
@app.route('/pokemon/tipo/<string:tipo_elegido>')
def lista_por_tipo(tipo_elegido):
    lista_pokes = pokemons_por_tipo(tipo_elegido)
    
    # También necesitamos el JSON aquí para saber los tipos secundarios de cada Pokémon en la lista
    from pokedex import cargar_datos
    datos = cargar_datos()
    
    # Creamos un mapeo rápido de ID -> lista de tipos en minúsculas
    mapa_tipos = {p["id"]: [t.lower() for t in p["type"]] for p in datos}
    
    for poke in lista_pokes:
        poke["tipos_clase"] = mapa_tipos.get(poke["id"], [])
        
    return render_template(
        'lista_tipo.html', 
        tipo=tipo_elegido, 
        pokemons=lista_pokes, 
        tipo_clase=tipo_elegido.lower()
    )

# Ruta del resultado (Muestra la info detallada del Pokémon elegido)
@app.route('/pokemon/resultado/<int:id_pokemon>')
def resultado(id_pokemon):
    if id_pokemon <= 0 or id_pokemon > 809:
        return render_template('error.html', error="ID de Pokémon inválido")
        
    pokemon_info = pokemon_elegido(id_pokemon)
    if not pokemon_info:
        return render_template('error.html', error="Pokémon no encontrado")
    
    # Extraemos los tipos en minúsculas para usarlos como clases de CSS
    tipos_clase = [t.lower() for t in pokemon_info.get("type", [])]
    
    # Formatear ID a 3 dígitos para la imagen
    id_formateado = str(id_pokemon).zfill(3)
    img_poke = f"images/{id_formateado}.png"
    
    return render_template(
        'resultado.html', 
        img_poke=img_poke, 
        pokemon_info=pokemon_info, 
        tipos_clase=tipos_clase
    )

if __name__ == '__main__':
    app.run(debug=True)