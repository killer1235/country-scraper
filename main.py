import bs4 as bs
import requests

url = 'https://scrapethissite.com/pages/simple/'

country = input("Enter country name to get data for .\n")

page = requests.get(url)

soup = bs.BeautifulSoup(page.content , 'html.parser')

for row in soup.find_all('div' , class_='row'):

    row.find_all('div' , class_='col-md-4 country')

    for col in row.find_all('h3' , class_='country-name'):
        
        text = col.get_text().strip()

        country.strip()
        if text == country:
            nextnode = col.find_next('div')

            capital = nextnode.find('span'  , class_='country-capital')
            population = nextnode.find('span' , class_='country-population')
            area = nextnode.find('span' , class_='country-area')

            print("Captial: " + capital.get_text().strip() + '\n')
            print( "Area(km2): "+ area.get_text().strip() + '\n'  )
            print("Population: "+ population.get_text().strip() + '\n')
        

        

