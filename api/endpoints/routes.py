from typing import List

from fastapi import APIRouter, HTTPException
from api.models.models import DeliveryOut, DeliveryCreate
from api.services.delivery_service import create_delivery_service, list_deliveries_service, get_delivery_service
from api.repository.database import MongoRepository

router = APIRouter()

repo = MongoRepository(collection_name="deliveries")


@router.post("/deliveries/", response_model=DeliveryOut)
async def create_delivery(delivery_create: DeliveryCreate):
    try:
        # Add your code to create the delivery here
        # You can call the function from the services module
        delivery = create_delivery_service(delivery_create)
        response = delivery.dict()
        # Insertar respuesta en la base de datos
        document_id = repo.create_deliver(response)
        response["id"] = document_id

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/deliveries/", response_model=List[DeliveryOut])
async def list_deliveries():
    try:
        # Add your code to list the deliveries here
        # You can call the function from the services module
        deliveries = repo.get_last_10_deliveries()

        return deliveries
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/deliveries/{delivery_id}", response_model=DeliveryOut)
async def get_delivery(delivery_id: str):
    try:
        delivery_doc = repo.get_delivery_by_id(delivery_id)
        if delivery_doc is None:
            raise HTTPException(status_code=404, detail="Delivery not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
