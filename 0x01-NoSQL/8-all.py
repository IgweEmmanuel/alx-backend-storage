#!/usr/bin/env python3
"""
Python code that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    List all documents in a collection
    Args:
        mongo_collection: the collection object
    Return: object
    """
    return mongo_collection.find()
