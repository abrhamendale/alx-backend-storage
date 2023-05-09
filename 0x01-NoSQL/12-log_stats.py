#!/usr/bin/env python3
"""
pyMongo
"""


import pymongo
from pymongo import MongoClient


def log_parser():
    """Parses Nginx log."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    n = client.logs.nginx
    print(n.count_documents({}), "logs")
    print("Methods:")
    print("   ", "method GET:", n.count_documents({"method" : "GET"}))
    print("   ", "method POST:", n.count_documents({"method" : "POST"}))
    print("   ", "method PUT:", n.count_documents({"method" : "PUT"}))
    print("   ", "method PATCH:", n.count_documents({"method" : "PATCH"}))
    print("   ", "method DELETE:", n.count_documents({"method" : "DELETE"}))
    print(n.count_documents({ '$and': [{"method" : "GET"}, {"path" : "/status"}]}),"status check")


if __name__ == "__main__":
    log_parser()
