import numpy as np
import random


def create_feature_vector(vibe, expenses, encoder_vibe, scaler):
    vibe_vector = encoder_vibe.transform([[vibe]])[0]
    
    expenses_scaled = scaler.transform([[expenses]])[0]
    
    return np.concatenate([vibe_vector, expenses_scaled])

def generate_recommendations(cluster_index, df_users, mock_data, season):
    users_in_cluster = df_users[df_users['cluster'] == cluster_index]
    
    city_counts = {}
    for _, row in users_in_cluster.iterrows():
        favorite_city = row['favorite_city']
        city_counts[favorite_city] = city_counts.get(favorite_city, 0) + 1
    
    recommended_city = max(city_counts, key=city_counts.get)

    city_data = mock_data[recommended_city]
    
    if season not in city_data['ideal_seasons']:
        # Find alternative cities that are suitable for the season
        suitable_cities = [
            city for city, data in mock_data.items() if season in data['ideal_seasons']
        ]
        
        if suitable_cities:
            recommended_city = random.choice(suitable_cities) 
            city_data = mock_data[recommended_city]

    return {
        'recommended_city': recommended_city,
        'places_to_visit': city_data['places_to_visit'],
        'restaurants': city_data['restaurants'],
        'activities': city_data['activities']
    }

def find_closest_cluster(vibe, expenses, kmeans, encoder_vibe, scaler):
    
    user_feature = create_feature_vector(vibe, expenses, encoder_vibe, scaler)
    
    closest_cluster = kmeans.predict([user_feature])[0]
    
    return closest_cluster
