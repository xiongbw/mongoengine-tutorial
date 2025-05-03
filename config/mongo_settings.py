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

    """
    Config for MongoDB Replica Set Server
    """
    REPLICA_SETTINGS = {
        'alias': 'replication',
        'host': 'mongodb://localhost:37017,localhost:37018,localhost:37019/db_charge?replicaSet=rs0',
    }

    MONGODB_SETTINGS = [
        STANDALONE_SERVER,
        REPLICA_SETTINGS
    ]
