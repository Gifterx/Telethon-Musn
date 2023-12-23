from motor.motor_asyncio import AsyncIOMotorClient

from Config import MONGO_DB_URI

print("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Yukki
    print("Connected to your Mongo Database.")
except:
    print("Failed to connect to your Mongo Database.")
    exit()
