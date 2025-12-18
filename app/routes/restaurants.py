from fastapi import APIRouter

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)

# Example: GET /restaurants
@router.get("/")
def list_restaurants():
    return [
        {"id": 1, "name": "Blue Marlin", "location": "Roatán"},
        {"id": 2, "name": "Poulsbo Fish Co.", "location": "Poulsbo"},
    ]

# Example: GET /restaurants/{id}
@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: int):
    return {"id": restaurant_id, "name": "Sample Restaurant"}
