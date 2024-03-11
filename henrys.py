# requests - for HTML connections
# bs4 (BeautifulSoup4) - for parsing the HTML content of the numerous websites
# csv - for writing output into a csv file
import requests
from bs4 import BeautifulSoup as bs
import csv

# page = 1
# while page !=50:
#     url = f'{photo_video}?page={page}'
#     print(url)
#     page += 1

# A list of 'root' websites from Henry's Camera Photo.
promos = 'https://www.henryscameraphoto.com/promos'
photo_video = 'https://www.henryscameraphoto.com/photo-video'
accessories = 'https://www.henryscameraphoto.com/accessories'
drones = 'https://www.henryscameraphoto.com/drones'
cine_gears = 'https://www.henryscameraphoto.com/cine-gears'

website_array = [photo_video, accessories, drones, cine_gears]

full_html = ''

# For loop to get all html files and append the output on variable full_html
page = 1

for website in website_array:
    while page != 50:
        url = f'{website}?page={page}'
        page_to_scrape = requests.get(website)
        soup = bs(page_to_scrape.text, 'html.parser')
        full_html += str(soup)
    page = 1

soup = bs(full_html, 'html.parser')

# Variable that selects the output for the script
items = soup.select('h4>a')
prices = soup.findAll('span', attrs={'class':'price-new'})

# Creates a .csv file to write the outputs (ITEM, PRICE)
file = open('henrys_scraped.csv', 'w', encoding='UTF-8')
writer = csv.writer(file)

writer.writerow(['ITEM', 'PRICE'])

# A for loop to print the output and to write it in the .csv file
for item, price in zip(items,prices):
    print(item.text + ' - ' + price.text)
    writer.writerow([item.text, price.text])