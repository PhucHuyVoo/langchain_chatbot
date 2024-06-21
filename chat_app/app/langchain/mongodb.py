import config
import pymongo


class MongoDB:
    def __init__(self):
        self.connection_string = f"mongodb://{config.MONGODB_USER}:{config.MONGODB_PASSWORD}@{config.MONGODB_URI}:{config.MONGODB_PORT}"

    def get_connection_string(self):
        return self.connection_string
    
