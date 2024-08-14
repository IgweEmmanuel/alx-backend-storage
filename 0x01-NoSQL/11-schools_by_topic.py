#!/usr/bin/env python3
"""
finds documents based on attribte
"""


def def schools_by_topic(mongo_collection, topic):
    """
    outpus schools by topic
    :param mongo_collection:
    :param topic:
    :return:
    """
    mongo_collection.find({"topics": topic})
