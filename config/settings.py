__MONGO_VERSION__ = "4.4.16"

"""
Settings for MongoDB Standalone Server
"""
MONGODB_SETTINGS = {
    'db': 'test',
    'host': 'localhost',
    'port': 27017
}

"""
Settings for MongoDB Replica Set Server with URI string
https://docs.mongoengine.org/guide/connecting.html#connect-with-uri-string

MONGODB_SETTINGS = {
    'host': 'mongodb://localhost:37017,localhost:37018,localhost:37019/db_charge?replicaSet=rs0',
}
"""
