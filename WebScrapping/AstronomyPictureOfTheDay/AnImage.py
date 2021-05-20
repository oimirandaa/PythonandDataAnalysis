from bs4 import BeautifulSoup
import requests
import shutil
from datetime import datetime

#This is a webscrapper that scrapes the image of the day fot the website A Picture of the day of NASA. 
#You enter the date and it gives you the image. 

#This function helps optimize the code for somthing that is repeated for evey option
def printDateandReturn(day, month, year, Months):
    print("The date you chosed is the " + str(day) + 
            " of " + str(Months[month - 1]) + " of " + str(year))

    if(month < 10):
        if(day < 10):
             return str((year-2000)) + "0" + str(month) + "0" + str(day)
        elif(day > 9):
            return str((year-2000)) + "0" + str(month) + "" + str(day)
    elif(month>9):
        if(day < 10):
            return str((year-2000)) + "" + str(month) + "0" + str(day)
        elif(day > 9):
            return str((year-2000)) + "" + str(month) + "" + str(day)

#The following function receives de date by console. It will return a String with the date we need
def dateInput():

    Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    #An array for the months

    print("Please enter the year, from  2015 to today")
    year = int(input())

    #We have to check that the year is valid 
    if(year<2015):
        print("Please enter a year that is valid.")
        dateInput()

    print("Please enter the month from 1 to 12 with the next values:\n"
        + "1 - January \n"
        + "2 - February\n"
        + "3 - March\n"
        + "4 - April\n"
        + "5 - May\n"
        + "6 - June\n"
        + "7 - July\n"
        + "8 - August\n"
        + "9 - September\n"
        + "10 - October\n"
        + "11 - November\n"
        + "12 - December\n")

    month = int(input())

    #Checking the month
    if(month > 12 and month < 1):
        print("You have to choose a valid month")
        dateInput()
    
    #For the Months that have 31 days
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
       
        print("Enter the day between 1 and 31")
        day = int(input())

        if(day<1 or day > 31):
            print("you have to choose a valid day")
            dateInput()
        else:
            date = printDateandReturn(day, month, year, Months)
            return date

    #For the months that have 30 days
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        print("Enter the day between 1 and 30")
        day = int(input())

        if(day < 1 or day > 30):
            print("You have to choose a valid day ")
            dateInput()
        else:
            date = printDateandReturn(day, month, year, Months)
            return date

    #For the month of february
    elif(month == 2):
        #For leap years when february has 29 days
        if(year == 2016 or year == 2020 or year == 2024 or year == 2028 or year == 2032 or year == 2034 or year == 2038):
            print("Please enter the day between 1 and 29")
            day = int(input())

            if(day < 1 or day > 29):
                print("You have to choose a valid day")
                dateInput()
            else:
                date = printDateandReturn(day, month, year, Months)
                return date

        #For February
        else:
            print("Please enter the day between 1 and 28")
            day = int(input())

            if(day < 1 or day > 28):
                print("You have to choose a valid day")
                dateInput()
            else:
                date = printDateandReturn(day, month, year, Months)
                return date

#The following funcion uses the function dateInput() to scrape the image of that date. 
def pictureScrapper():
    #We call the function for the date and we store in a variable
    date = int(dateInput())

    #We check for the date of today so we can find the image that we are looking for
    datetoday = datetime.today().strftime('%Y%m%d')
    datetoday = int(datetoday[2:])

    #We check the date that is before the date of today
    if(date > datetoday):
        print("Choose a date that is before today")
        pictureScrapper()

    #Finally, if the date is valid, we pars it so we use it as a string
    date = str(date)

    #This is the url of the picture
    url = "https://apod.nasa.gov/apod/ap" + date + ".html"
    html_text = requests.get(url).content

    #We call the Soup variable
    soup = BeautifulSoup(html_text, 'html.parser')

    #This try block will try to find the image, if the picture of the day es an image then it will be compleated.
    try:
        #We look for the img type
        images = soup.findAll('img') 

        #This will save the string from the url of the image.
        example = images[0]

        url_base = "https://apod.nasa.gov/apod/" #A base url to find the image
        url_ext = example.attrs['src'] #We extract the url for the image so we can find it

        full_Url = url_base + url_ext #This is the url for the image

        r = requests.get(full_Url, stream=True) #We requests for the url of the image

        if r.status_code == 200: #We make sure that the requests is valid 

            #We store the image in the folder Images and name the pictures as image and the date.
            with open("D:/Proyectos/Python/WebScrapping/AstronomyPictureOfTheDay/Images/image" + date + ".jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

            print("The image was downloaded")

    #The except block will take into acount when there is a video 
    except:
        print("No image was found, the date you chosed is a video")

#This version of the function takes as a parameter the date you want
def pictureScrapper(day, month, year):

    #We check the date that is valid
    if(year < 2015):
        return print("Invalid Year")

    if(month < 1 or month > 12):
        return print("Invalid month")
    elif(month < 10):
        if(day < 1 or day > 31):
            return print("Invalid day")
        elif(day<10):
            date = str(year - 2000) + "0" + str(month) + "0" + str(day)
        elif(day >= 10):
            date = str(year - 2000) + "0" + str(month) + "" + str(day)
    elif(month >= 10):
        if(day < 1 or day > 31):
            return print("Invalid day")
        elif(day<10):
            date = str(year - 2000) + "" + str(month) + "0" + str(day)
        elif(day >= 10):
            date = str(year - 2000) + "" + str(month) + "" + str(day)

    #Parse the date
    date = int(date)

    #We check for the date of today so we can find the image that we are looking for
    datetoday = datetime.today().strftime('%Y%m%d')
    datetoday = int(datetoday[2:])

    #We check the date that is before the date of today
    if(date > datetoday):
        return print("Choose a date that is before today")
        
    #Finally, if the date is valid, we pars it so we use it as a string
    date = str(date)

    #This is the url of the picture
    url = "https://apod.nasa.gov/apod/ap" + date + ".html"
    html_text = requests.get(url).content

    #We call the Soup variable
    soup = BeautifulSoup(html_text, 'html.parser')

    #This try block will try to find the image, if the picture of the day es an image then it will be compleated.
    try:
        #We look for the img type
        images = soup.findAll('img') 

        #This will save the string from the url of the image.
        example = images[0]

        url_base = "https://apod.nasa.gov/apod/" #A base url to find the image
        url_ext = example.attrs['src'] #We extract the url for the image so we can find it

        full_Url = url_base + url_ext #This is the url for the image

        r = requests.get(full_Url, stream=True) #We requests for the url of the image

        if r.status_code == 200: #We make sure that the requests is valid 

            #We store the image in the folder Images and name the pictures as image and the date.
            with open("D:/Proyectos/Python/WebScrapping/AstronomyPictureOfTheDay/Images/image" + date + ".jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

            print("The image was downloaded")

    #The except block will take into acount when there is a video 
    except:
        print("No image was found, the date you chosed is a video")

pictureScrapper()
