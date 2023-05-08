#!/usr/bin/env python3
"""
pyMongo
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts items into collection."""
    for key, value in kwargs.items():
        return (mongo_collection.insert({key : value}))
