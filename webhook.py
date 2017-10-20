#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
from threading import Thread

import bottle
import time
import json

__author__ = 'mishindanila'

import os
import requests
from bottle import post, run, request, route

@route("/")
def hi():
    return "Hi"

@post("/")
def pos():
    js = request.json

    bot_id = '410526091:AAFdTBSEOao1cUDwivV04qyK38OuQqswz_g'
    
    chat_id = str(js['message']['chat']['id'])
    name = str(js['message']['from']['first_name'])
    surname = str(js['message']['from']['last_name'])
    message = str(js['message']['text'])
    
    print("Name: " + str(js['message']['from']['first_name']))
    print("Surname: " + str(js['message']['from']['last_name']))
    print("Message: " + str(js['message']['text']))

    if(message == "Привет"):
        ans = "Привет, друг!"
    elif(message == "Ахтунги?"):
        ans = "Список ахтунгов: [ Пусто :( ]"
        
    requests.get('https://api.telegram.org/bot'+bot_id+'/sendMessage?chat_id='+chat_id+'&text='+ans)
                            
    return "0"

run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
