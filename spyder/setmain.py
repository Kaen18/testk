# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 20:26:25 2022

@author: Laboratorio
"""

from flask import Flask, jsonify, request 
#llama el archivo holaPost.py y la funcion holaPost 
from holaPost import holaPost
from scrap import scrap
app = Flask(__name__)

##servicios rest 
#app.register_blueprint(productos)
#app.register_blueprint(holaPost)
#app.register_blueprint(holaPostTelegram)
app.register_blueprint(scrap)
#app.register_blueprint(holaGet)

@app.route('/', methods=['GET'])
def hello():
    return 'Favor enviarme http://192.168.2.9:5000/cliente {nrodoc:4655894}'

if __name__ == "__main__":
    
    ##192.168.2.9
    ##app.run(host = '127.0.0.1', debug = True , port = 5000)
    app.run(host = '0.0.0.0', debug = True , port = 5000)
    app.run(debug = True)
    