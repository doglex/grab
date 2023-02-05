import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))


def get_soup(url:str) -> BeautifulSoup:
    ans = s.get(url, timeout=5)
    soup = BeautifulSoup(ans.content, features="lxml")
    return soup



if __name__ == '__main__':
    print(get_soup("https://www.baidu.com/"))
