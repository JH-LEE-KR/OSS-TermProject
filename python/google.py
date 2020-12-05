from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

# 구글 드라이버를 크롬 버전에 맞게 설치하고 경로를 입력해준다.
# 이곳에 크롬 드라이버 경로를 입력해주세요.

chromedriver_path = "/Users/kimtaeyoung/Desktop/project/opensource_termproject/2020-02-OSS-TermProject/python/chromedriver"

# 몇개의 파일을 크롤링할지
crawling_num = 500

# 폴더 생성해주는 함수

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# 크롤링 할 단어들을 받아온다. 
# 크롤링할 단어는 keywords.txt에 입력하면 된다. 

def get_keywords(keywords_file='python/keywords.txt'):
        # read search keywords from file
        with open(keywords_file, 'r', encoding='utf-8-sig') as f:
            text = f.read()
            lines = text.split('\n')
            lines = filter(lambda x: x != '' and x is not None, lines)
            keywords = sorted(set(lines))

        print('{} keywords found: {}'.format(len(keywords), keywords))

        # re-save sorted keywords
        with open(keywords_file, 'w+', encoding='utf-8') as f:
            for keyword in keywords:
                f.write('{}\n'.format(keyword))

        return keywords

#모델 폴더를 만들어준다. 

createFolder("python/model/")

for i in get_keywords() :
   
    driver = webdriver.Chrome(chromedriver_path)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    count = 1

    #폴더가 없다면 폴더를 만들어준다. 
    createFolder("python/model/"+i)

    for image in images:
        try:
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, "python/model/"+i+"/"+str(count) + ".jpg")
            count = count + 1

            # 크롤링할 개수 설정. 
            if count > crawling_num:
                break
        except:
            pass

    driver.close()