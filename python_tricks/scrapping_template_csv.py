# imports
import csv
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# site to be scraped
url = ''

try:

    # get the html
    html = urlopen(url)

    # error handling
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found.")
else:
    # create the file and the headers
    with open('tyres.csv', 'w') as file:
        writer = csv.writer(file)

        # what are the headers like below:
        # fields = ['Title', 'Description', 'Price']
        # writer = csv.DictWriter(file, fieldnames=fields)
        # writer.writeheader()

        # or like this (simpler)
        writer.writerow(['title', 'description', 'price'])

        # parse with BeautifulSoup
        bs = BeautifulSoup(html, 'html.parser')

        # search for the data i want
        data = bs.findAll('tag')
        # tag.attrs['href']

        # for loop to write each element in the file
        for element in data:
            data1 = element.find('a', {'class': 'js-sku-link'}).attrs['title']

            data2 = element.find('p', {'class': 'specs'}).get_text()

            data3 = element.find(
                'a', {'class': 'js-sku-link sku-link'}).get_text()

            # this goes with the dictionary writer
            # writer.writerow(
            # {'Title': title, 'Description': description, 'Price': price})

            # or like this (simpler)
            writer.writerow([data1, data2, data3])
