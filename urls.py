from urllib.parse import unquote
import json
import re

def checkCondition(url):
    return 'jsv=2.5.9&appKey' in url and 'timeslotId' not in url

def checkHasCookies(req):
    return '_m_h5_tk' in [i['name'] for i in req['request']['cookies']]

def getPageId(url):
    return eval(re.search(r'"pageId":(\d+),', url).group(1))

if __name__ == '__main__':
    with open('pages.lazada.sg.har') as file:
        data = json.load(file)

    allUrls = data['log']['entries']
    requests = [i for i in allUrls if checkCondition(i['request']['url'])]
    tmpUrl = [i for i in requests if checkHasCookies(i)][0]
    
    COOKIES = '; '.join([f'{i["name"]}={i["value"]}' for i in tmpUrl['request']['cookies']])

    with open('cookies.json', 'w') as file:
        file.write(json.dumps({'COOKIES': COOKIES}, indent=4))

    appUrls = set([unquote(i['request']['url']) for i in allUrls if checkCondition(i['request']['url'])])
    # appUrls=[unquote(i.split('data',1)[1]) for i in appUrls]
    sortedUrls = sorted([i for i in appUrls if 'pageId' in i], key=lambda x: getPageId(x))
    d = {
        getPageId(url): url for url in sortedUrls
    }
    sortedUrls = list(d.values())

    with open('urls.json', 'w') as file:
        file.write(json.dumps([[i for i in appUrls if 'pageId' not in i][-1]] + sortedUrls, indent=4))
