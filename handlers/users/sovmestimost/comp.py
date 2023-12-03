import requests
from bs4 import BeautifulSoup as BS

def sovmestimost(z_w, z_m, type):
    v = []
    r = requests.get(f'https://horoscopes.rambler.ru/sovmestimost-znakov-zodiaka/zhenshhina-{z_w}-muzhchina-{z_m}/')
    soup = BS(r.content, 'html.parser')
    title = soup.find('h1', class_='_3wtsS _1W8Ro _2kQY7').text.strip()  # good
    predislov = soup.find('p', class_='mtZOt').text.strip()  # good
    v.append(predislov)
    all = soup.find('div', class_='_1E4Zo _3BLIa').find_all(['p', 'h2'])
    all_types = soup.find_all('h2', class_='_29SJz')
    index = 0
    for i, content in enumerate(all):
        if content.text == type:
            index = i
            v.append(content.text)
            break

    for i in all[index + 1:]:
        if i.name == 'h2':
            break
        v.append(i.text)
    return v


