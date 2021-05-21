# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

# Instancia de la aplicación de flask
app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, resources= { r"/*": {"origins": "*"} })

app.config['MONGO_URI'] = 'mongodb+srv://dev_desktop:Asd123***@cluster0.qx1q9.mongodb.net/ipark_dev?retryWrites=true&w=majority'
mongo = PyMongo(app)


# Definiciones de rutas de los blueprints
from raspberry.cameraService.camera import camera_micro_service

# Instancias del Blueprint
app.register_blueprint(camera_micro_service)

#Esto permite hacer pruebas con HTTP (Solo usar en local)
#os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

@app.route('/api')
def index():
    return 'Server on'
    

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def angular(path):
    return render_template('index.html')
