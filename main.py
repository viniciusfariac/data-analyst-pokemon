import requests
import pandas as pd 
from utils import clear_data

def pegar_pokemon(qtd):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={qtd}"
    response = requests.get(url)
    data = response.json()

    pokemons = []

    for item in data["results"]:
        details = requests.get(item["url"]).json()
        pokemons.append({
            "id": details['id'],
            "name": details['name'],
            "height": details['height'],
            "weight": details['weight'],
            "base_experience": details['base_experience']
        })
    
    return pd.DataFrame(pokemons)

def saving_csv(df, caminho="data/pokemons.csv"):
    df.to_csv(caminho, index=False)
    print(f"CSV salvo com sucesso {caminho}")



if __name__ == "__main__":
    number = int(input("number of Pokémon searched: "))
    print("starting")
    df = pegar_pokemon(number)

    print("clean datas")
    df_clean = clear_data(df)

    print("saving csv")
    saving_csv(df_clean)