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
    
#This functions transforms the month in the tuple into a number between 1 and 12
def Months(Month):
    Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if(Month == Months[0]):
        month = "01"
    elif(Month == Months[1]):
        month = "02"
    elif(Month == Months[2]):
        month = "03"    
    elif(Month == Months[3]):
        month = "04"
    elif(Month == Months[4]):
        month = "05"
    elif(Month == Months[5]):
        month = "06"
    elif(Month == Months[6]):
        month = "07"
    elif(Month == Months[7]):
        month = "08"
    elif(Month == Months[8]):
        month = "09"
    elif(Month == Months[9]):
        month = "10"
    elif(Month == Months[10]):
        month = "11"
    elif(Month == Months[11]):
        month = "12"
    
    return month

#This function returns a list with al the dates in the format we want. 
def cleanDates():

    cleanDates = []

    #This is the actual cleaning.
    for date in dates():

        cleanDate = date.split()

        #This part, transformas the year of the tuple into a number with only two numbers, Like we need it. 
        year = int(cleanDate[0])
    
        year = str(year - 2000)

        #We need to transform the month into a number 
        month = Months(cleanDate[1])

        #We Parse the day 
        day = str(cleanDate[2])

        #We combine them 

        cleanDates.append(year + month + day)

    return cleanDates

