class MongoConnectionError(Exception):
    def __init__(self, url: str, message: str):
        self.url = url
        self.message = message
        super().__init__(f"Failed to connect to MongoDB at {url}: {message}")

class MongoSessionCreationError(Exception):
    def __init__(self, url: str, message: str):
        self.url = url
        self.message = message
        super().__init__(f"Failed to create session for MongoDB at {url}: {message}")
