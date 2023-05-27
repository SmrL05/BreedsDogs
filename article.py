from datetime import datetime
import json
from bottle import post, request
from re import compile as regex_compile

def isCorrectMail(email: str):
    pattern = regex_compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$")
    if pattern.match(email):
        return True
    else: 
        return False


@post('/article', method='post')
def my_form():
    # Берем данные из формы
    article_ = request.forms.get('ARTICLE')
    name_ = request.forms.get('NAME_AUTHOR')
    email_ = request.forms.get('EMAIL_AUTHOR')
    phone_ = request.forms.get('PHONE_AUTHOR')

