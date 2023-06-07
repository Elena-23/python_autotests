from faker import Faker
import requests


token = '21aaef743c13c59081c1e8fd37aff8c2'
host = 'https://pokemonbattle.me:9104'
faker = Faker()
pokemon_name = faker.name()


response = requests.post(f'{host}/pokemons', json = 
                     {                       
    "name": pokemon_name,
    "photo": "https://dolnikov.ru/pokemons/albums/055.png",
    }, headers= {"Content-Type" : "application/json", "trainer_token": token})

if response.status_code == 201:
    pokemon_id = response.json()['id']
    print(response.json())


    put_response = requests.put(f'{host}/pokemons', json = 
                     {
    "pokemon_id": pokemon_id,
    "name": "Пирожок",
    "photo": "https://dolnikov.ru/pokemons/albums/055.png",
    }, headers= {"Content-Type" : "application/json", "trainer_token": token})

    
    print(put_response.json())

    pokeball_response = requests.post(f'{host}/trainers/add_pokeball', json = 
                     {
       "pokemon_id": pokemon_id,
       }, headers= {"Content-Type" : "application/json", "trainer_token": token})

    print(pokeball_response.json())







   

