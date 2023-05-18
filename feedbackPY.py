from datetime import datetime
import json
from bottle import post, request
import re

#функция проверки валидности почты
def checkEmail(email):
    #инициализация паттерна для проверки строки регулярным выражением
    pattern = re.compile("[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$") 
    if re.match(pattern, email) is not None:
        return True
    else:
        return False



@post('/feedback', method='post')
def my_form():
    #получение введённых данных с формы главной страницы
    feedbacktext = request.forms.get('FEEDBACKTEXT')
    email = request.forms.get('ADRESS')
    nickname = request.forms.get('NICKNAME')
    date_ = request.forms.get('DATE_')
    #создание словаря, содержащего введённые пользователем данные, где ключ это email, а значение это список из username и списка questions
    dictionary = {}
    #проверки заполнености форм и валидности введённых данных
    if (len(feedbacktext)>3):
        #проверка содержания буквы в тексте вопроса по символьно
        if any(c.isalpha() for c in feedbacktext): 
            if (len(email)>0):
                if (len(nickname)>0):
                    if (len(nickname)>=3): 
                        #проверка валидности почты
                        if (checkEmail(email)):
                             #переменная состояния содержания текущей введённой почты в файле data.txt
                            state = ""
                            #открытие файла data.txt для считывания из него данных
                            with open('feedbacks.txt') as json_file:
                                #загрузка данных, считанных из файла data.txt в формате json
                                dictionary = json.load(json_file)
                                #проверка содержания введённого emal в словаре, то есть отправлял ли данный пользователь вопрос ранее
                                if email in dictionary.keys():
                                    #проверка содержания введённого вопроса у текущего пользователя
                                    if feedbacktext not in dictionary[email]['feedbacktexts']:
                                        #добавление введённого вопроса в случае, если его нет в вопросах пользователя
                                        dictionary[email]['feedbacktexts'].append(feedbacktext)
                                        state = "again"
                                    else:
                                        #изменение переменной состояния, которая демонстрирует, что пользователь уже задал этот вопрос
                                        state = "again, but this question you asked yet"
                                else:
                                    #если данной почты нет в данных, то создается новый элемент словаря
                                    time_ = datetime.datetime.today().strftime("%H:%M:%S")
                                    dictionary[email] = {'nickname' : nickname, 'feedbacktexts' : [feedbacktext], 'dates' : [date_], 'times' : [time_]}
                            #открытие файла data.txt на запись
                            with open('feedbacks.txt', 'w') as outfile:
                                #запись в файл data.txt данных из словаря посредством преобразования в json
                                json.dump(dictionary, outfile)
                            #получение текущей даты
                            
                            #возвращение строки с успешным результатом взаимодействия пользователя с формой, на которую влияет переменная состояния
                            return "Thanks {0}, {1}! The answer will be sent to the mail {2}\n Access Date:  {3}".format(state, name,  email, date_)
                        else:  return "Erorr! Email is not valid"
                    else: return "Erorr! Name is so short"
                else: return "Erorr! Name is empty"
            else: return "Erorr! Email is empty"
        else: return "Erorr! Question is not correct"
    else: return "Erorr! Question is so short"