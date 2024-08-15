#!/usr/bin/env pythoi:n3
"""
Writing strings to Redis
"""
from uuid import uuid4
import redis


class Cache():
    """
    This class writes to Redis
    """


    def __init__(self):
        """string to Redis"""
        self._redis = redis.Redis()
        self.flushdb = self._redis.flushall


    def store(self, data) -> str:
        """store data and returns a string"""
        randkey = str(uuid4())
        self._redis.set(randkey, data)
        res = self._redis.get(randkey)
        return res.decode("utf-8")
