from datetime import datetime
import json
from bottle import post, request, template
import re

#проверка валидности почтового адреса
def checkEmail(email):
    pattern = re.compile("[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$") 
    if re.match(pattern, email) is not None:
        return True
    else:
        return False

#проверка валидности телефонного номера
def checkPhone(phone):
    pattern = re.compile("^((\+7|7|8)+\(([0-9]{3})\)+([0-9]{3})+\-+([0-9]{2})+\-+([0-9]{2}))$");
    
    if re.match(pattern, phone) is not None:
        return True
    else:
        return False


@post('/feedback', method='post')
def my_form():
    feedbacktext = request.forms.get('FEEDBACKTEXT')
    nickname = request.forms.get('NICKNAME')
    email = request.forms.get('EMAIL')
    phone = request.forms.get('PHONE')
    #создание словаря, содержащего введённые пользователем данные, где ключ это email, а значение это список из username и списка questions
    dictionary = {}
    check = checkvalue( nickname, email, phone, feedbacktext) 
    if (check== ""):
         with open('feedbacks.txt') as json_file:
         #загрузка данных, считанных из файла data.txt в формате json
            dictionary = json.load(json_file)
         time_ = datetime.today().strftime("%H:%M:%S")
         date_ = datetime.now().date()
         dictionary[email] = {'nickname' : nickname, 'feedbacktexts' : feedbacktext,'phone': phone , 'dates' : str(date_), 'times' : str(time_)}
         with open('feedbacks.txt', 'w') as outfile:
            #запись в файл data.txt данных из словаря посредством преобразования в json
            json.dump(dictionary, outfile)
         return template("feedbackV.tpl", title='Feedback', year = str(datetime.now().date()), error="", errorCheck=["", "", "", ""])
    else:
        errorCheck = [nickname, email, phone, feedbacktext]
        return template("feedbackV.tpl", title='Feedback', year = str(datetime.now().date()), error=check[1], errorCheck=errorCheck)

#проверка введённых данных
def checkvalue(nickname, email, phone, feedbacktext):
    if (len(feedbacktext) > 0):
        if (len(nickname) >= 3):
            if (checkEmail(email)):
                if (checkPhone(phone)):
                    return ""
                else:
                    return ["3", "Error! Your phone is not valid\nTry it '+7(xxx)xxx-xx-xx'" ]
            else:
                return ["2", "Error! Your email is not valid"]
        else: 
            return ["1", "Error! Your nickname is so short"]
    else: 
        return ["4", "Error! Your feedback is empty"]
