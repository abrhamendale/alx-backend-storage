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
    print(n.count_documents({}))
    print("Methods:")
    print("\t", "method GET: ", n.count_documents({"method" : "GET"}))
    print("\t", "method GET: ", n.count_documents({"method" : "POST"}))
    print("\t", "method GET: ", n.count_documents({"method" : "PUT"}))
    print("\t", "method GET: ", n.count_documents({"method" : "PATCH"}))
    print("\t", "method GET: ", n.count_documents({"method" : "DELETE"}))
    print("\t", n.count_documents({ '$and': [{"method" : "GET"}, {"path" : "/status"}]})," status check")


if __name__ == "__main__":
    log_parser()
