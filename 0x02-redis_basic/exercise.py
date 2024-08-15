#!/usr/bin/env pythoi:n3
"""
Writing strings to Redis
"""
from uuid import uuid4
import redis
from typing import Union Optional Callable


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """
    This class writes to Redis
    """

    def __init__(self):
        """
        string to Redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """
        store data and returns a string
        :param data:
        :return:
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> UnionOfTypes:
        """
        convert the data back
         to the desired format
        :param key:
        :param fn:
        :return:
        """
        if !key:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self: bytes) -> str:
            """return string"""
            return self.decode("utf-8")
        
    def get_int(self: bytes) -> int:
            """return int"""
            return int.from_bytes(self, sys.bytesorder)
