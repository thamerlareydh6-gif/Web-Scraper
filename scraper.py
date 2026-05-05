import requests
from bs4 import BeautifulSoup


def cnn_travel_scraper(url):
    res = requests.get(url)
    # print(res.status_code)
    soup = BeautifulSoup(res.content, "html.parser")
    content = soup.find_all(
        "p", class_="paragraph-elevate inline-placeholder vossi-paragraph_elevate"
    )
    r = ""
    if content:
        for para in content:
            r += para.text.strip() + "\n"
        return r
    else:
        return "No article found !"


print(
    cnn_travel_scraper(
        "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"
    )
)
