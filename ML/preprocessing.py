import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def preprocess_data(df_users):
    
    # doesn't needed due to synthetic data generation
    # df_users['reviews'].fillna('', inplace=True)
    # df_users['expenses'] = df_users['expenses'].fillna(df_users['expenses'].mean())
    # df_users['vibe'] = df_users['vibe'].fillna('Unknown')
    

    """
    Preprocesses the user data by encoding the 'vibe' column using one-hot encoding
    and scaling the 'expenses' column using standardization.

    Parameters
    ----------
    df_users : pd.DataFrame
        The user data to be preprocessed.

    Returns
    -------
    df_users : pd.DataFrame
        The original user data with the 'vibe' and 'expenses' columns preprocessed.
    features : pd.DataFrame
        A DataFrame containing the preprocessed 'vibe' and 'expenses' columns.
    encoder_vibe : OneHotEncoder
        The one-hot encoder used to encode the 'vibe' column.
    scaler : StandardScaler
        The standard scaler used to scale the 'expenses' column.

    Notes
    -----
    The preprocessing steps are as follows:

    1. The 'vibe' column is one-hot encoded using the `OneHotEncoder` class.
    2. The 'expenses' column is scaled using the `StandardScaler` class.
    """

    encoder_vibe = OneHotEncoder(sparse_output=False)
    vibe_encoded = encoder_vibe.fit_transform(df_users[['vibe']])

    scaler = StandardScaler()
    expenses_scaled = scaler.fit_transform(df_users[['expenses']])

    features = pd.DataFrame(np.hstack([vibe_encoded, expenses_scaled]),
                            columns=np.concatenate([encoder_vibe.get_feature_names_out(['vibe']), ['scaled_expenses']]))
    
    return df_users, features, encoder_vibe, scaler
