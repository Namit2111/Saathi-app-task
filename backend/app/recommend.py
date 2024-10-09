
from fastapi import APIRouter
from pydantic import BaseModel
from utils.load_model import load_model  
from utils.recommendation import generate_recommendations, find_closest_cluster
from utils.mock_data import mock_data
from utils.gemini import generate_json
from prototype.mock_trend import mock_trend
import os
router = APIRouter()

class RecommendationRequest(BaseModel):
    vibe: str
    expenses: float
    season: str

kmeans_loaded, encoder_vibe_loaded, scaler_loaded, df_users = load_model()

@router.post("/recommendation")
async def get_recommendation(request: RecommendationRequest):
    new_user_vibe = request.vibe
    new_user_expenses = request.expenses
    new_user_season = request.season

    user = {
        "vibe": new_user_vibe,
        "expenses": new_user_expenses,
        "season": new_user_season
    }

    closest_cluster = find_closest_cluster(new_user_vibe, new_user_expenses, kmeans_loaded, encoder_vibe_loaded, scaler_loaded)

    recommendations = generate_recommendations(closest_cluster, df_users, mock_data, new_user_season)
    trend = mock_trend[recommendations['recommended_city']]
    os.system('cls')
    itenary = generate_json(str(recommendations),str(trend),str(user))
    print(itenary)
    # return {
    #     "recommended_city": recommendations['recommended_city'],
    #     "places_to_visit": recommendations['places_to_visit'],
    #     "restaurants": recommendations['restaurants'],
    #     "activities": recommendations['activities']
    # }

    return {
        "Itenary": itenary
    }