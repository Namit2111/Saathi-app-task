## README.md

# Travel Itinerary Recommendation System

This project is a **FastAPI** application that provides personalized travel itinerary recommendations based on user preferences using machine learning (K-Means clustering). The application loads pre-trained models, and encodes user data to segment them into clusters and generate recommendations for cities, places to visit, restaurants, and activities. The project leverages a machine learning model that clusters users based on their preferences, and a recommendation engine that generates itineraries for new users.

---

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
- [Prerequisites](#prerequisites)
- [Running the Application](#running-the-application)
- [Running via Docker](#running-via-docker)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Machine Learning Model](#machine-learning-model)
---

## Features

- **User Clustering:** Uses K-Means to segment users based on travel preferences.
- **Itinerary Recommendations:** Provides recommendations for cities, places to visit, restaurants, and activities based on the user's cluster.
- **Pre-Trained Model Loading:** Loads pre-trained models (KMeans, encoders, scalers) to generate recommendations.
- **API Endpoints:** Exposes a FastAPI-based API for generating recommendations.

---

## backend Structure

```bash
.
├── app.py                           # Entry point for FastAPI application
├── app/
│   ├── __init__.py                  # Initializes FastAPI app
│   ├── recommend.py                 # Recommendation logic and routes
├── Utils/
│   ├── load_model.py                # Load pre-trained model, encoder, scaler, and user data
│   ├── recommendation.py            # Recommendation logic and clustering functions
│   └── mock_data.py                 # Mock data used in recommendations
├── models/                          # Saved models and data
│   ├── kmeans_model.pkl             # Pre-trained KMeans model
│   ├── encoder.pkl                  # Saved OneHotEncoder
│   ├── scaler.pkl                   # Saved StandardScaler
│   └── df_users.pkl                 # Clustered user data
├── Dockerfile                       # Docker configuration file
└── README.md                        # Project documentation
```

---

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.8+**
- **FastAPI**
- **Docker** (if running via Docker)
- **Joblib** (for loading saved machine learning models)
- **Uvicorn** (for serving FastAPI)
- **Required packages** (can be installed from requirements.txt)
---

## Running the Application

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/travel-recommendation-system.git
cd travel-recommendation-system
```

### 2. Set up a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set environment variables:

Create a `.env` file at the root of the backend with the following content:

```env
GEMINI_API="your-gemini-api-key-here"
```

### 4. Run the FastAPI application:

```bash
cd backend
python app.py
```

The application will be available at `http://127.0.0.1:8000`.

---

## Running via Docker

To run the application in a Docker container, follow these steps:

### Docker Compose

If you have a `docker-compose.yml` file, you can also use `docker-compose` to manage your Docker containers:

```bash
docker-compose up --build
```
Put your Gemini key in place before running.
---

## Environment Variables

The application relies on the following environment variable:

- `GEMINI_API`: Your API key for the Gemini service (mock or real).

Make sure to include it in your `.env` file or pass it in the Docker run command as shown above.

---

## API Endpoints

The FastAPI application exposes the following endpoint:

- `POST /recommend`: Generate a travel itinerary recommendation based on user preferences.

### Example Request:

```bash
POST /recommend
Content-Type: application/json

{
  "vibe": "Adventure",
  "expenses": 250,
  "season": "Summer"
}
```

### Example Response:

```json
{
  "itenary": "Detailed Planned Guide"
}
```

---

## Machine Learning Model

The recommendation system uses a **K-Means Clustering** model, which segments users based on their preferences for travel vibe, budget, and season. The system then finds the closest cluster to a new user and recommends an itinerary based on the cluster's data.

### Model Files:

- **KMeans Model**: `kmeans_model.pkl`
- **OneHotEncoder**: `encoder.pkl`
- **StandardScaler**: `scaler.pkl`
- **Clustered User Data**: `users.csv`

### Steps for the Recommendation Flow:

1. **Load the Model**: Load the pre-trained KMeans model, encoder, scaler, and user data from the `models/` directory.
2. **Cluster Matching**: Based on the user input (vibe, expenses), the user is matched to the closest cluster.
3. **Recommendation Generation**: Based on the user's cluster, cities and activities from the mock data are recommended.

---
