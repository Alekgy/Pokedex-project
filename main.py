from flask import Flask, render_template, request, url_for, redirect
from pokedex import UserForm, pokemon_elegido
import json
from blog import create_post_model
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
ruta = "./pokedex.json"
app.config['SECRET_KEY'] = 'SUPER SECRETO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://exjvvilnwxwygr:cda38de61a463a46c13cbbe9214e21a8efa168b8e8ee939824b5ef94d917a1bc@ec2-54-157-16-196.compute-1.amazonaws.com:5432/d87bbc07c3e9t8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

Post = create_post_model(db)

@app.route('/')
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

@app.route('/blog')
def blog():
    posts = Post.query.order_by(Post.date.desc()).all()
    print(posts)
    return render_template('blog.html', posts=posts)

@app.route('/blog/add')
def add():
    return render_template('add.html')

@app.route('/blog/create', methods=['POST'])
def create_post():
        title = request.form.get('titulo')
        text = request.form.get('texto')
        post = Post(title=title, text=text)
        db.session.add(post)
        db.session.commit()
        return redirect('/blog')


@app.route('/blog/delete', methods=['POST'])
def delete():
    post_id = request.form.get('post_id')
    post = db.session.query(Post).filter(Post.id==post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/blog')

