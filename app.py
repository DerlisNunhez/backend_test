from flask import Flask, request, render_template
import requests 

app = Flask(__name__)

#URL de la api
API_URL = 'https://rickandmortyapi.com/api/character'

@app.route("/")
def index():
    #request que envia el usuario desde el html
    page = request.args.get('page',1)

    name = request.args.get('name')

    if name:
        response = request.get(API_URL, params ={'name': name})

        if response != 200:
            return render_template('index.html', characters=[], search=True, error_message='Personaje no encontrado')
    #requests a la api
    response = requests.get(API_URL, params={'page' : page})
    
    data = response.json()
    
    return render_template('index.html',characters=data['results'], info=data['info'], page=int(page), search=False)