#!/usr/bin/env python3
"""
Insert a document in python
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert into collection
    Args:
        mongo_collection: collection object
        kwargs: the dictionary input
    Return: _id
    """
    if kwargs:
        res = mongo_collection.insert_one(kwargs)
        return res.inserted_id
    else:
        return
