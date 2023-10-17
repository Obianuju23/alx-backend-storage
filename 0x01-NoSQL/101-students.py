#!/usr/bin/env python3
"""Python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """function that return sorted average score of all students"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student

    
