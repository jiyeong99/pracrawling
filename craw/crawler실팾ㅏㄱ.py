# crawling.py
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "craw.settings")
import django
django.setup()
from myapp.models import Data


# def name_card():
#     # 고릴라 차트 100에서
#     req = requests.get('https://card-search.naver.com/list?ptn=2&sortMethod=ri&bizType=CPC')
#     html = req.content.decode('utf-8','replace')
#     soup = BeautifulSoup(html, 'html.parser')
#     adjective_name = soup.select('#app > div.cards > div > div.tabpanel > ul > li > div.info > a > b')
    
#     card_list = []
    
#     for name in adjective_name:
#         card_list.append(name.text.strip())
#         #adjective_list안에 이름들이 하나씩 저장되었다.
#     return card_list

def name_card():
    # 고릴라 차트 100에서
    req = requests.get('https://www.card-gorilla.com/chart/top100?term=weekly/')
    html = req.content.decode('utf-8','replace')
    soup = BeautifulSoup(html, 'html.parser')
    adjective_name = soup.select('#q-app > section > div.chart_view > section > div.inner > article.con_area > div > div > ul > li > a > div > p.card_name > a')
    
    card_list = []
    
    for name in adjective_name:
        card_list.append(name.text.strip())
        #adjective_list안에 이름들이 하나씩 저장되었다.
    return card_list

if __name__ == '__main__':
    i=0
    while(i<len(name_card())):
        a = Data(title=name_card()[i])
        a.save()
        i+=1