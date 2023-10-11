import requests
from bs4 import BeautifulSoup


def scrap_data():
    response = requests.get('https://www.bbc.com/').text
    soup = BeautifulSoup(response, "lxml")

    new_div = soup.find("section", class_="module--news")
    div_content = new_div.find("div", class_="module__content")
    div_content2 = div_content.find_all("div", class_="media__content")
    #print(div_content2.prettify())

    new_data = []

    for elm in div_content2 :
        url = elm.h3.a.text
        title = elm.p.text
        source = elm.findAll('a')[1].text
        new_data.append(
            {
                'url': url,
                'title': title,
                'source': source
            }
        )
    return new_data

"""print("Url : ", url.strip())
print("Title : ", title.strip())
print("Source : ", source.strip())"""

