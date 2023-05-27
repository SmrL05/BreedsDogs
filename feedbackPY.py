from datetime import datetime
import json
from bottle import post, request
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
    email = request.forms.get('ADRESS')
    nickname = request.forms.get('NICKNAME')
    date_ = request.forms.get('DATE_')
    #ñîçäàíèå ñëîâàðÿ, ñîäåðæàùåãî ââåä¸ííûå ïîëüçîâàòåëåì äàííûå, ãäå êëþ÷ ýòî email, à çíà÷åíèå ýòî ñïèñîê èç username è ñïèñêà questions
    dictionary = {}
    #ïðîâåðêè çàïîëíåíîñòè ôîðì è âàëèäíîñòè ââåä¸ííûõ äàííûõ
    if (len(feedbacktext)>3):
        #ïðîâåðêà ñîäåðæàíèÿ áóêâû â òåêñòå âîïðîñà ïî ñèìâîëüíî
        if any(c.isalpha() for c in feedbacktext): 
            if (len(email)>0):
                if (len(nickname)>0):
                    if (len(nickname)>=3): 
                        #ïðîâåðêà âàëèäíîñòè ïî÷òû
                        if (checkEmail(email)):
                             #ïåðåìåííàÿ ñîñòîÿíèÿ ñîäåðæàíèÿ òåêóùåé ââåä¸ííîé ïî÷òû â ôàéëå data.txt
                            state = ""
                            #îòêðûòèå ôàéëà data.txt äëÿ ñ÷èòûâàíèÿ èç íåãî äàííûõ
                            with open('feedbacks.txt') as json_file:
                                #çàãðóçêà äàííûõ, ñ÷èòàííûõ èç ôàéëà data.txt â ôîðìàòå json
                                dictionary = json.load(json_file)
                                #ïðîâåðêà ñîäåðæàíèÿ ââåä¸ííîãî emal â ñëîâàðå, òî åñòü îòïðàâëÿë ëè äàííûé ïîëüçîâàòåëü âîïðîñ ðàíåå
                                if email in dictionary.keys():
                                    #ïðîâåðêà ñîäåðæàíèÿ ââåä¸ííîãî âîïðîñà ó òåêóùåãî ïîëüçîâàòåëÿ
                                    if feedbacktext not in dictionary[email]['feedbacktexts']:
                                        #äîáàâëåíèå ââåä¸ííîãî âîïðîñà â ñëó÷àå, åñëè åãî íåò â âîïðîñàõ ïîëüçîâàòåëÿ
                                        dictionary[email]['feedbacktexts'].append(feedbacktext)
                                        state = "again"
                                    else:
                                        #èçìåíåíèå ïåðåìåííîé ñîñòîÿíèÿ, êîòîðàÿ äåìîíñòðèðóåò, ÷òî ïîëüçîâàòåëü óæå çàäàë ýòîò âîïðîñ
                                        state = "again, but this question you asked yet"
                                else:
                                    #åñëè äàííîé ïî÷òû íåò â äàííûõ, òî ñîçäàåòñÿ íîâûé ýëåìåíò ñëîâàðÿ
                                    time_ = datetime.datetime.today().strftime("%H:%M:%S")
                                    dictionary[email] = {'nickname' : nickname, 'feedbacktexts' : [feedbacktext], 'dates' : [date_], 'times' : [time_]}
                            #îòêðûòèå ôàéëà data.txt íà çàïèñü
                            with open('feedbacks.txt', 'w') as outfile:
                                #çàïèñü â ôàéë data.txt äàííûõ èç ñëîâàðÿ ïîñðåäñòâîì ïðåîáðàçîâàíèÿ â json
                                json.dump(dictionary, outfile)
                            #ïîëó÷åíèå òåêóùåé äàòû
                            
                            #âîçâðàùåíèå ñòðîêè ñ óñïåøíûì ðåçóëüòàòîì âçàèìîäåéñòâèÿ ïîëüçîâàòåëÿ ñ ôîðìîé, íà êîòîðóþ âëèÿåò ïåðåìåííàÿ ñîñòîÿíèÿ
                            return "Thanks {0}, {1}! The answer will be sent to the mail {2}\n Access Date:  {3}".format(state, name,  email, date_)
                        else:  return "Erorr! Email is not valid"
                    else: return "Erorr! Name is so short"
                else: return "Erorr! Name is empty"
            else: return "Erorr! Email is empty"
        else: return "Erorr! Question is not correct"
    else: return "Erorr! Question is so short"