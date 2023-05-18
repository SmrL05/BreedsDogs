from datetime import datetime
import json
from bottle import post, request
import re

#������� �������� ���������� �����
def checkEmail(email):
    #������������� �������� ��� �������� ������ ���������� ����������
    pattern = re.compile("[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$") 
    if re.match(pattern, email) is not None:
        return True
    else:
        return False



@post('/feedback', method='post')
def my_form():
    #��������� �������� ������ � ����� ������� ��������
    feedbacktext = request.forms.get('FEEDBACKTEXT')
    email = request.forms.get('ADRESS')
    nickname = request.forms.get('NICKNAME')
    date_ = request.forms.get('DATE_')
    #�������� �������, ����������� �������� ������������� ������, ��� ���� ��� email, � �������� ��� ������ �� username � ������ questions
    dictionary = {}
    #�������� ������������ ���� � ���������� �������� ������
    if (len(feedbacktext)>3):
        #�������� ���������� ����� � ������ ������� �� ���������
        if any(c.isalpha() for c in feedbacktext): 
            if (len(email)>0):
                if (len(nickname)>0):
                    if (len(nickname)>=3): 
                        #�������� ���������� �����
                        if (checkEmail(email)):
                             #���������� ��������� ���������� ������� �������� ����� � ����� data.txt
                            state = ""
                            #�������� ����� data.txt ��� ���������� �� ���� ������
                            with open('feedbacks.txt') as json_file:
                                #�������� ������, ��������� �� ����� data.txt � ������� json
                                dictionary = json.load(json_file)
                                #�������� ���������� ��������� emal � �������, �� ���� ��������� �� ������ ������������ ������ �����
                                if email in dictionary.keys():
                                    #�������� ���������� ��������� ������� � �������� ������������
                                    if feedbacktext not in dictionary[email]['feedbacktexts']:
                                        #���������� ��������� ������� � ������, ���� ��� ��� � �������� ������������
                                        dictionary[email]['feedbacktexts'].append(feedbacktext)
                                        state = "again"
                                    else:
                                        #��������� ���������� ���������, ������� �������������, ��� ������������ ��� ����� ���� ������
                                        state = "again, but this question you asked yet"
                                else:
                                    #���� ������ ����� ��� � ������, �� ��������� ����� ������� �������
                                    time_ = datetime.datetime.today().strftime("%H:%M:%S")
                                    dictionary[email] = {'nickname' : nickname, 'feedbacktexts' : [feedbacktext], 'dates' : [date_], 'times' : [time_]}
                            #�������� ����� data.txt �� ������
                            with open('feedbacks.txt', 'w') as outfile:
                                #������ � ���� data.txt ������ �� ������� ����������� �������������� � json
                                json.dump(dictionary, outfile)
                            #��������� ������� ����
                            
                            #����������� ������ � �������� ����������� �������������� ������������ � ������, �� ������� ������ ���������� ���������
                            return "Thanks {0}, {1}! The answer will be sent to the mail {2}\n Access Date:  {3}".format(state, name,  email, date_)
                        else:  return "Erorr! Email is not valid"
                    else: return "Erorr! Name is so short"
                else: return "Erorr! Name is empty"
            else: return "Erorr! Email is empty"
        else: return "Erorr! Question is not correct"
    else: return "Erorr! Question is so short"