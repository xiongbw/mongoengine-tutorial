import logging

# Config pymongo logger
pymongo_logger = logging.getLogger('pymongo')
pymongo_logger.setLevel(logging.DEBUG)


class MongoConfig:
    __MONGO_VERSION__ = "4.4.16"

    """
    Config for MongoDB Standalone Server
    """
    STANDALONE_SERVER = {
        'alias': 'standalone',
        'db': 'test',
        'host': 'localhost',
        'port': 27017
    }

    MONGODB_SETTINGS = [
        STANDALONE_SERVER
    ]
