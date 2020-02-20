#!/data/data/com.termux/files/usr/bin/python
from os import rename, path, remove
import io
import requests
from bs4 import BeautifulSoup
import schedule
import datetime
import time

def scrape():
    if path.exists('/sdcard/result.txt'):
        rename('/sdcard/result.txt', '/sdcard/result_old.txt')    
    page = requests.get('https://economictimes.indiatimes.com/indices/nifty_50_companies')
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='pageContent')
    elements = results.findAll("div", {"id": "headStuff"})
    with open('result.txt', 'w') as o:
        for group in elements:
            html = group.findAll("div")
            for css in html:
                o.write(css.text +"\n")
    line1=open("result.txt","r",encoding='UTF-8')
    line2=open("result_old.txt","r",encoding='UTF-8')
    file1=line1.readline()
    file2=line2.readline()
    if file1==file2:
	    print ("same")
    else:
        f=open("result.txt","r")
        name=f.read()
        print(name)
        a=datetime.datetime.now()
        b=(a.strftime("Time: %H:%M\nNifty: "+name))
        chat='chat id here'
        requests.get(f"https://api.telegram.org/bot"botAPI-key"/sendMessage?chat_id={chat}&text={b}") 
    line1.close()
    line2.close()
    remove ('result_old.txt')
schedule.every(1).seconds.do(scrape)
while 1:
	schedule.run_pending()
	time.sleep(0)
