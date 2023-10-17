#!/bin/usr/env python3
""" Python function that lists all documents in a collection using PyMongo"""

def list_all(mongo_collection)
    """A function that lists all documents"""
    All_documents = mongo_collection.find()

    if All_ documents.count() == 0:
        return []
    return All_documents

