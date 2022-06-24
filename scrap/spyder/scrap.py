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

ruta_img = "C:\\Users\\kacosta\\Documents\\testk\\scrap\\img\\"
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
    global fullpath,options,driver_path,driver,PID
    global nombre,telefono,canal,detalle
    global codRes, menRes, resPath
    print('CLARO--->', request.data)
    try:
        detalle = request.json['detalle']
        print('CLARO--->', detalle['usuario'])
        print('CLARO--->', detalle['clave'])
        
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
        driver.get('https://ingreso.claro.com.py/auth/realms/claro-py/protocol/openid-connect/auth?client_id=MiClaro&redirect_uri=https%3A%2F%2Fm-miclaro.claro.com.py%2Foauth%2Fcallback&response_type=code&scope=openid%20profile%20email%20claro_profile%20miclaro.claro.amx%2Fapi%3Arw%20ums.claro.amx%2Fuser%3Ar&state=476f6644245442b48c6fbda489f0eaa3&code_challenge=FSQdubo5q3SuuhrOySkQeSXDpMViPYSEBhNFlJzKRz4&code_challenge_method=S256&response_mode=query')
        time.sleep(5)
        
        usuario = driver.find_element_by_id('username')
        usuario.send_keys(detalle['usuario'])
        clave = driver.find_element_by_id('password')
        clave.send_keys(detalle['clave'])
        time.sleep(1)
        button =  driver.find_element_by_id('kc-login')
        button.click()
        time.sleep(10)
        """
        for element in driver.find_elements_by_tag_name('span'):
            #print('ELEMTS--->',element.text)
            if element.text == 'Ver Mi Factura':
                element.click()
        """
        name_img = 'claro'+str(calendar.timegm(gmt))
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
    
    
    
    
    
    
    
    
    
    





