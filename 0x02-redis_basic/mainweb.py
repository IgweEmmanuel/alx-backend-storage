# Example usage with a temporary Redis client
if __name__ == "__main__":
    get_page = __import__("web").get_page
    url = "http://slowwly.robertomurray.co.uk/delay/3000/url/slow"
    content = get_page(url)
    if content:
        print(f"Fetched content for {url}:\n{content[:100]}...")  # Print first 100 chars
    else:
        print(f"Failed to fetch content for {url}")
