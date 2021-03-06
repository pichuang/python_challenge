__author__ = 'root'

import urllib3
import os
import re
from collections import Counter

def download(src):
    http = urllib3.PoolManager()
    with http.urlopen('GET', src) as request_data:
        return request_data

# Write file
if not os.path.isfile("2.txt"):
    print("2.txt is not exist")

    # Open connection
    request = download("http://www.pythonchallenge.com/pc/def/ocr.html")
    with open("2.txt", "wb") as file:
        file.write(request.data)

# Read file
with open("2.txt", "r") as file:
    read_file = file.read()

# Get mess below
data = re.findall('<!--(.+?)-->', read_file, re.S)[-1]


'''
Normal Cunter
'''
# Count char
# counts = {}
# for char in data:
#     counts[char] = counts.get(char, 0) + 1
# print(counts)

'''
Use Collection Counter
'''
#data_dict = dict(Counter(data))
#print(data_dict)


# Only print rare char
print("Answer: {0}".format(''.join(re.findall('[a-z]', data))))

