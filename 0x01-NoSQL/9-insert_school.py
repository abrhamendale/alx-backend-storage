#!/usr/bin/env python3
"""
pyMongo
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts items into collection."""
    return (mongo_collection.insert_one(kwargs))
