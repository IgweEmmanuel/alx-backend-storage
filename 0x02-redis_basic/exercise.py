#!/usr/bin/env pythoi:n3
"""
Writing strings to Redis
"""
from uuid import uuid4
import redis
from typing import Union


class Cache:
    """
    This class writes to Redis
    """


    def __init__(self):
        """string to Redis"""
        self._redis = redis.Redis()
        self._redis.flushadb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data and returns a string"""
        randkey = str(uuid4())
        self._redis.mset({randkey: data})
        return randkey
