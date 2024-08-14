#!/usr/bin/env python3
"""
finds documents based on attribte
"""


def def schools_by_topic(mongo_collection, topic):
    """
    outpus schools by topic
    :mongo_collection
    :topic
    """
    mongo_collection.find({"name": "topic"})
