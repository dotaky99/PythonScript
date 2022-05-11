import requests
import os
import time, re
from bs4 import BeautifulSoup as bs
'''
1. 모든 href 등 링크들을 가져옴
2. js 체크
'''

def check_phishing():
    # step1: input keyword
    # str_keyword = str(input("input your keyword: "))
    str_keyword = "치킨"
    filter_str = ""
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=%EC%A0%9C%EC%A3%BC+%EB%A0%8C%ED%8A%B8%EC%B9%B4&research_url=&sm=tab_pge&start=1&where=web"
    }

    url = ""
    url_list = []
    with open("data/"+str_keyword+".txt", "r") as f:
        while 1:
            # 파일 끝까지 읽기
            url = f.readline().strip()
            if url == '':
                break

            # 웹 서비스 중인지 체크
            try:
                html = requests.get(url, headers=headers).content.decode('euc-kr', 'replace')
                print(url+" is con")
            except:
                print(url+" is not")
                continue

            soup = bs(html, "html.parser")


            # print(soup)
            time.sleep(1)
            break

if __name__ == '__main__':
    check_phishing()