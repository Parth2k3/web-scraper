import requests
from bs4 import BeautifulSoup
from database.database import insert_data, delete_database

names = []
years = []
wins = []
losses = []
otlosses = []
gfs = []
gas = []
diffs = []


for page in range(1,7):

    url = f"https://www.scrapethissite.com/pages/forms/?page_num={page}&per_page=100"

    response = requests.get(url)
    text = response.text

    soup = BeautifulSoup(text, 'html.parser')
    table = soup.find('table', class_ = 'table')

    team_names = table.find_all('td', class_ = 'name')
    for name in team_names:
        names.append(name.text.strip())

    team_years = table.find_all('td', class_ = 'year')
    for year in team_years:
        years.append(year.text.strip())


    team_wins = table.find_all('td', class_ = 'wins')
    for win in team_wins:
        wins.append(win.text.strip())


    team_losses = table.find_all('td', class_ = 'losses')
    for loss in team_losses:
        losses.append(loss.text.strip())

    team_otlosses = table.find_all('td', class_ = 'ot-losses')
    for otloss in team_otlosses:
        otlosses.append(otloss.text.strip())


    team_gfs = table.find_all('td', class_ = 'gf')
    for gf in team_gfs:
        gfs.append(gf.text.strip())

    team_gas = table.find_all('td', class_ = 'ga')
    for ga in team_gas:
        gas.append(ga.text.strip())

    team_diffs = table.find_all('td', class_ = 'diff')
    for diff in team_diffs:
        diffs.append(diff.text.strip())

    
json = []
for i in range(len(names)):
    dict = {
        'name': names[i],
        'year':years[i],
        'wins':wins[i],
        'losses':losses[i],
        'otlosses':otlosses[i],
        'gf':gfs[i],
        'ga':gas[i],
        'diff':diffs[i]
    }
    json.append(dict)



result = insert_data('teams', json)
print(result)

# delete_database('teams')