import json

from typing import Optional, Any, Type, TypeVar, Callable

from decouple import config, UndefinedValueError
from pydantic import BaseModel, Field, ValidationError, validator

T = TypeVar('T')


def env_var(field_name: str, default: Any = None, cast_type: Callable[[str], T] = str) -> T:
    try:
        value = config(field_name, default=default)
        if value is None:
            return default
        return cast_type(value)
    except UndefinedValueError:
        return default
    except (TypeError, ValueError) as e:
        if cast_type is None:
            raise ValueError(f"Failed to cast environment variable {field_name} to {str.__name__}") from e
        else:
            raise ValueError(f"Failed to cast environment variable {field_name} to {cast_type.__name__}") from e



class MongoConfig(BaseModel):
    host: str = Field(default_factory=lambda: env_var("MONGO_HOST", default="localhost"))
    port: int = Field(default_factory=lambda: env_var("MONGO_PORT", default=27017, cast=int))
    db: str = Field(default_factory=lambda: env_var("MONGO_DB", default="mydatabase"))
    user: Optional[str] = Field(default_factory=lambda: env_var("MONGO_USER", default=None))
    password: Optional[str] = Field(default_factory=lambda: env_var("MONGO_PASSWORD", default=None))
    url: Optional[str] = Field(default=None)

    def __repr__(self) -> str:
        attributes = self.dict(exclude={"url"})
        url = self.url or self.get_url()
        attributes['url'] = url
        attributes_str = json.dumps(attributes, indent=4)[1:-1]
        return f"{self.__class__.__name__}({attributes_str})"

    def __str__(self) -> str:
        return self.__repr__()

    def get_url(self) -> str:
        if self.user and self.password:
            return f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}"
        return f"mongodb://{self.host}:{self.port}"
