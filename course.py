import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pprint import pprint


def get_list_name_valute():
    return list(valute.keys())

def get_course(name_valute):
    return valute[name_valute]


def get_course_info(id):
    name_valute = xml.find('valute', {'id': id}).find('name').text
    valute_nominal = int(xml.find('valute', {'id': id}).nominal.text)
    valute_Value = float(xml.find('valute', {'id': id}).value.text.replace(',', '.'))
    return f"{name_valute} стоит {valute_Value/valute_nominal} руб/шт"

valute = {}

url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
responce = requests.get(url, params={'date_req': datetime.today().strftime('%d/%m/%Y')})
xml = BeautifulSoup(responce.content, 'html.parser')
valute_information = xml.find_all('valute')


for inf in valute_information:
    valute_nominal = int(inf.nominal.text)
    valute_Value = float(inf.value.text.replace(',', '.'))
    valute[inf.find('name').text] = valute_Value/valute_nominal


if __name__=='__main__':
    print(get_list_name_valute())
    print(xml)
    pprint(valute)
    print(get_course_info("R01020A"))
    print(get_course_info("R01239"))
    print(get_course_info("R01035"))