from httpx import AsyncClient, Request
from asyncio import run

import json


async def get_homeworld(homeworld: str) -> dict:
    async with AsyncClient() as client:
        response = await client.get(homeworld)
        return response.json()


async def get_character() -> dict:
    async with AsyncClient() as client:
        response = await client.get("https://swapi.dev/api/people/?page=1")
        return response.json()
    

async def save_starships() -> None:
    with open("data.json", "w") as data:
        json.dump(await get_character(), data, indent=4)


async def task_1():
    character = await get_character()
    character = character["results"][0]

    name = character["name"]
    height = character["height"]
    mass = character["mass"]
    hair_color = character["hair_color"]

    print(f"{name=}", sep="\n")
    print(f"{height=}", sep="\n")
    print(f"{mass=}", sep="\n")
    print(f"{hair_color=}", sep="\n")


async def task_2():
    character = await get_character()
    character_home_link = character["results"][0]["homeworld"]
    character = character["results"][0]["name"]

    character_home = await get_homeworld(character_home_link)
    character_home = character_home["name"]

    print(f"{character} was born on {character_home}.")


async def task_3():
    ...


async def main():
    await task_1()
    await task_2()



if __name__ == "__main__":
    run(main())