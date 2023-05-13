#!/usr/bin/python3
import redis

r = redis.Redis()
r.set('a', 'b')
print(int_or_str('b'))
