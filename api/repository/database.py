from typing import Dict, List, Optional

from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from api.models.models import DeliveryOut
from core.config import MONGO_CONNECTION_STRING, DB_NAME


class MongoRepository:
    def __init__(self, collection_name: str):
        self.client = MongoClient(MONGO_CONNECTION_STRING)
        self.db = self.client[DB_NAME]
        self.collection = self.db[collection_name]

    def create_deliver(self, document: Dict) -> str:
        try:
            result = self.collection.insert_one(document)
            return str(result.inserted_id)
        except PyMongoError as e:
            # Manejo de excepción para errores de PyMongo
            raise Exception(f"Error inserting the document in DB: {e}")

    def get_last_10_deliveries(self) -> List[Dict]:
        deliveries = []
        for delivery in self.collection.find().sort([("_id", -1)]).limit(10):
            # delivery["_id"] = str(delivery["_id"])
            delivery["id"] = str(delivery["_id"])
            deliveries.append(delivery)
        return deliveries

    def get_delivery_by_id(self, delivery_id: str) -> Optional[DeliveryOut]:
        document = self.collection.find_one({"_id": ObjectId(delivery_id)})

        if document:
            document["id"] = str(document["_id"])
            return DeliveryOut(**document)
        return None
