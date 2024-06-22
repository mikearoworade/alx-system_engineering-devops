import requests
import time

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Adding a longer delay to prevent rate limiting
        time.sleep(2)
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        return data['data']['subscribers']
    
    except requests.exceptions.HTTPError as http_err:
        # Check for specific 403 error and provide more context
        if response.status_code == 403:
            print(f"HTTP error 403: Forbidden. Access to subreddit {subreddit} might be restricted.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    except KeyError:
        print("Subreddit not found or invalid data format.")
    
    return 0

