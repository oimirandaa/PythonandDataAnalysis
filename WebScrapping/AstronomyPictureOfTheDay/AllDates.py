#This program will scrape all the dates from the website so we can extract all the pictures since 2015
from bs4 import BeautifulSoup
import requests
import shutil
from datetime import datetime

#This Function scrapes all the dates that have an image for APOD
def dates():

    #Url for the Page
    url = "https://apod.nasa.gov/apod/archivepix.html"

    #We Scrap the page
    htmlText = requests.get(url).content

    soup = BeautifulSoup(htmlText, 'html.parser')

    fechas = soup.find_all('b')

    #We save the data in a list
    scrap = []
    for fecha in fechas: 
        scrap.append(fecha.text)

    #But we only need the second entry
    dates = scrap[1]

    #With this method, we divide the long string with all the dates and titles into a list where every entry is a date with title
    dates = dates.splitlines()

    #We delete an empty cel
    del dates[0]

    #We create a new array where we separate the date from the title 
    newDates = []
    for date in dates: 
        #This is a tuple where we store the three elements, but we only need the date
        part = date.partition(':')
        newDates.append(part[0])

    return newDates
    
for date in dates():
    print(date)