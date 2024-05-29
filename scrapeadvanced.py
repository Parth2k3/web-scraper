import requests
from bs4 import BeautifulSoup
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36'
}
url = "https://www.scrapethissite.com/pages/advanced/?gotcha=headers"

response  = requests.get(url, headers=headers)
text = response.text
soup = BeautifulSoup(text, 'html.parser')
container = soup.find('div', class_ = 'row')
content = container.find('div', class_ = 'col-md-4').text.strip()
print(content,'\n')

url2 = "https://www.scrapethissite.com/pages/advanced/?gotcha=login"
response2  = requests.get(url2, headers=headers)
text2 = response2.text
soup2 = BeautifulSoup(text2, 'html.parser')
print(soup2)

#The site requires login credentials for login and csrf token inclusions' scraping.