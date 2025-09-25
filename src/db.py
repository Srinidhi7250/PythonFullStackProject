# db.manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

# load enviroment variables from .env file
load_dotenv()
url=os.getenv("SUPABASE_URL")
key=os.getenv("SUPABASE_KEY")
supabase=create_client(url,key)
# Create task
# Create a new food item
def create_food(name, ingredients, calories, protein, fat, carbs, diet_type, tags):
    return supabase.table("foods").insert({
        "name": name,
        "ingredients": ingredients,
        "calories": calories,
        "protein": protein,
        "fat": fat,
        "carbs": carbs,
        "diet_type": diet_type,
        "tags": tags
    }).execute()

# Get all food items
def get_all_foods():
    return supabase.table("foods").select("*").execute()

# Update a food item
def update_food(food_id, name=None, ingredients=None, calories=None, protein=None, fat=None, carbs=None, diet_type=None, tags=None):
    update_data = {}
    if name: update_data["name"] = name
    if ingredients: update_data["ingredients"] = ingredients
    if calories: update_data["calories"] = calories
    if protein: update_data["protein"] = protein
    if fat: update_data["fat"] = fat
    if carbs: update_data["carbs"] = carbs
    if diet_type: update_data["diet_type"] = diet_type
    if tags: update_data["tags"] = tags
    
    return supabase.table("foods").update(update_data).eq("food_id", food_id).execute()

# Delete a food item
def delete_food(food_id):
    return supabase.table("foods").delete().eq("food_id", food_id).execute()

#Users Table Operations

# Create a new user
def create_user(name, email, password, diet_preference):
    return supabase.table("users").insert({
        "name": name,
        "email": email,
        "password": password,
        "diet_preference": diet_preference
    }).execute()

# Get all users
def get_all_users():
    return supabase.table("users").select("*").execute()

# Update a user
def update_user(user_id, name=None, email=None, password=None, diet_preference=None):
    update_data = {}
    if name: update_data["name"] = name
    if email: update_data["email"] = email
    if password: update_data["password"] = password
    if diet_preference: update_data["diet_preference"] = diet_preference
    
    return supabase.table("users").update(update_data).eq("user_id", user_id).execute()

# Delete a user
def delete_user(user_id):
    return supabase.table("users").delete().eq("user_id", user_id).execute()

# preferences table operations

# Add user preference (rating a food)
def create_preference(user_id, food_id, rating):
    return supabase.table("preferences").insert({
        "user_id": user_id,
        "food_id": food_id,
        "rating": rating
    }).execute()

# Get all preferences of a user
def get_user_preferences(user_id):
    return supabase.table("preferences").select("*").eq("user_id", user_id).execute()

# Update rating
def update_preference(pref_id, rating):
    return supabase.table("preferences").update({
        "rating": rating
    }).eq("pref_id", pref_id).execute()

# Delete a preference
def delete_preference(pref_id):
    return supabase.table("preferences").delete().eq("pref_id", pref_id).execute()

# operations on Recommendation

# Create a new recommendation
def create_recommendation(user_id, food_id, reason):
    return supabase.table("recommendations").insert({
        "user_id": user_id,
        "food_id": food_id,
        "reason": reason
    }).execute()

def get_all_recommendations():
    return supabase.table("recommendations").select("*").execute()

def get_recommendations_by_user(user_id):
    return supabase.table("recommendations").select("*").eq("user_id", user_id).execute()

def update_recommendation(rec_id, reason=None):
    update_data = {}
    if reason:
        update_data["reason"] = reason

    return supabase.table("recommendations").update(update_data).eq("rec_id", rec_id).execute()
def delete_recommendation(rec_id):
    return supabase.table("recommendations").delete().eq("rec_id", rec_id).execute()