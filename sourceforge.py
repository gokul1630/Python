import io
import requests
from bs4 import BeautifulSoup
import extras
from os import rename, path, remove
import schedule
import time

def scrape():
    if path.exists('web.txt'):
        rename('web.txt', 'web_old.txt')
    URL = 'https://sourceforge.net/p/x00td-stuff/activity/?page=0&limit=100#5e2e8676ee24ca77d4cd6a51'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='content_base')
    job_elems = results.findAll("div", {"class": "activity"})
    with open('web.txt', 'w') as o:
        for group in job_elems:
            devices = group.findAll("a")
            for device in devices:
                o.write(device.text +"\n")
    line1=open("web.txt","r")
    line2=open("web_old.txt","r")
    a=line1.readline()
    a=line1.readline()
    b=line2.readline()
    b=line2.readline()
    if a==b:
        pass
    else:
          f = open("web.txt")
          m = f.readline()
          m =f.readline()  
          chat="Enter chat id here"
          print(m)
          print("Link :")
          print("\nhttps://sourceforge.net/projects/x00td-stuff/files"+m+"/download")
          requests.get(f"https://api.telegram.org/" enter BotAPI-Key"/sendMessage?chat_id={chat}&text={m}") 
    line1.close()
    line2.close()
    remove('web_old.txt') 
schedule.every(1).seconds.do(scrape)
while 1:
	schedule.run_pending()
	time.sleep(1)