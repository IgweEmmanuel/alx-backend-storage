import requests
import redis
from typing import Optional

class Cache:
    def __init__(self):
        # Initialize the Redis client
        self._redis = redis.Redis()
    
    def get_page(self, url: str) -> Optional[str]:
        # Track the number of times the URL is accessed
        count_key = f"count:{url}"
        self._redis.incr(count_key)

        # Check if the content is cached
        cached_content = self._redis.get(url)
        if cached_content:
            return cached_content.decode('utf-8')

        # If not cached, fetch the content from the URL
        response = requests.get(url)
        if response.status_code == 200:
            # Cache the result with an expiration time of 10 seconds
            self._redis.setex(url, 10, response.text)
            return response.text

        # If the request failed, return None
        return None

# Usage example:
if __name__ == "__main__":
    cache = Cache()
    url = "https://example.com"
    html_content = cache.get_page(url)
    if html_content:
        print(f"Content from {url}:\n{html_content[:200]}...")  # Print the first 200 characters
    else:
        print(f"Failed to retrieve content from {url}")

