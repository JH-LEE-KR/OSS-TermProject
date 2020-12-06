from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from multiprocessing import Pool #멀티쓰레딩

# 구글 드라이버를 크롬 버전에 맞게 설치하고 경로를 입력해준다.
# 이곳에 크롬 드라이버 경로를 입력해주세요.
chromedriver_path = "/Users/kimtaeyoung/Desktop/project/opensource_termproject/2020-02-OSS-TermProject/python/chromedriver"
# 몇개의 파일을 크롤링할지
crawling_num = 500

# headless 셀레니움
# 크롬 드라이버에 적용할 옵션들
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

# 폴더를 확인하고 없다면 만들어준다.
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

# 크롤링
# get_keywords의 결과를 파라미터로 넣어주면 된다. 
def crawling(search_name):
    driver = webdriver.Chrome(chromedriver_path, chrome_options=options) #headless를 위한 옵션을 추가
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(search_name)
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
    createFolder("python/model/"+search_name)

    for image in images:
        try:
            image.click()
            # 이미지가 로딩되는 속도. 안정적으로는 2-3초가 적당.
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, "python/model/"+search_name+"/"+str(count) + ".jpg")
            count = count + 1

            # 크롤링할 개수 설정. 
            if count > crawling_num:
                break
        except:
            pass

    # 끝나고 크롬 드라이버를 종료해준다
    driver.close()

if __name__ == '__main__':

    #모델 폴더를 만들어준다. 
    createFolder("python/model/")
    
    pool = Pool(processes=3) # 3개의 프로세스를 사용합니다.
    pool.map(crawling, get_keywords()) 