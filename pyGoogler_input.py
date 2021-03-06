#VERSION 0.1
#UNSTABLE, MESSY
#OUTPUTS [queryInput].csv in working folder


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from googlesearch import search
import csv
import string
import re

print('Enter search query')
queryInput = input()
csvFilename = queryInput.replace(' ', '_') + '.csv'
i = 1
result_list = []
    
def scrapeTitle(url):
    try:
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url,headers=hdr)
        page = urlopen(req, timeout = 10)
        soup = BeautifulSoup(page.read().decode('utf-8', 'ignore'), "html.parser")
        return soup.title.text
    except Exception as error:
        return 'ERROR:' + str(error);
        pass     

for url in search(queryInput,        # The query you want to run
#                tld = 'com',  # The top level domain
#                lang = 'en',  # The language
#                start = 0,    # First result to retrieve
#                stop = 20,  # Last result to retrieve
            num = 10,     # Number of results per page
            pause = 5.0,  # Lapse between HTTP requests
           ):
    result = []
    
    title = re.sub(r'[\n\r\t]*', '', scrapeTitle(url))
    if 'ERROR:' in title:
        errorMsg = title
        title = ""
        result = ([i, title, url, errorMsg])
    else:
        result = ([i, title, url])
    
    result_list.append(result)
    data = [result]
    wr = open(csvFilename, 'a', newline ='')
    with wr:
        write = csv.writer(wr)
        write.writerows(data)
    print(result)
    print(" ")
    i += 1
