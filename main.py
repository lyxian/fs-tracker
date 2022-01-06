import pendulum
import requests
import json
import os
import re

# **********
# * HOW-TO *
# **********
# - append URLs to 'url'
# - update cookies

def saveJSON(filename: str, data: str):
    try:
        with open(filename, 'w') as file:
            file.write(json.dumps(json.loads(data), indent=4, ensure_ascii=False))
        print(f'Data saved in {filename} successfully...')
    except Exception as error:
        print(f'Data not saved due to: {error}')

def getFilename(url):
    text = url.split('data')[-1]
    pageId = 1 if 'pageId' not in text else re.search(r'"pageId":(\d+),', text).group(1)
    return f'data/{pendulum.now().to_date_string()}:{pageId}.json'

def getRequiredCookes(cookies: str):
    return '; '.join(re.search(r'(_m_h5_tk=\w+);.*(_m_h5_tk_enc=\w+)', cookies).groups())

if 0:
    API_URL = 'https://acs-m.lazada.sg/h5/mtop.lazada.pegasus.service.business.fs/1.0/?jsv=2.5.9&appKey=24677475&t=1641311368567&sign=75ee38244cd32930133c59fdbec5ef97&api=mtop.lazada.pegasus.service.business.fs&v=1.0&type=originaljson&isSec=1&AntiCreep=true&timeout=20000&dataType=json&sessionOption=AutoLoginOnly&x-i18n-language=en-SG&x-i18n-regionID=SG&isIcmsMtop=true&parallel=true&isFirstScreenRequest=true&appkey=24677475&data={"isbackup":true,"appId":"101102","backupParams":"language,regionID","flashsaleVersion":3,"language":"zh","regionID":"SG","platform":"pc"}'
    with open('cookies.json', 'r') as file:
        COOKIES = json.load(file)['COOKIES']
    headers = {
        'cookie': getRequiredCookes(COOKIES)
    }
    response = requests.get(API_URL, headers=headers)
    print(json.dumps(json.loads(response.text), ensure_ascii=False))


if __name__ == '__main__':
    if 1:
        TO_AGGREGATE = True
        items = []
        with open('urls.json', 'r') as file:
            API_URLS = json.load(file)
        for API_URL in API_URLS:
            if 'cookies.json' not in os.listdir():
                COOKIES = input('Enter Cookies: ')
                with open('cookies.json', 'w') as file:
                    file.write(json.dumps({'COOKIES': COOKIES}, indent=4))
            else: 
                with open('cookies.json', 'r') as file:
                    COOKIES = json.load(file)['COOKIES']

            headers = {
                'cookie': getRequiredCookes(COOKIES)
            }
            
            response = requests.get(API_URL, headers=headers)
            response_status = json.loads(response.text)['ret'][0]
            if 'SUCCESS' in response_status:
                # aggregate data
                if TO_AGGREGATE:
                    items.extend(json.loads(response.text)['data']['resultValue']['101102']['data'][0]['items'])
                else:
                    saveJSON(getFilename(API_URL), response.text)
            else:
                print(f'Something went wrong...({response_status})\n{API_URL}\n')
                # os.remove('cookies.json')
        if TO_AGGREGATE:
            try:
                filename = pendulum.now().format("YYYY-MM-DD:HH\H")
                with open(f'data/{filename}.json', 'w') as file:
                    file.write(json.dumps(items, indent=4, ensure_ascii=False))
                print(f'Data saved in {filename} successfully...')
            except Exception as error:
                print(f'Data not saved due to: {error}')

    else:
        API_URL = input('Enter URL: ')
        if 'cookies.json' not in os.listdir():
            COOKIES = input('Enter Cookies: ')
            with open('cookies.json', 'w') as file:
                file.write(json.dumps({'COOKIES': COOKIES}, indent=4))
        else: 
            with open('cookies.json', 'r') as file:
                COOKIES = json.load(file)['COOKIES']

        headers = {
            'cookie': getRequiredCookes(COOKIES)
        }
        
        response = requests.get(API_URL, headers=headers)
        response_status = json.loads(response.text)['ret'][0]
        if 'SUCCESS' in response_status:
            saveJSON(getFilename(API_URL), response.text)
        else:
            print(f'Something went wrong...({response_status})')
            os.remove('cookies.json')
