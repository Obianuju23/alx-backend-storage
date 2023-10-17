#!/usr/bin/env python3
"""Python function that changes all topics of school document based on name"""


def update_topics(mongo_collection, name, topics):
    """Function that changes topics of school documents"""
    New_query = {"name": name}
    New_Topics = {"$set": {"topics": topics}}

    mongo_collection.update_many(New_query, New_Topics)
