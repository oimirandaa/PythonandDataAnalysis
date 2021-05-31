from bs4 import BeautifulSoup
import requests
import shutil
from datetime import datetime, date

#This version of the function scrapes the picture for today 
def pictureScrapper():
    #We check for the date of today so we can find the image that we are looking for
    today = date.today()
    datetoday = datetime.today().strftime('%Y%m%d')
    date1 = int(datetoday[2:])

    #Finally, if the date is valid, we pars it so we use it as a string
    date1 = str(date1)

    #This is the url of the picture
    url = "https://apod.nasa.gov/apod/ap" + date1 + ".html"
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
            with open("D:/DesktopImages/image" + date1 + ".jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

            print("The image for " + str(today) + " was downloaded")

    #The except block will take into acount when there is a video 
    except:
        print("No image was found, the date " + str(today) + "is a video")

pictureScrapper()