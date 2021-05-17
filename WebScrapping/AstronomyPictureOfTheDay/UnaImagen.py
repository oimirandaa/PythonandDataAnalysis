from bs4 import BeautifulSoup
import requests
import shutil

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

