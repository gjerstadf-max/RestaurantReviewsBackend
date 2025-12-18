import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from typing import List

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend working!"}

@app.get("/search")
def search(query: str):
    """
    Search Google Places for restaurants matching 'query'.
    Returns JSON with list of results.
    """
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    # Use fixed lat/lng for Seattle (replace if needed)
    params = {
        "query": f"{query} restaurant",
        "location": "47.6062,-122.3321",  
        "radius": 5000,  # meters
        "key": GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    # If Google returns an error, send it back for debugging
    if data.get("status") != "OK":
        return {"error": data.get("status"), "message": data.get("error_message")}
    
    results = [
        {
            "name": r.get("name"),
            "address": r.get("formatted_address"),
            "rating": r.get("rating", 0),
            "user_ratings_total": r.get("user_ratings_total", 0)
        }
        for r in data.get("results", [])
    ]
    
    return {"results": results}
