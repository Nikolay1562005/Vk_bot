import vk_api
from course import *
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from wiki import*
import json


with open('admin_data.json', 'r', encoding='utf8') as f:
    data = json.load(f)

token = data['admin_data']['token']
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

list_name_valute = get_list_name_valute()

def correction(message):
    global seletion
    for valute in list_name_valute:
        if message.lower() in valute.lower():
            seletion = valute
            return True
    return False


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        msg_id = randint(1, 10**7)
        if correction(msg):
            list_name_valute = get_list_name_valute()
            res = seletion + ': ' + str(get_course(seletion)) + 'руб'

        elif 'валюта' in msg:
            res = ''
            for i in list_name_valute:
                res += '\n' + i
        elif msg.startswith('#wiki'):
            res = get_wiki_arctile(msg[6:])
        else:
            res = 'Не понимаю Ваш запрос'
        try:
            vk.messages.send(user_id=user_id, random_id=msg_id, message=res)
        except:
            print('error')