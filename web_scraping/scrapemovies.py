import requests
from database.database import insert_data, delete_database

def scrapemovies():
    url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015"
    response = requests.get(url)
    final_json = response.json()
    headings = ['title', 'year', 'awards', 'nominations']

    for year in range(2010,2015):
        url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={year}"
        response = requests.get(url)
        json = response.json()
        for element in json:
            final_json.append(element)
    print('successfully scraped movies page')
    result = insert_data('movies', final_json)
    print(result)
    return result
#delete_database('movies')