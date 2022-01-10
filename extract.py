import pandas
import json

# if __name__ == '__main__':
directory = 'data'

file1 = 'data/2022-01-08:12H.json'
file2 = 'data/2022-01-08:18H.json'

keys = [
    'itemId',
    'itemTitle',
    'itemUrl',
]

def getNames(filename):
    with open(filename, 'r') as file:
        items = json.load(file)

    return pandas.DataFrame(sorted([{k:v for k,v in item.items() if k in keys} for item in items], key=lambda x: x['itemId']))

if __name__ == '__main__':
    df1 = getNames(file1)
    df2 = getNames(file2)

    df1.to_csv('df1.csv', index=False)
    df2.to_csv('df2.csv', index=False)

    # print(d)