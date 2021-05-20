from bs4 import BeautifulSoup
import requests
import shutil

#This is a webscrapper that scrapes the image of the day fot the website A Picture of the day of NASA. 
#You enter the date and it gives you the image. 

#The following function receives de date by console
def dateInput():

    Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print("Please enter the year, from  2015 to today")
    year = int(input())

    if(year<2015):
        print("Please enter a year that is valid.")
        dateInput()

    print("Please enter the month from 1 to 12 with the next values:\n "
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
            print("The date you chosed is the " + day + 
            " of " + Months[month - 1] + " of " + year)

            return day + "/" + month + "/" + year

    #For the months that have 30 days
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        print("Enter the day between 1 and 30")
        day = int(input())

        if(day < 1 or day > 30):
            print("You have to choose a valid day ")
            dateInput()
        else:
            print("The date you chosed is the " + day + 
            " of " + Months[month - 1] + " of " + year)

            return day + "/" + month + "/" + year

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
                print("The date you chosed is the " + day + 
                " of " + Months[month - 1] + " of " + year)

                return day + "/" + month + "/" + year

        else:
            print("Please enter the day between 1 and 28")
            day = int(input())

            if(day < 1 or day > 28):
                print("You have to choose a valid day")
                dateInput()
            else:
                print("The date you chosed is the " + day + 
                " of " + Months[month - 1] + " of " + year)

                return day + "/" + month + "/" + year


dateInput()

url = "https://apod.nasa.gov/apod/ap210515.html"
html_text = requests.get(url).content

soup = BeautifulSoup(html_text, 'html.parser')

images = soup.findAll('img') 

example = images[0]

url_base = "https://apod.nasa.gov/apod/"

url_ext = example.attrs['src']

full_Url = url_base + url_ext
 
print(full_Url)

r = requests.get(full_Url, stream=True)

if r.status_code == 200:

    with open("D:/Proyectos/Python/WebScrapping/AstronomyPictureOfTheDay/Images/imagen.jpg", 'wb') as f:

        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

