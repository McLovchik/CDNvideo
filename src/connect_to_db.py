from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_USERNAME, MONGO_DB_PASSWORD

client = AsyncIOMotorClient(
    f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}'
    f'@cluster0.ekgiy0k.mongodb.net/?retryWrites=true&w=majority'
)


def get_cities_collection():
    """Returns async collection of cities from MongoDB"""
    db = client['Cities']
    return db['cities']
