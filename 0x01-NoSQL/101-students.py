#!/usr/bin/env python3
"""
pyMongo
"""


import pymongo


def top_students(mongo_collection):
    """Returns all students sorted by average score."""
    if (mongo_collection is not None):
        return (mongo_collection.aggregate([{"$group" => {"_id" => "$_id", '$name' => { $avg" => "$score" },},},]))
