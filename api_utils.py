import time
import requests
from config import API_KEY

def fetch_realtime_transactions():
    url = f"https://api.example.com/transactions?api_key={API_KEY}"
    return retry_request(url)

def buy_hero_token(amount):
    # Implement your buy HERO token logic
    pass

def sell_hero_token(amount):
    # Implement your sell HERO token logic
    pass

def buy_solana(amount):
    # Implement your buy SOLANA token logic
    pass

def check_user_sold_solana(wallet_address):
    # Implement your check user sold SOLANA logic
    pass

def retry_request(url):
    max_retries = 3
    retries = 0
    wait_time_seconds = 5
    
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data (retry {retries}): {e}")
            retries += 1
            time.sleep(wait_time_seconds * (2 ** retries))  # Exponential backoff
    
    raise RuntimeError(f"Failed to fetch data after {max_retries} retries")
