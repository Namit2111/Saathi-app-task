import pandas as pd
from data_generation import generate_mock_user_data,mock_data
from preprocessing import preprocess_data
from segmentation import segment_users, get_user_profiles,save_model
# from recommendation import generate_recommendations, find_closest_cluster
# from load_model import load_model
import random

# ------------------------------------------Generating and saving and loading dataset---------------
# Generate a mock dataset of 100 users
df_users = generate_mock_user_data(100)

df_users.to_csv('users.csv', index=False)

df_users = pd.read_csv('users.csv')
# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------Generating and savinn model --------------------
df_users, features, encoder_vibe, scaler = preprocess_data(df_users)

df_users, kmeans = segment_users(df_users, features)

save_model(kmeans, encoder_vibe, scaler,df_users)
# ----------------------------------------------------------------------------------------------------

# Get user profiles with clusters
# user_profiles = get_user_profiles(df_users)
# print("\nUser Profiles with Clusters:")
# print(user_profiles.head())



#Load model
# kmeans_loaded, encoder_vibe_loaded, scaler_loaded ,df_users= load_model()

# new_user_vibe = 'Adventure'
# new_user_expenses = 250  
# new_user_season = 'Summer'  

# # Find the closest cluster for the new user
# closest_cluster = find_closest_cluster(new_user_vibe, new_user_expenses, kmeans_loaded, encoder_vibe_loaded, scaler_loaded)

# # Generate recommendations based on the user's cluster and season
# recommendations = generate_recommendations(closest_cluster, df_users,mock_data, new_user_season)

# # Display the recommendations
# print("\nRecommended Itinerary for New User:")
# print("Recommended City:", recommendations['recommended_city'])
# print("Places to Visit:", recommendations['places_to_visit'])
# print("Recommended Restaurants:", recommendations['restaurants'])
# print("Activities to Do:", recommendations['activities'])
