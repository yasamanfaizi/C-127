from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser  = webdriver.Chrome("./chromedriver")
browser.get(url)
time.sleep(10)
def collect():
    headers = ["name", "lightyears from earth", "planet mass", "stellar magnitude", "discovery date"]
    planets = []
    for i in range(491):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for y in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            li = y.find_all("li")
            temp = []
            for a,b in enumerate(li):
                if a == 0:
                    temp.append(b.find_all("a")[0].contents[0])
                else:
                    try: 
                        temp.append(b.contents[0])
                    except: 
                        temp.append("")
            planets.append(temp)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("info.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(planets)
collect()