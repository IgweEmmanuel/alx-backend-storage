#!/usr/bin/env python3
""" Expiring web cache module """

import redis
import requests
from typing import Callable
from functools import wraps

# Initialize the Redis client
redis_client = redis.Redis()

def wrap_requests(fn: Callable) -> Callable:
    """ Decorator wrapper for caching and counting URL accesses """

    @wraps(fn)
    def wrapper(url: str) -> str:
        """ Wrapper that adds caching and counting functionality """
        # Increment the count of how many times the URL has been accessed
        redis_client.incr(f"count:{url}")
        
        # Check if the response is already cached
        cached_response = redis_client.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        
        # If not cached, fetch the content from the URL
        result = fn(url)
        
        # Cache the result with an expiration time of 10 seconds
        redis_client.setex(f"cached:{url}", 10, result)
        
        return result

    return wrapper

@wrap_requests
def get_page(url: str) -> str:
    """ Retrieves the HTML content of a URL and returns it as a string """
    response = requests.get(url)
    return response.text

# Usage example:
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.co.uk"
    print("Fetching URL content...")
    html_content = get_page(url)
    print(f"Content from {url}:\n{html_content[:200]}...")  # Print the first 200 characters

