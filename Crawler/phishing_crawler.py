import requests
import os
from bs4 import BeautifulSoup as bs

def parse_url():
    url, file_name = generate_url()
    page_num = 0
    print(url)
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query=%EC%A0%9C%EC%A3%BC+%EB%A0%8C%ED%8A%B8%EC%B9%B4&research_url=&sm=tab_pge&start=1&where=web"
    }
    # Exist Directory and file
    this_dir, _ = os.path.split(__file__)
    data_dir = this_dir + '/data'
    path_file = data_dir + '/' + file_name
    if os.path.isdir(data_dir):
        if os.path.isfile(path_file):
            pass
        else:
            with open(path_file, 'w'):
                pass
    else:
        os.makedirs('data')
        if os.path.isfile(path_file):
            pass
        else:
            with open(path_file, 'w'):
                pass

    size_temp = 0
    while 1:
        # 페이지 수대로 URL 생성
        file_size = 0
        page_num = page_num + 1
        url_result = url + "&page="+str(page_num)
        html = session.get(url_result, headers=headers).content.decode('euc-kr', 'replace')
        soup = bs(html, "html.parser")

        # 해당 페이지에 있는 링크를 불러옴
        for meta in soup.find_all('td', class_="darkgreen"):
            with open(path_file, 'a') as f:
                f.write(meta.text.strip()+"\n")

        file_size = os.path.getsize(path_file)
        if file_size == size_temp:
            print("더이상 받아올 데이터가 없습니다.")
            exit(0)

        size_temp = file_size


def generate_url():
    # step0: save material
    url_front = 'https://rankey.com/search/rankey_search.php?what=site&search_word='

    # step1: input keyword
    str_keyword = str(input("input your keyword: "))
    # str_keyword = "배달"
    file_name = str_keyword
    str_keyword = str(str_keyword.encode("euc-kr"))
    print(f'encode is: {str_keyword}')

    # step2: remove binary keyword 'b' and replace \x to %
    str_keyword = str_keyword.replace('\\x', "%")
    str_keyword = str_keyword.replace('\'', "")[1:]
    print(f'remove b and replace is: {str_keyword}')

    return url_front+str_keyword, file_name+".txt"

if __name__ == '__main__':
    parse_url()

