import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
def pokemon_scraping():
    url = "https://pokemondb.net/pokedex/game/x-y"
    headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    r = requests.get(url, headers=headers)

    time.sleep(2)

    soup = BeautifulSoup(r.content, 'html.parser')

    pokemon = {'name': [], 'type': []}
    poke = soup.find_all("span", class_="infocard-lg-data text-muted")

    for i in poke:
        name = i.find("a", class_="ent-name").text
        pokemon['name'].append(name)
        tp = i.find("br")
        tp = tp.find_next("small")
        tp = tp.find_all("a", class_="itype")
        pokemon['type'].append(tp)

    for i in range(len(pokemon['type'])):
        for j in range(len(pokemon['type'][i])):
            pokemon['type'][i][j] = pokemon['type'][i][j].text
        
        pokemon['type'][i] = ' '.join(pokemon['type'][i])
        pokemon['type'][i] = pokemon['type'][i].lower()

    scrape = []

    for i in range(len(pokemon['name'])):
        scrape.append({'name': pokemon['name'][i], 'type': pokemon['type'][i]}) 
    
    return scrape