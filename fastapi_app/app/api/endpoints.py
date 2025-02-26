from fastapi import APIRouter, Request
from app.services.sum_service import get_sum
from app.config import DUMMY_API_KEY

router = APIRouter()

@router.get("/")
async def sum_values(request: Request):
    return {
        "success": True,
        "message": "Backend is Running"
    }

@router.post("/getSum")
async def sum_values(request: Request):
    data = await request.json()
    a = data.get("a")
    b = data.get("b")
    if a is None or b is None:
        return {"error": "Both 'a' and 'b' are required"}
    
    result = get_sum(a, b)
    return {
        "sum": result,
        "api_key_used": DUMMY_API_KEY
    }
