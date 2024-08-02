import asyncio
import contextlib
from typing import Dict, Optional, AsyncIterator

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pydantic import BaseModel

from .config import MongoConfig
from .exceptions import MongoConnectionError, MongoSessionCreationError

class AsyncMongo:
    """A class for managing asynchronous MongoDB connections."""

    _instances: Dict[str, 'AsyncMongo'] = {}
    _locks: Dict[str, asyncio.Lock] = {}

    def __new__(cls, config: MongoConfig, *args, **kwargs) -> 'AsyncMongo':
        """Ensures a singleton instance for each unique MongoDB connection URL."""
        url: str = config.get_url()
        if url not in cls._locks:
            cls._locks[url] = asyncio.Lock()
        if url not in cls._instances:
            cls._instances[url] = super().__new__(cls)
        return cls._instances[url]

    def __init__(self, config: MongoConfig) -> None:
        """Initializes the AsyncMongo instance."""
        if not hasattr(self, '_initialized') or not self._initialized:
            self._config: MongoConfig = config
            self._mongo_client: Optional[AsyncIOMotorClient] = None
            self._initialized: bool = True

    @classmethod
    async def create(cls, config: Optional[MongoConfig] = None, **kwargs) -> 'AsyncMongo':
        """Creates or returns an existing instance of AsyncMongo."""
        if config is None:
            config = MongoConfig(**kwargs)
        url: str = config.get_url()
        if url not in cls._locks:
            cls._locks[url] = asyncio.Lock()
        async with cls._locks[url]:
            if url not in cls._instances:
                instance = cls(config)
                await instance.connect()
                cls._instances[url] = instance
        return cls._instances[url]

    async def connect(self) -> None:
        """Connects to the MongoDB server."""
        if self._mongo_client is None:
            try:
                self._mongo_client = AsyncIOMotorClient(self._config.get_url())
                await self._mongo_client.server_info()
            except Exception as e:
                raise MongoConnectionError(url=self.url, message=str(e))

    async def disconnect(self) -> None:
        """Disconnects from the MongoDB server."""
        if self._mongo_client:
            self._mongo_client.close()
            self._mongo_client = None

    @contextlib.asynccontextmanager
    async def get_or_create_session(self) -> AsyncIterator[AsyncIOMotorDatabase]:
        """Creates a new session or returns an existing one."""
        await self.connect()
        try:
            yield self._mongo_client[self._config.database] if self._config.database else self._mongo_client.get_default_database()
        except Exception as e:
            raise MongoSessionCreationError(url=self.url, message=str(e))

    async def reconnect(self) -> None:
        """Reconnects to the MongoDB server."""
        await self.disconnect()
        await self.connect()

    @property
    def url(self) -> str:
        """Returns the MongoDB URL."""
        return self._config.get_url()
