#!/usr/bin/env python3
"""
pyMongo
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """Changes all tpoics of a document."""
    mongo_collection.update_one({"name" : name}, {'$set':{"topics" : topics}})
