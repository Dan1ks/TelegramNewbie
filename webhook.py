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
    #print(js)
    bot_id = '478575473:AAFdWjmJF36mXLjizKHIPA4M99uxwNrLTYE'

    chat_id = str(js['message']['chat']['id'])
    name = str(js['message']['from']['first_name'])
    surname = str(js['message']['from']['last_name'])
    message = str(js['message']['text'])

    print("Name: " + str(js['message']['from']['first_name']))
    print("Surname: " + str(js['message']['from']['last_name']))
    print("Message: " + str(js['message']['text']))

    if (message == "Hello!"):
        ans = "Hello!"
    requests.get('https://api.telegram.org/bot' + bot_id + '/sendMessage?chat_id=' + chat_id + '&text=' + ans)

    return "0"


run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
