#!/usr/bin/env python3
"""
pyMongo
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts items into collection."""
    dic = dict()
    dic = kwargs
    if mongo_collection is not None:
        return (mongo_collection.insert_one(dic))
