from datetime import datetime
import json
from bottle import post, request, template
from re import compile as regex_compile

global title, year
title=''
year = datetime.now().year

# Функция для проверкии соответствия почты или номера телефона соответствующему паттерну
def isCorrectData(data, type_):
    patternEmail = regex_compile("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$")
    patternPhone = regex_compile("^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    if (type_ == "email"):
        if patternEmail.match(data):
            return True
        else: 
            return False
    elif (type_ == "phone"):
        if patternPhone.match(data):
            return True
        else: 
            return False
    else: 
        return False


@post('/article', method='post')
def my_form():
    # Берем данные из формы
    global titleArticle_, article_, urlArticle_, name_, email_, phone_
    titleArticle_ = request.forms.get('TITLE_ARTICLE')
    article_ = request.forms.get('ARTICLE')
    urlArticle_ = request.forms.get('URL_ARTICLE')
    name_ = request.forms.get('NAME_AUTHOR')
    email_ = request.forms.get('EMAIL_AUTHOR')
    phone_ = request.forms.get('PHONE_AUTHOR')
    if (checkInputFields() != ""):        
          return template("article.tpl", title=title, year=year, titleArticle = titleArticle_, article = article_, urlArticle = urlArticle_, name = name_, email = email_, phone = phone_, state = 1, error=checkInputFields())
    if (writeToFile() != ""):        
          return template("article.tpl", title=title, year=year, titleArticle = titleArticle_, article = article_, urlArticle = urlArticle_, name = name_, email = email_, phone = phone_, state = 1, error=writeToFile())
    return template("article.tpl", title=title, year=year, titleArticle = '', article = '', urlArticle = '', name = '', email = '', phone = '', state = 0, error='')

# Функция для проверки введенных значений на сайте
def checkInputFields():
    error = ""
    if (titleArticle_ == "" or article_ == "" or urlArticle_ == "" or name_ == "" or email_ == "" or phone_ == ""):
        error = "You left the fields empty!"
    elif (len(titleArticle_) <= 3):
        error = "Insert the correct title of the article!"
    elif (len(urlArticle_) <= 3):
        error = "Insert the correct link!"
    elif (len(article_) <= 9 or len(article_) >= 300):
        error = "Write the correct annotation!"
    elif (len(name_) <= 2):
        error = "Enter the correct author name!"
    elif (isCorrectData(email_, "email") == False):
        error = "Enter the correct email!"
    elif (isCorrectData(phone_, "phone") == False):
        error = "Enter the correct author number! Pattern +7(***)***-**-**"
    else:
        error = ""
    return error

# Функция для записи данных в файл json
def writeToFile():
    error = ""
    date_object = datetime.today().strftime('%Y-%m-%d')
    articles_ = {}
    with open('articles.txt') as json_file:
        # Считывание данных из файла
        articles_ = json.load(json_file)
    for i in articles_:
        # Проверка "есть ли на сайте статья с таким названием"
        if titleArticle_ in articles_[i]['titleArticle']:
            # Если статья есть, выводим сообщение пользователю
            error = "Статья с таким названием уже есть на сайте!"
            return error
        else:
            # Если статьи нет, заносим данные в словарь, а затем в файл
            articles_[len(articles_)] = {'titleArticle' : titleArticle_, 'article' : article_, 'urlArticle' : urlArticle_, 'name' : name_, 'email' : email_, 'phone' : phone_, 'date' : date_object}
            break
    # Запись в файл
    with open('articles.txt', 'w') as outfile:
        json.dump(articles_, outfile)
    return error