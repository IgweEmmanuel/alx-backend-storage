#!/usr/bin/env python3
"""
update a collection in python
"""


def update_topics(mongo_collection, name, topics):
    """
    update collection
    Args:
        mongo_collection: collection object
        name: name of subject
        topics: subject topics
    Return: list of documents
    """
    mongo_collection.update_many(
                {"name": name},
                {"$set": {"topics": topics}}
            )
