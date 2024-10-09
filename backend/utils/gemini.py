import os
import google.generativeai as genai
from config.config import GEMINI_API

genai.configure(api_key = GEMINI_API)

model = genai.GenerativeModel("gemini-1.5-flash")
def generate_json(recommendations,trend,user):

    prompt = """You are a traveling planner that helps people plan their next trip. You are given the following data: \n
    Recommendations: {}\n
    trends of the city: {}\n
    based on this data, create a detailed itinerary for the user to visit the recommended places. \n
    The itinerary should be detailed and organized, with detailed descriptions of each place. \n 
    You can only use given recommendations and trends to plan the itinerary.\n
    Make sure trends are relevant to the user's preferences. given user prefrences are:{}
    """.format(recommendations,trend,user)
    result = model.generate_content(prompt)
    return result.text


if __name__ == "__main__":
    print(get_cookies_recipes())
