import pandas as pd
from sklearn.cluster import KMeans
import joblib

# Function to segment users using K-Means clustering
def segment_users(df_users, features, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df_users['cluster'] = kmeans.fit_predict(features)
    return df_users, kmeans

# Function to get user profiles with cluster information
def get_user_profiles(df_users):
    return df_users[['user_id', 'vibe', 'expenses', 'cluster']]

def save_model(kmeans, encoder_vibe, scaler,df_users, model_path='models/'):
    joblib.dump(kmeans, model_path + 'kmeans_model.pkl')
    joblib.dump(encoder_vibe, model_path + 'encoder_vibe.pkl')
    joblib.dump(scaler, model_path + 'scaler.pkl')
    df_users.to_csv(model_path + 'users.csv', index=False)