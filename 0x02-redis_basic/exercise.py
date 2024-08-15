#!/usr/bin/env pythoi:n3
"""
Writing strings to Redis
"""
from uuid import uuid4
import redis
from typing import Union


UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """
    This class writes to Redis
    """

    def __init__(self):
        """string to Redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """store data and returns a string"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
