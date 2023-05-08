#!/usr/bin/env python3
"""
MongoDB
"""


from mongoengine import connect


def list_all(mongo_collection):
    """Lists all documents in a collection."""
    if (mongo_collection):
        return (mongo_collection.documents)
    else:
        return ([])
