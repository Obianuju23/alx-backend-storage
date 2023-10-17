#!/usr/bin/env python3
"""Python function that inserts new document in collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """A function that inserts new document"""

    new_document_id = mongo_collection.insert(kwargs)
    return new_document_id

