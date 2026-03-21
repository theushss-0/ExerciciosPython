import pandas as pd
import requests



url = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


response = requests.get(url, headers=headers)


dfs = pd.read_html(response.text)


print(dfs[0].head)
print(len(dfs))


