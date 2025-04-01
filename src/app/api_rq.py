from src.aiohttps import get_info_currency

from fastapi import APIRouter





router = APIRouter(prefix="/api/currency",tags=["API"])



@router.get("")
async def get_info_about_currency(amount: int):
    return  await get_info_currency(amount)
