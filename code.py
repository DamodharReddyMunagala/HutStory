import urllib.request as urlRequest
import urllib.parse as urlParse
from bs4 import BeautifulSoup
import pandas as pd
import re
import pymongo
from pymongo import MongoClient

page_links = []
architects_url = []
global A,B,D,G,H,J,K,M

A = []
B = []
D = []
G = []
H = []
J = []
K = []
M = []
page1 = "http://www.justdial.com/Vijayawada/Architects/ct-10020039"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
req = urlRequest.Request(page1, headers = headers)
html = urlRequest.urlopen(req)
soup = BeautifulSoup(html, 'lxml')

for item in soup.find('div', {'class' : 'fcon'}).findAll('a', href = re.compile('^(http://www.justdial.com/Vijayawada/Architects/ct-10020039/page-)')):
    #This loop is used to get the link of the pages that are hidden
    if item.attrs['href'] in page_links:
        pass
    else:
        page_links.append(item.attrs['href'])


def htmlPage(url):
    
        ###This function is used to get the html content of the webpage
    
    # pretend to be a chrome 47 browser on a windows 10 machine
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    req = urlRequest.Request(url, headers = headers)
    htmlParse(req)

# pretend to be a chrome 47 browser on a windows 10 machine
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
#req = urlRequest.Request(url, headers = headers)
# open the url

def htmlParse(req):
    
        ###This function is used to get the links of each and every person(here Architect)
    
    html = urlRequest.urlopen(req)
    soup = BeautifulSoup(html, 'lxml')

    #for data in soup.find('ul', {'class' : 'rsl col-md-12 padding0'}).findAll('li',{'class' : 'cntanr'}):
    #   for link in (data.findAll('a',{'class' : 'rating_div'})):
    #        print (link.attrs['href'])
    
    for link in soup.findAll('div',{'class' : 'col-sm-6 col-xs-8 store-details sp-detail paddingR0'}):
        for ele in link.find('h4').find('span',{'class':'jcn'}):
            architects_url.append(ele.attrs['href'])

htmlPage(page1)

for link in page_links:
    htmlPage(link)


def getDetails(final_link):
    
        ###This function is used to get the detailsof the every person(here Architect)
    
    url = final_link
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    req = urlRequest.Request(url, headers = headers)
    html = urlRequest.urlopen(req)
    soup = BeautifulSoup(html, 'lxml')
    
    C = []
    E = []
    F = []
    I = []
    L = []
    N = []
    WorkingHours = {}
    
    try:
        for ele in soup.find('div', {'class' : 'col-sm-9 col-xs-12'}).findAll('h1',{'class' : 'rstotle'}):
            if ele is None:
                A.append('None')
            else:
                for data in ele.find('span', {'class' : 'item'}).find('span', {'class' : 'fn'}):
                    if data is None:
                        A.append('None')
                    else:
                        A.append(data)
                        
    except AttributeError as e:
        A.append('None')

    try:
        for ele in soup.find('div', {'class' : 'col-sm-9 col-xs-12'}).findAll('div', {'itemprop' : 'aggregateRating'}):
            if ele is None:
                B.append('None')
            else:
                for data in ele.find('span',{'class' : 'total-rate'}).find('span', {'class' : 'value-titles'}):
                    if data is None:
                        B.append('None')
                    else:
                        B.append(data)
    except AttributeError as e:
        B.append('None')

    try:
        for ele in soup.find('div', {'class' : 'col-sm-9 col-xs-12'}).findAll('ul', {'class' : 'rstocnct'}):
            if ele is None:
                C.append('None')
            else:
                for att in ele.findAll('p',{'class' : 'jrcw'}):
                    if att is None:
                        C.append('None')
                    else:
                        for data in att.findAll('span', {'class' :'telCntct'}):
                            if data is None:
                                C.append('None')
                            else:
                                Z = ''
                                if data is None:
                                    C.append('None')
                                else:
                                    for item in data.findAll('a'):
                                        if item is None:
                                            Z = Z + 'None' + ''
                                        else:
                                            Z = Z + str(item.text) + ' '
                                    C.append(Z)
    except AttributeError as e:
        C.append('None')

    try:
        for ele in soup.find('div', {'class' : 'col-sm-4 col-xs-12 padding0 leftdt'}).findAll('ul', {'id' : 'comp-contact'}):
            if ele is None:
                D.append('None')
            else:
                for data in ele.find('span',{'itemprop' : 'streetAddress'}):
                    if data is None:
                        D.append('None')
                    else:
                        D.append(data)
    except AttributeError as e:
        D.append('None')

    for ele in soup.find('div', {'class' : 'col-sm-4 col-xs-12 padding0 leftdt'}).findAll('li', {'onclick' : "_ct('alsolstdin', 'dtpg');"}):
        if ele is None:
            I.append('None')
        else:
            for data in ele.findAll('span', {'style' : 'display:none;'}):
                Z = ''
                if data is None:
                    I.append('None')
                else:
                    for item in data.findAll('a'):
                        if item is None:
                            Z = Z + 'None' + ''
                        else:
                            Z = Z + str(item.text).replace('\r\n\t\t\t\t', ' * ')
                    I.append(Z)

    for ele in soup.find('div', {'class' : 'col-sm-4 col-xs-12 padding0 leftdt'}).findAll('div', {'id' : "mhd"}):
        if ele is None:
            E.append('None')
            F.append('None')
        else:
            for data in ele.find('ul', {'id' : 'statHr'}).findAll('li'):
                if data is None:
                    E.append('None')
                    F.append('None')
                else:
                    Z = ''
                    Y = ''
                    if data is None:
                        E.append('None')
                        F.append('None')
                    else:
                        cells = data.findAll('span')
                        try:
                            E = cells[0].find(text = True).strip()
                            F = cells[1].find(text = True).strip()
                        except AttributeError as e:
                            E = 'None'
                            F = 'None'
                        WorkingHours[E] = F
                        
    for data in soup.find('div', {'class' : 'col-sm-4 col-xs-12 padding0 leftdt'}).findAll('div', {'class' : 'mreinfwpr'}):
        if data is None:
            L.append('None')
        else:
            for item in data.findAll('p', {'class' : 'mreinfp'}):
                if item is None:
                    L.append('None')
                else:
                    if item.text == 'Year Established':
                        for item in data.find('ul', {'class' : 'alstdul'}).find('li'):
                            L.append(item)
                    else:
                        pass

    #print (WorkingHours)                
    G.append(WorkingHours)
    J.append(' '.join(I))
    M.append(''.join(L))
    K.append(' '.join(C))
    N.append(' '.join(A))  
    

for detail in architects_url:
    getDetails(detail)
    
print (len(architects_url))

#for link in page_links:
    #print(link)

df=pd.DataFrame(A, columns = ['Builder Name'])
df['Builder Rating'] = B
df['Phone Numbers'] = K
df['Address'] = D
df['Work They Do'] = J
df['WorkingHours'] = G
df['Year Established'] = M 
df.to_csv('hutstory_vijayawada_architects.csv',index=True,header=True) #Used to create a DataFrame

client = MongoClient()
db = client.hutStory_database
collects = db.collects
for i in range(len(A)):
    collect = {"Builder Name" : A[i],
            "Builder Rating" : B[i],
            "Phone Numbers" : K[i],
            "Address" : D[i],
            "Work They Do" : J[i],
            "Working Hours" : G[i],
            "Year Established" : M[i],}
    collect_id = collects.insert_one(collect).inserted_id

print (db.collection_names(include_system_collections=False))

for data in collects.find({"Builder Rating" : "4.8"}):
    print (data)
