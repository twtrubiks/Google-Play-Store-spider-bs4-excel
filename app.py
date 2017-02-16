import requests
import datetime
import time
from bs4 import BeautifulSoup
from dbModel import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
targetURL = 'https://play.google.com/store/apps/top'
head = 'https://play.google.com'


def getItemTitle():
    rs = requests.session()
    res = rs.get(targetURL, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    ItemList = []
    soup_total = soup.select('.id-responsive-see-more')
    for index, title_link in enumerate(soup_total, 1):
        ItemList.append(head + title_link['href'])
        print('{} %'.format(round(100 * index / len(soup_total), 2)))
    return ItemList


def getAppLink(Itemdata):
    app_item = []
    for index, item in enumerate(Itemdata, 1):
        rs = requests.session()
        formdata = {
            'start': '0',
            'num': '100',
        }
        res = rs.post(item, data=formdata, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        item_head = soup.select('.cluster-heading h2')[0].text
        for data in soup.select('.id-card-list .card'):
            app_data = {
                "itemhead": item_head,
                "link": head + data.find('a')['href']
            }
            app_item.append(app_data)
        print('{} %'.format(round(100 * index / len(ItemList), 2)))
    return app_item


def getAppInformation(app):
    all_information = []
    for index, item in enumerate(app, 1):
        rs = requests.session()
        res = rs.get(item['link'], verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        for data in soup.select('.main-content'):
            datePublished, numDownloads = "", ""
            for tag in data.select('.details-section-contents .meta-info .content'):
                try:
                    if (tag.attrs['itemprop'] == 'datePublished'):
                        datePublished = tag.text
                    if (tag.attrs['itemprop'] == 'numDownloads'):
                        numDownloads = tag.text
                    if (datePublished != "" and numDownloads != ""):
                        break
                except:
                    pass
            try:
                app_data = {
                    "app": data.select('.id-app-title')[0].text,
                    "link": item['link'],
                    "autor": data.select('.document-subtitle.primary')[0].text,
                    "rate": data.select('.score')[0].text,
                    "download": numDownloads,
                    "publish": datePublished,
                    "item": item['itemhead']
                }
            except:
                print(item['link'])
                break

            all_information.append(app_data)
        print('{} %'.format(round(100 * index / len(app), 2)))
    return all_information


def WriteDB(information):
    for data in information:
        insert_data = GooglePlay(
            App=data['app'],
            Link=data['link'],
            Autor=data['autor'],
            Rate=data['rate'],
            Download=data['download'],
            Publish=datetime.datetime.strptime(data['publish'], "%Y年%m月%d日").date(),
            Item=data['item'],
        )
        db.session.add(insert_data)
    db.session.commit()


if __name__ == '__main__':
    tStart = time.time()
    print('Start parsing google play...(1/3)')
    ItemList = getItemTitle()
    print('Start parsing google play...(2/3)')
    app_data = getAppLink(ItemList)
    print('Start parsing google play...(3/3)')
    information = getAppInformation(app_data)
    print('End parsing google play')
    tEnd = time.time()
    print('It cost {} sec'.format(round(tEnd - tStart, 2)))
    print('Start Writing DB')
    WriteDB(information)
    print('End Writing DB')
    print('DONE')
