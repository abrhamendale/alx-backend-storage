#!/usr/bin/env python3
"""
pyMongo
"""


def top_students(mongo_collection):
    """Returns all students sorted by average score."""
    return (mongo_collection.aggregate([{$group: {"_id": "_id", averageScore: { $avg: "$score" }}}]))
