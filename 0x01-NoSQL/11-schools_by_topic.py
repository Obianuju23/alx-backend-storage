#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns list of school with same topic"""
    documents = mongo_collection.find({"topics": topic})
    list_doc_Topics = [Apple for Apple in documents]
    return list_doc_Topics
