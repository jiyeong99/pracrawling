from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "craw.settings")
import django
django.setup()
from myapp.models import Data, Benefit
try:
    shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
except FileNotFoundError:
    pass

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_argument("headless")
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

for i in range(1,2435):
    try:
        driver.get(url=f'https://www.card-gorilla.com/card/detail/{i}')
        driver.execute_script('document.querySelector("#q-app > header").style.visibility="hidden";')

        # card이름
        card_name_css_selector = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.tit > strong')
        card_name = card_name_css_selector.text
        # 카드 브랜드
        card_brand_css_selector = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.tit > p')
        card_brand = card_brand_css_selector.text
        
        # 카드 연회비
        card_fee_in_css_selector = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(1) > dd.in_out')
        card_fee_in = card_fee_in_css_selector.text
        # 카드 실적
        card_record = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(2)')
        card_record = card_record.text
        
        # 카드 타입
        try:
            card_type = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(3)')
            card_type = card_type.text
        except:
            NoSuchWindowException
            card_type = None

        # 카드 신청 url
        # card_url = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.app_btn > a')
        # if card_url == True:
        #     card_url = card_url.get_attribute('href')
        
        # 카드 이미지
        card_image = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.card_img > img')
        card_image = card_image.get_attribute('src')

        # 카드 혜택
        card_option_name = driver.find_elements(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt > strong')
        card_option_content = driver.find_elements(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt > i')
        card_option_detail_cbefore = driver.find_elements(By.XPATH, '//*[@id="q-app"]/section/div[1]/section/div/article[2]/div[1]/dl')
                
        if card_name != '':
            print('card_name:',card_name)
            print('card_brand:',card_brand)
            print('card_in_out:',card_fee_in)
            print('card_record:',card_record)    
            if card_type != None:
                print('card_type_lst:',card_type)    
            print('card_image:',card_image)
            data = Data(name=card_name,brand=card_brand,fee=card_fee_in,card_record=card_record, card_type=card_type, card_image=card_image)
            data.save()


            for j in card_option_detail_cbefore:
                j.click()
                
            card_option_detail_cafter = driver.find_elements(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl.on > dd > div')


            for k in range(len(card_option_name)):
                con = card_option_name[k].text
                coc = card_option_content[k].text
                cod = card_option_detail_cafter[k].text
                print('card_option_name:',con)
                print('card_option_content:',coc)
                print('card_option_detail:', cod)
                benefit = Benefit(benefit_name=con,benefit_content=coc,benefit_detail=cod,card=data)
                benefit.save()
    except:
        continue
'''
driver.get(url=f'https://www.card-gorilla.com/card/detail/9')
driver.execute_script('document.querySelector("#q-app > header").style.visibility="hidden";')

# card이름
card_name_css_selector = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.tit > strong')
card_name = card_name_css_selector.text
# 카드 브랜드
card_brand_css_selector = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.tit > p')
card_brand = card_brand_css_selector.text

# 카드 연회비
card_fee_in_css_selector = driver.find_element(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(1) > dd.in_out')
card_fee_in = card_fee_in_css_selector.text
# 카드 실적
card_record = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(2)')
card_record = card_record.text

# 카드 타입
try:
    card_type = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(3)')
except:
    NoSuchWindowException
    card_type = None

if card_type != None :
    card_type = card_type.text
else :
    print('card_type is None')
# 카드 신청 url
# card_url = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.app_btn > a')
# if card_url == True:
#     card_url = card_url.get_attribute('href')

# 카드 이미지
card_image = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.card_img > img')
card_image = card_image.get_attribute('src')

# 카드 혜택
card_option_name = driver.find_elements(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt > strong')
card_option_content = driver.find_elements(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt > i')
card_option_detail_cbefore = driver.find_elements(By.XPATH, '//*[@id="q-app"]/section/div[1]/section/div/article[2]/div[1]/dl')
        
if card_name != '':
    print('card_name:',card_name)
    print('card_brand:',card_brand)
    print('card_in_out:',card_fee_in)
    print('card_record:',card_record)    
    if card_type != None:
        print('card_type_lst:',card_type)    
    print('card_image:',card_image)
    # data = Data(name=card_name,brand=card_brand,fee=card_fee_in,card_record=card_record, card_type=card_type, card_image=card_image)
    # data.save()


    for j in card_option_detail_cbefore:
        j.click()
            
    card_option_detail_cafter = driver.find_elements(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl.on > dd > div')


    for k in range(len(card_option_name)):
        con = card_option_name[k].text
        coc = card_option_content[k].text
        cod = card_option_detail_cafter[k].text
        print('card_option_name:',con)
        print('card_option_content:',coc)
        print('card_option_detail:', cod)
        # benefit = Benefit(benefit_name=con,benefit_content=coc,benefit_detail=cod,card=data)
        # benefit.save()
'''