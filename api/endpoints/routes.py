from http.client import HTTPException
from typing import List

from fastapi import APIRouter
from api.models.models import DeliveryOut,DeliveryCreate
from api.services.delivery_service import create_delivery_service, list_deliveries_service, get_delivery_service

router = APIRouter()


@router.post("/deliveries/", response_model=DeliveryOut)
async def create_delivery(delivery_create: DeliveryCreate):
    try:
        # Add your code to create the delivery here
        # You can call the function from the services module
        delivery = create_delivery_service(delivery_create)
        return delivery
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/deliveries/", response_model=List[DeliveryOut])
async def list_deliveries():
    try:
        # Add your code to list the deliveries here
        # You can call the function from the services module
        deliveries = list_deliveries_service()
        return deliveries
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/deliveries/{delivery_id}", response_model=DeliveryOut)
async def get_delivery(delivery_id: int):
    try:
        # Add your code to get the delivery here
        # You can call the function from the services module
        delivery = get_delivery_service(delivery_id)
        if not delivery:
            raise HTTPException(status_code=404, detail="Delivery not found")
        return delivery
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))