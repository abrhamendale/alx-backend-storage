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
            store(data)
    return inner

class Cache:
    """Redis cache class."""
    def __init__(self):
        self._redis = redis.Redis()


    #@count_calls
    def store(self, data: Union[str, bytes, int, float]):
        r = uuid.uuid4()
        self._redis.set(str(r), data)
        return (str(r))


    def get_str(method):
        def inner(key: str, fn=None):
            #print(type(key))
            if type(key) == "str" and fn is None:
                return method(key, lambda d: d.decode("utf-8"))
            else:
                return method(key, fn)
        return inner


    def get_int(method):
        def inner(key: str, fn=None):
            if type(key) == "int" and fn is None:
                return method(key, lambda d: d.decode("utf-32"))
            else:
                return method(key, fn)
        return inner

    @get_str
    @get_int
    def get(self, key: str, fn=None):
        print("!")
        if key is not None:
            print("!!",fn)
            if fn is not None:
                print("!!!")
                print(1)
                v = self._redis.get(key)
                return (fn(v))
        else:
            return (None)
