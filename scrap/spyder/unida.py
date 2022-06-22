# -*- coding: utf-8 -*-
"""
Created on Fri May 20 18:42:50 2022

@author: Laboratorio
"""
"""
"""

# Librerias
# pip install selenium

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
#Controlar Tiempo

import time

# Utilitarios para sistema operativo

import os, signal
from PIL import Image
import requests


#Definimos dos variables
ruta_img = "C:\\Users\\user\\Pictures\\Camera Roll"
name_img = "eclass"
timer = time.time()
#Ruta para Windows

mainpath = "C:\\chrome\\"

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
time.sleep(1)

#Inicializamos el Navegador 
driver.get('https://eclass.unida.edu.py/eclass//')#<-cambiar enlace antes de ejecutar

carpeta_user = "C:\\Users\\"
carpeta_desktop = "user\\Pictures\\Camera Roll\\"


#Se imprime las variables declaradas 
carpeta_final=carpeta_user + carpeta_desktop

print("CARPETAAAAA", carpeta_final)


time.sleep(15)
codigo = driver.find_element_by_id('codigo')
codigo.send_keys('2019100801')

#Agregar password 
passw = driver.find_element_by_id('password')
passw.send_keys('Minombr3')#<-agregar contraseña
driver.save_screenshot(ruta_img+name_img+"1"+".png")
archivo1=ruta_img+name_img+"1"+".png"
files={'photo':open(archivo1,'rb')}
#resp=requests.post('https://api.telegram.org/bot5318805370:AAFjestIPZr0XMkGM8MjbfTP2YFmz13TCPA/sendPhoto?chat_id=-595915883',files=files)

#click boton 
for element in driver.find_elements_by_class_name('btn'):
    if element.text == 'Ingresar':
        element.click()
time.sleep(3)   
elem = driver.find_element_by_id('spanClose');
elem.click()
time.sleep(2)  
driver.save_screenshot(ruta_img+name_img+"2"+".png")
archivo2=ruta_img+name_img+"2"+".png"
files={'photo':open(archivo2,'rb')}
#resp=requests.post('https://api.telegram.org/bot5318805370:AAFjestIPZr0XMkGM8MjbfTP2YFmz13TCPA/sendPhoto?chat_id=-595915883',files=files)
#screenshot = Image.open()
driver.close()
driver.quit()