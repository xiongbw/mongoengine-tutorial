from mongoengine import connect
from config.settings import MONGODB_SETTINGS

"""
Connect to MongoDB
https://docs.mongoengine.org/guide/connecting.html
"""

connect(**MONGODB_SETTINGS)
