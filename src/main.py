from fastapi import FastAPI
import aiohttp

from models import City
from actions_in_db import add_city_db, delete_city_db, get_city_db, get_nearby_cities_db

app = FastAPI()


@app.get("/cities/{city}")
async def get_city_info(city: str):
    result = await get_city_db(city)
    return result


@app.delete("/cities/{city}")
async def delete_city(city: str):
    result = await delete_city_db(city)
    return result


@app.post("/cities")
async def add_city(city: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                    f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
            ) as response:
                response.raise_for_status()
                data = await response.json()
                if not data:
                    return "Координаты города не найдены"
        except aiohttp.ClientError:
            return "Координаты города не найдены"
    latitude, longitude = float(data[0]['lat']), float(data[0]['lon'])
    city_obj = City(name=city, location=[latitude, longitude])
    result = await add_city_db(city_obj)
    return result


@app.get("/cities/nearby/latitude/longitude")
async def get_nearby_cities(latitude: float, longitude: float):
    return await get_nearby_cities_db(latitude, longitude)
