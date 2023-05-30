from datetime import datetime
import json
from bottle import post, request, template
import re

#ôóíêöèÿ ïðîâåðêè âàëèäíîñòè ïî÷òû
def checkEmail(email):
    #èíèöèàëèçàöèÿ ïàòòåðíà äëÿ ïðîâåðêè ñòðîêè ðåãóëÿðíûì âûðàæåíèåì
    pattern = re.compile("[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$") 
    if re.match(pattern, email) is not None:
        return True
    else:
        return False



@post('/feedback', method='post')
def my_form():
    #ïîëó÷åíèå ââåä¸ííûõ äàííûõ ñ ôîðìû ãëàâíîé ñòðàíèöû
    feedbacktext = request.forms.get('FEEDBACKTEXT')
    nickname = request.forms.get('NICKNAME')
    email = request.forms.get('EMAIL')
    #date_ = request.forms.get('DATE_')
    #создание словаря, содержащего введённые пользователем данные, где ключ это email, а значение это список из username и списка questions
    dictionary = {}
    check = checkvalue(feedbacktext, nickname) 
    if (check== ""):
         with open('feedbacks.txt') as json_file:
         #загрузка данных, считанных из файла data.txt в формате json
            dictionary = json.load(json_file)
         time_ = datetime.today().strftime("%H:%M:%S")
         date_ = datetime.now().date()
         dictionary[email] = {'nickname' : nickname, 'feedbacktexts' : feedbacktext, 'dates' : str(date_), 'times' : str(time_)}
         with open('feedbacks.txt', 'w') as outfile:
            #запись в файл data.txt данных из словаря посредством преобразования в json
            json.dump(dictionary, outfile)
         return template("feedbackV.tpl", title='Feedback', year = str(datetime.now().date()), error="", errorCheck=[])
    else:
        errorCheck = [nickname, feedbacktext]
        if (check[0] == "1"):
            errorCheck = ["", feedbacktext]
        if (check[0] == "2"):
            errorCheck = [nickname, ""]
        return template("feedbackV.tpl", title='Feedback', year = str(datetime.now().date()), error=check[1], errorCheck=errorCheck)
    

def checkvalue(feedbacktext, nickname):
    if (len(feedbacktext) > 0):
        if (len(nickname) >= 3):
            return ""
        else: 
            return ["1", "Error! Your nickname is so short"]
    else: 
        return ["2", "Error! Your feedback is empty"]
