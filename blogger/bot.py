import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

links = []

def getUa():
    o = open("user").read()
    r = random.choice(o.splitlines())
    return r

#def getLink1():
#    links = ["https://www.billalblogs.me/2020/06/belajar-arduino-part-1.html", "https://www.billalblogs.me/2020/05/pengertian-subnet-mask.html"]
#    return random.choice(links)
    
def getAllLink():
    global links
    r = requests.get("https://www.billalblogs.me")
    b = BeautifulSoup(r.text, "html.parser")
    f = b.findAll("h2", {"class": "post-title entry-title"})
    for a in f:
        link = a.find("a").get("href")
        links.append(link)

def getLink():
    getAllLink()
    return random.choice(links)

def delay(timer, url):
    for second in range(timer, 0, -1):
        print (f"\r[{a}] Tunggu: {second} detik -> proses", end="", flush=True)
        sleep(1)
    print (f" -> sukses -> {url}")

def main(url):
    opt = Options()
    opt.add_argument("user-agent=" + getUa())
    browser = webdriver.Chrome()
    
    browser.get(url)
    delay(20, url)
    browser.quit()
a = 0
while True:
    a += 1
    url = getLink()
    main(url)