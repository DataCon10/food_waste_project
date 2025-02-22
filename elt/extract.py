import os, requests, json
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

# Set up API key and connection string (assume these are in your environment)
SPOONACULAR_API_KEY = os.environ['SPOONACULAR_API_KEY']
AZURE_BLOB_CONNECTION_STRING = os.environ['AZURE_BLOB_CONNECTION_STRING']

# Connect to Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_CONNECTION_STRING)
container_client = blob_service_client.get_container_client("raw-recipes")

def fetch_recipes(query="leftovers", number=50):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "query": query,
        "number": number,
        "addRecipeInformation": True
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("results", [])

def upload_raw_data(data, filename):
    blob_client = container_client.get_blob_client(filename)
    blob_client.upload_blob(json.dumps(data), overwrite=True)

if __name__ == "__main__":
    recipes = fetch_recipes("leftovers", 50)
    upload_raw_data(recipes, "recipes_raw.json")
    print("Raw recipe data uploaded.")
