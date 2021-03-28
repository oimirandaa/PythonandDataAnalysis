import requests 
from bs4 import BeautifulSoup as bs

#This file will give you the link of the image of the user of github that is requested. It does not save it.
github_user = input('Input github User: ')
url = 'https://github.com/' + github_user
r = requests.get(url)

soup = bs(r.content, 'html.parser')

#This line extracts the link
profile_image = soup.find('img', {'alt':'Avatar'})['src']

print(profile_image)