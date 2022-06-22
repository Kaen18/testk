# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:48:48 2022

@author: Laboratorio
"""

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    #contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['C:\Users\Laboratorio\Desktop\eclass.png']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = "-595915883"
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1834145008:AAFjVvTM4JGbXPp7wX4aRx3GUmv2CnGZ-fM')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()