# pokedex.py
import json

RUTA_JSON = "./pokedex.json"

def cargar_datos():
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar el JSON: {e}")
        return []

def obtener_todos_los_tipos():
    datos = cargar_datos()
    tipos_unicos = set()
    for pokemon in datos:
        for tipo in pokemon.get("type", []):
            tipos_unicos.add(tipo)
    return sorted(list(tipos_unicos))

def pokemons_por_tipo(tipo_elegido):
    datos = cargar_datos()
    lista_filtrada = []
    
    for p in datos:
        if tipo_elegido in p.get("type", []):
            # Formateamos el ID a 3 dígitos para coincidir con tus archivos de imágenes
            id_formateado = str(p["id"]).zfill(3)
            img_ruta = f"images/{id_formateado}.png"
            
            lista_filtrada.append({
                "id": p["id"],
                "name": p["name"]["english"],
                "img": img_ruta
            })
            
    return lista_filtrada

def pokemon_elegido(id_pokemon):
    datos = cargar_datos()
    for poke in datos:
        if poke["id"] == int(id_pokemon):
            return poke
    return None