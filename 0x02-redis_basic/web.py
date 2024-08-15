import requests
from functools import cache
from typing import Optional

# Set cache timeout to 10 seconds
CACHE_TIMEOUT = 10

def count_url_access(redis_client, url):
  """
  Increments the access count for a given URL in Redis.
  """
  key = f"count:{url}"
  redis_client.incr(key)
  redis_client.expire(key, CACHE_TIMEOUT)  # Set expiration

@cache(maxsize=None, timeout=CACHE_TIMEOUT)  # Cache decorator
def get_page(url: str, redis_client=None) -> Optional[str]:
  """
  Retrieves the HTML content of a URL, handling caching and access counting.

  Args:
      url: The URL to fetch.
      redis_client: An optional Redis client instance (for testing purposes).

  Returns:
      The HTML content of the URL, or None if an error occurs.
  """

  # Use provided Redis client or create a temporary one
  if not redis_client:
    import redis
    redis_client = redis.Redis()

  count_url_access(redis_client, url)  # Track access count

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-2xx status codes
    return response.text
  except requests.exceptions.RequestException as e:
    print(f"Error fetching URL {url}: {e}")
    return None

# Example usage with a temporary Redis client
if __name__ == "__main__":
  url = "http://slowwly.robertomurray.co.uk/delay/3000/url/slow"
  content = get_page(url)
  if content:
    print(f"Fetched content for {url}:\n{content[:100]}...")  # Print first 100 chars
  else:
    print(f"Failed to fetch content for {url}")

