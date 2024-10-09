import pandas as pd
import random


mock_data = {
    'Mumbai': {
        'places_to_visit': ['Gateway of India', 'Marine Drive', 'Elephanta Caves'],
        'restaurants': ['Leopold Cafe', 'Bistro Grill', 'The Table'],
        'activities': ['beach visit', 'shopping', 'sightseeing'],
        'ideal_seasons': ['Winter', 'Summer']  
    },
    'Shimla': {
        'places_to_visit': ['Mall Road', 'Jakhoo Temple', 'Christ Church'],
        'restaurants': ['The Restaurant', 'Cafe Simla Times', 'Himachali Rasoi'],
        'activities': ['skiing', 'hiking', 'sightseeing'],
        'ideal_seasons': ['Winter'] 
    },
    'Goa': {
        'places_to_visit': ['Baga Beach', 'Fort Aguada', 'Dudhsagar Waterfalls'],
        'restaurants': ['Gunpowder', 'Fisherman\'s Wharf', 'Vinayak Family Restaurant'],
        'activities': ['beach visit', 'water sports', 'nightlife'],
        'ideal_seasons': ['Winter', 'Summer'] 
    },
    'Jaipur': {
        'places_to_visit': ['Hawa Mahal', 'Amber Fort', 'City Palace'],
        'restaurants': ['Chokhi Dhani', 'Barbeque Nation', '1135 AD'],
        'activities': ['sightseeing', 'shopping', 'cultural experiences'],
        'ideal_seasons': ['Winter', 'Spring']  
    },
    'Darjeeling': {
        'places_to_visit': ['Tiger Hill', 'Batasia Loop', 'Darjeeling Himalayan Railway'],
        'restaurants': ['Kunga Restaurant', 'The Tea Lounge', 'Glenary’s'],
        'activities': ['tea plantation visits', 'hiking', 'sightseeing'],
        'ideal_seasons': ['Spring', 'Summer']  
    },
}

def generate_mock_user_data(num_users=100):
    """
    Generate a mock dataset of user data for testing and development purposes.

    Parameters
    ----------
    num_users : int, optional
        The number of users to generate. Default is 100.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the generated user data.

    Notes
    -----
    The generated data includes the following columns:

    - user_id: a unique identifier for each user
    - expenses: a random number between 50 and 500, representing the user's
        average daily expenses
    - vibe: a randomly chosen string from the list ['Adventure', 'Relaxation',
        'Luxury', 'Budget'], representing the user's travel vibe
    - reviews: a random string of 5 words, representing the user's review
        history
    - previous_destinations: a random sample of 1-3 cities from the list of
        cities in the mock_data dictionary, representing the user's previous
        travel destinations
    - favorite_city: a random city from the list of cities in the mock_data
        dictionary, representing the user's favorite city
    """
    vibes = ['Adventure', 'Relaxation', 'Luxury', 'Budget']
    cities = list(mock_data.keys())
    
    data = []
    for user_id in range(1, num_users + 1):
        user_data = {
            'user_id': user_id,
            'expenses': round(random.uniform(50, 500), 2),
            'vibe': random.choice(vibes),  
            'reviews': " ".join(random.choices(["Amazing", "Great", "Average", "Fun", "Terrible"], k=5)),
            'previous_destinations': random.sample(cities, k=random.randint(1, 3)), 
            'favorite_city': random.choice(cities)  
        }
        data.append(user_data)
    
    return pd.DataFrame(data)
