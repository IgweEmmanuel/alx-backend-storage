import redis
import uuid
from typing import Union, Optional, Callable

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key   


    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int]]] = None) -> Union[str,   
 int, None]:
        """
        Retrieves data from Redis and applies an optional conversion function.

        Args:
            key: The key to retrieve data for.
            fn: An optional callable to convert the retrieved data to the desired format.

        Returns:
            The retrieved data, converted if a conversion function is provided,
            or None if the key does not exist.
        """

        data = self._redis.get(key)
        if data is None:
            return None

        if not fn:
            return data  # Return data as-is if no conversion function is provided

        return fn(data)  # Apply conversion function if provided

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string from Redis, automatically decoding it from bytes.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer from Redis, automatically converting it from bytes.
        """
        return self.get(key, fn=int.from_bytes)
