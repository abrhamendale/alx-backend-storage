#!/usr/bin/env python3
"""
MongoDB
"""

import pymongo


def list_all(mongo_collection):
    """Lists all documents in a collection."""
    if (mongo_collection is not None):
        return (mongo_collection.find())
    else:
        return ([])
