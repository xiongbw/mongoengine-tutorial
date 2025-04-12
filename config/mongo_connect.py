import logging

from mongoengine import connect

from config.settings import MONGODB_SETTINGS

"""
Connect to MongoDB
https://docs.mongoengine.org/guide/connecting.html
"""

connect(**MONGODB_SETTINGS)

# Config pymongo logger
pymongo_logger = logging.getLogger('pymongo')
pymongo_logger.setLevel(logging.DEBUG)
