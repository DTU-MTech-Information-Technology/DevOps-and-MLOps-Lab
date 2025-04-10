import os
from hvac import Client
from dotenv import load_dotenv

load_dotenv()

# Initialize the Vault client
vault_client = Client(url=os.getenv("VAULT_ADDR"), token=os.getenv("VAULT_TOKEN"))

# Fetch the secret from Vault
secret = vault_client.secrets.kv.v2.read_secret(path="/myapp/api_key")

# Extract the API key from the response
api_key = secret["data"]["data"]["value"]

# Use the API key in the application (for demonstration purposes, we'll print it)
print(f"Retrieved API Key: {api_key}")
