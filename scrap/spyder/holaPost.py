# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 19:50:47 2022

@author: Laboratorio
"""

from flask import Blueprint, request, jsonify


holaPost = Blueprint('holaPost', __name__)

@holaPost.route('/holaPost',methods=['POST'])


#Logica

def llamarServicioSet():
    global nombre
    nombre =  request.json['nombre']
    print(nombre)
    inicializarVariables(nombre)
    
    
    salida = {'codRes': codRes, 'menRes' : menRes, 'resNombre' : resNombre, 'resApellido' : resApellido}
    return jsonify({'ParmOut': salida})

def inicializarVariables(nombre):
    global codRes, menRes, resNombre, resApellido
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    resNombre =  nombre
    resApellido = 'Acosta'

