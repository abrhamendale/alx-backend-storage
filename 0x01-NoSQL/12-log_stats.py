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
    print("\t", "method GET: ", n.count_documents({"$match" : {"method" : "GET"}}))
    print("\t", "method GET: ", logs.nginx.count_documents({"$match" : {"method" : "POST"}}))
    print("\t", "method GET: ", logs.nginx.count_documents({"$match" : {"method" : "PUT"}}))
    print("\t", "method GET: ", logs.nginx.count_documents({"$match" : {"method" : "PATCH"}}))
    print("\t", "method GET: ", logs.nginx.count_documents({"$match" : {"method" : "DELETE"}}))
    print("\t", logs.nginx.count_documents({"$match" : {"method" : "GET"}}, {"$match" : {"path" : "/status"}}),"status check")


if __name__ == "__main__":
    log_parser()
