#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def nginx_stat_log():
    """Function that provide some stats about Nginx logs"""
    client = MongoClient()
    database = client.logs
    collection = database.nginx

    Total_docs = collection.count_docs({})
    get = collection.count_docs({"method": "GET"})
    post = collection.count_docs({"method": "POST"})
    put = collection.count_docs({"method": "PUT"})
    patch = collection.count_docs({"method": "PATCH"})
    delete = collection.count_docs({"method": "DELETE"})
    path = collection.count_docs({"method": "GET", "path": "/status"})

    print("{:d} logs". format(total))
    print("Methods:")
    print("\tmethod GET: {:d}". format(get))
    print("\tmethod POST: {:d}". format(post))
    print("\tmethod PUT: {:d}". format(put))
    print("\tmethod PATCH: {:d}". format(patch))
    print("\tmethod DELETE: {:d}". format(delete))
    print("{:d} status check". format(path))


if __name__ == "__main__":
    nginx_stat_log()
