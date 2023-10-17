#!/usr/bin/env python3
""" Python function that lists all documents in a collection using PyMongo"""

def list_all(mongo_collection)
    """A function that lists all documents"""
    all_documents = mongo_collection.find()

    if all_documents.count() == 0:
        return []

    return all_documents

