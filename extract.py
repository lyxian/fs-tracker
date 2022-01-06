import random
import json
import os

# if __name__ == '__main__':
directory = 'data'
files = os.listdir(directory)
num = random.randint(0, len(files)-1)

# with open(os.path.join(directory, files[0])) as file:
#     items = json.load(file)

# items = data['data']['resultValue']['101102']['data'][0]['items']
# print(data)

file1 = 'data/2022-01-05:12H.json'
file2 = 'data/2022-01-05:18H.json'

with open(file1, 'r') as file:
    items = json.load(file)
    print(f'{file1}: {len(items)}')

with open(file2, 'r') as file:
    items = json.load(file)
    print(f'{file2}: {len(items)}')