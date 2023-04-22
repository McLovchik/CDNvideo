from connect_to_db import get_cities_collection
from models import City
from pymongo.errors import WriteError
from geopy.distance import geodesic
from fastapi.responses import JSONResponse


async def add_city_db(city: City):
    """Add city in db"""
    city_dict = city.dict()
    collection = get_cities_collection()
    try:
        result = await collection.insert_one(city_dict)
        if result.acknowledged:
            return f"Город {city_dict.get('name')} успешно добавлен"
    except WriteError as e:
        return f"Город {city_dict.get('name')} уже существует в базе данных"
    return "Неизвестная ошибка"


async def delete_city_db(city: str):
    """Delete city in db"""
    collection = get_cities_collection()
    result = await collection.delete_one({"name": city})
    if result.deleted_count == 1:
        return "Город удален"
    else:
        return "Город не найден"


async def get_city_db(city: str):
    """Get city from db"""
    collection = get_cities_collection()
    result = await collection.find_one({"name": city})
    if result is None:
        return 'Такого города в базе нет'
    return {'name': result['name'], 'location': result['location']}


async def get_nearby_cities_db(latitude: float, longitude: float):
    """Get nearest cities by given coordinates"""
    collection = get_cities_collection()
    cursor = collection.find({})
    cities = []
    async for document in cursor:
        city_name = document.get('name')
        city_location = document.get('location')
        distance = geodesic((latitude, longitude), tuple(city_location)).km
        cities.append({'name': city_name, 'distance': distance})
    cities = sorted(cities, key=lambda x: x['distance'])
    result = [{'name': city['name'], 'distance': city['distance']} for city in cities[:2]]
    return JSONResponse(content=result)
