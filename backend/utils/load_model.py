import joblib
import pandas as pd
import os 

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) 
MODELS_DIR = os.path.join(BASE_DIR, 'models')
def load_model():
    kmeans_model = joblib.load(os.path.join(MODELS_DIR, 'kmeans_model.pkl'))
        
    encoder = joblib.load(os.path.join(MODELS_DIR, 'encoder_vibe.pkl'))
    
    scaler = joblib.load(os.path.join(MODELS_DIR, 'scaler.pkl'))
    
    df_users = pd.read_csv(os.path.join(MODELS_DIR, 'users.csv'))
    
    return kmeans_model, encoder, scaler, df_users

if __name__ == '__main__':
    load_model()