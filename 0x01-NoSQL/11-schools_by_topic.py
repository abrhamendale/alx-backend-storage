#!/usr/bin/env python3
"""
pyMongo
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returns documents with a specific topic."""
    if mongo_collection is not None:
        return (mongo_collection.find({"mongo_collection.topics": { '$in': ['$topic'] }}))
