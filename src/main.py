from prefect import flow, task
from prefect.futures import wait
import requests
from random import randint
from models import Character, Episode, Location

@task
def get_rick_and_morty_character(id: int = randint(1, 826)) -> Character:
    '''
    Get a Rick and Morty character from the rickandmortyapi
    Link: https://rickandmortyapi.com/documentation/

    Defaults to a random Rick and Morty character
    '''
    response = requests.get(f'https://rickandmortyapi.com/api/character/{id}')
    print(response)
    character = Character(**response.json())
    return character

@task
def get_rick_and_morty_episode(id: int = randint(1, 51)) -> Episode:
    '''
    Get a Rick and Morty episode from the rickandmortyapi
    Link: https://rickandmortyapi.com/documentation/

    Defaults to a random Rick and Morty episode
    '''
    response = requests.get(f'https://rickandmortyapi.com/api/episode/{id}')
    print(response)
    episode = Episode(**response.json())
    return episode

@task
def get_rick_and_morty_location(id: int = randint(1, 126)) -> Location:
    '''
    Get a Rick and Morty location from the rickandmortyapi
    Link: https://rickandmortyapi.com/documentation/

    Defaults to a random Rick and Morty location
    '''
    response = requests.get(f'https://rickandmortyapi.com/api/location/{id}')
    print(response)
    location = Location(**response.json())
    return location

@flow
def get_rick_and_morty_character_episodes(id: int = randint(1, 826)) -> list[Episode]:
    '''
    Get the episodes associated to a particular Rick and Morty character
    Link: https://rickandmortyapi.com/documentation/

    Defaults to a random Rick and Morty character
    '''
    rick_and_morty_character = get_rick_and_morty_character(id=id)
    locations = [get_rick_and_morty_episode.submit(id=int(episode.split('/')[-1])) for episode in rick_and_morty_character.episode]
    wait(locations)


if __name__ == '__main__':
    get_rick_and_morty_character_episodes(id = 8)