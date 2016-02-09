from bottle import route, run, template
import requests
from bs4 import BeautifulSoup
import os 
import string
import re
URL1 = "http://public.mig.kz/"
eur = ""
usd = ""
rub = ""
non_decimal = re.compile(r'[^\d.]+')
@route('/')
def index():
    resp = requests.get(URL1)
    bs4 = BeautifulSoup(resp.content,"html.parser")
    result = None
    tags = bs4.find_all('h4')
    for tag in tags:
    	h4 =""
    	ul = ""
    	if tag.string =='usd':
    		usd = non_decimal.sub("",tag.parent.p.string)
    	if tag.string =='eur':
    		eur = non_decimal.sub("",tag.parent.p.string)
    	if tag.string =='rub':
    		rub = non_decimal.sub("",tag.parent.p.string)
    	
    
    return {"usd": usd, "eur": eur, "rub": rub}


URL = "https://github.com/giAtSDU/apt_spring_2016_hw1"

@route('/forks')
def forks():
    resp = requests.get(URL)
    bs4 = BeautifulSoup(resp.content, "html.parser")
    res = None
    for tag in bs4.find_all('a'):
        if tag.has_attr('class') and 'social-count' in tag.attrs['class']:
            res = int(tag.string)
    return {"forks": res}

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
