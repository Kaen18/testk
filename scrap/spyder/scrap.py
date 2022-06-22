# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 18:59:15 2022

@author: Kaen

{
    "nombre":"Kevin Acosta",
    "numtel":"59598566482",
    "canal":"",
    "detalle":{
        "":""
    }
}

NIS:2314468
"""
from flask import Blueprint, request, jsonify
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime


import time

# Utilitarios para sistema operativo

import os, signal
from PIL import Image
import requests
import calendar

gmt = time.gmtime()

ruta_img = "C:\\Users\\user\\Desktop\\scraping\\img\\"
name_img = ""
timer = time.time()
mainpath = "C:\\chrome\\"

scrap = Blueprint('scrap', __name__)

@scrap.route('/scrap',methods=['POST'])


#Logica

def llamarServicioSet():
    global nombre,telefono,canal,detalle
    canal =  request.json['canal']
    if canal == 'ANDE':
        scrapAnde(request)
    elif canal == 'CLARO':
        scrapClaro(request)
 
    salida = {'codRes': codRes, 'menRes' : menRes, 'resPath' : resPath}
    return jsonify({'ParmOut': salida})






def inicializarVariables(request):
    global codRes, menRes, resNombre, resApellido
    
    print('REQUEST--->',request)
    
    nombre =  request.json['nombre']
    telefono =  request.json['numtel']
    canal =  request.json['canal']
    detalle =  request.json['detalle']
    print('NOMBRE--->',nombre)
    print('TELEFONO--->',telefono)
    print('CANAL--->',canal)
    print('DETALLE--->',detalle)
    
    
    
    #fullpath = os.path.join(mainpath)
    
    
    
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    resNombre =  nombre
    resApellido = 'Acosta'



"""
*******ANDE********
"""

def scrapAnde(request):
    global fullpath,options,driver_path,driver,PID
    global nombre,telefono,canal,detalle
    global codRes, menRes, resPath
    
    try:
        
        detalle = request.json['detalle']
        print('ANDE--->', detalle['NIS'])

        fullpath = os.path.join(mainpath)

        # Opciones de Navegacion

        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')

        driver_path = 'C:\\chrome\\chromedriver.exe'

        # Se crea la variable driver y se le pasa drive path que es la ruta del driver y se le pasa options

        driver = webdriver.Chrome(driver_path, chrome_options = options)

        # Inicializarla en la pantalla 2
        driver.set_window_position(2000, 0)
        driver.maximize_window()
        PID = driver.service.process.pid ##ID proceso Chomedriver
        print ('PID: ' + str(PID))
        time.sleep(8)


        #Inicializamos el Navegador 
        driver.get('https://www.ande.gov.py/servicios/')
        time.sleep(5)
        
        for element in driver.find_elements_by_class_name('c-hand'):
            if element.text == 'COMERCIAL':
                element.click()
                time.sleep(3)
                
                
        for element2 in driver.find_elements_by_tag_name('a'):
            
            #print('ELEMTS--->',element2.text)
            if element2.text == 'Consulta de Facturas':
                element2.click()

    
        NIS = driver.find_element_by_id('in-Factura_nis')
        NIS.send_keys(detalle['NIS'])
    
        for button in driver.find_elements_by_tag_name('button'):
            #print('ELEMTS--->',button.text)
            if button.text == 'Consultar':
                button.click()
        time.sleep(3)
        name_img = 'ande'+str(calendar.timegm(gmt))
        print('NAMEIMAGE-->',name_img)
        driver.save_screenshot(ruta_img+name_img+".png")
    
        driver.close()
        driver.quit()
    
        codRes = 'SIN_ERROR'
        menRes = 'OK'
        resPath = name_img+".png"
    except:
        codRes = 'ERROR'
        menRes = 'OK'
        resPath = 'NULL'
    
    

"""
*******CLARO********
"""  
def scrapClaro(request):
    
    print('CLARO--->', request.data)
    
    
    
    
    
    
    
    
    
    
    
    





