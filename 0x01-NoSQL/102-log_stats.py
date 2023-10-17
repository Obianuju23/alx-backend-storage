#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def nginx_stat_log():
    """Function that provides some stats about Nginx logs"""
    client = MongoClient()
    collection = client.logs.nginx

    Total_docs = collection.count_documents({})
    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    path = collection.count_documents({"method": "GET", "path": "/status"})

    print("{:d} logs".format(Total_docs))
    print("Methods:")
    print("\tmethod GET: {:d}".format(get))
    print("\tmethod POST: {:d}".format(post))
    print("\tmethod PUT: {:d}".format(put))
    print("\tmethod PATCH: {:d}".format(patch))
    print("\tmethod DELETE: {:d}".format(delete))
    print("{:d} status check".format(path))


if __name__ == "__main__":
    nginx_stat_log()
