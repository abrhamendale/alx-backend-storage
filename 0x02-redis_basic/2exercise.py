#!/usr/bin/env python3
"""
Redis
"""


from typing import Union
import redis
import uuid


def count_calls(method):
    def inner(data: Union[str, bytes, int, float]):
        r = redis.Redis()
        if method.__name__ == "store":
            nm = cache.store.__qualname__
            r.incr(nm)
        return store(data)

def fn1(method):
    def fn2(key: str, fn = None):



class Cache:
    """Redis cache class."""
    def __init__(self):
        self._redis = redis.Redis()


    #@count_calls
    def store(self, data: Union[str, bytes, int, float]):
        r = uuid.uuid4()
        self._redis.set(str(r), data)
        return (str(r))

    def get(self, key: str, fn=None):
        if key is not None:
            if fn is not None:
                v = self._redis.get(key)
                return (fn(v))
            else:
                if type(key) == "str":
                    return (get_str(self._redis.get(key)))
                if type(key) == "int":
                    return (get_int(self._redis.get(key)))
        else:
            return (None)

    def get_str(v):
        v.decode(str)

    def get_int(v):
        v.decode(int)
