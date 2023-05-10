#!/usr/bin/env python3
"""
Redis
"""


from typing import Union
import redis
import uuid


class Cache:
    """Redis cache class."""
    def __init__(self):
        self._redis = redis.Redis()
    

    def store(self, data: Union[str, bytes, int, float]):
        r = uuid.uuid4()
        self._redis.set(str(r), data)
        return (str(r))
