#!/usr/bin/env python3
"""
pyMongo
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returns documents with a specific topic."""
    return (mongo_collection.find({"topic": {"$elemMatch" : {topic}}}))
