import sys
import requests

es_url = sys.argv[1]
filename = sys.argv[2]

doc_num = 1
with open(filename) as f:
    for line in f:
        requests.post(url=es_url + '/articles/article', data=line)
        print('Added document:\t' + str(doc_num))
        doc_num += 1
