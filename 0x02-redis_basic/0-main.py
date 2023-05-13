#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"123"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
print(cache.get(key))
