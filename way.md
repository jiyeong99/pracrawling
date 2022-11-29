crawling
: 소프트웨어와 같은 무언가가 인터넷을 돌아다니며 정보를 수집해 오는 작업
crawler
: 크롤링 작업을 하는 소프트웨어
출처 : [법률신문] 김태욱, 2022.06.13 https://m.lawtimes.co.kr/Content/Opinion?serial=179382

1. 셀레니움 설치
    `pip install selenium`

2. 크롬 드라이버 자동 설치
    `pip install chromedriver-autoinstaller`
3. 크롤러만들기
```python
# myapp/crawler.py
from selenium import webdriver
import chromedriver_autoinstaller

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10)
```
4. 크롤러 써보기?
```python
# myapp/views.py

```
데이터 가져오는 방법을 모르겠어서 실패.. 다른방법 찾아보기

5. 
6. 