from httpx import AsyncClient, Request
from asyncio import run

import json


# async def get_homeworld() -> dict:


async def get_starships() -> dict:
    async with AsyncClient() as client:
        response = await client.get("https://swapi.dev/api/people/?page=1")
        return response.json()
    

async def save_starships() -> None:
    with open("data.json", "w") as data:
        json.dump(await get_starships(), data, indent=4)


async def main():
    print(await save_starships())


if __name__ == "__main__":
    run(main())