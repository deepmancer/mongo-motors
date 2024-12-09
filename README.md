# 🌱 Mongo Motors - Async MongoDB Client

<p align="center">
    <img src="https://img.shields.io/badge/MongoDB-47A248.svg?style=for-the-badge&logo=MongoDB&logoColor=white" alt="MongoDB">
    <img src="https://img.shields.io/badge/PyPI-3775A9.svg?style=for-the-badge&logo=PyPI&logoColor=white" alt="PyPI">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=for-the-badge" alt="License">
</p>

`mongo-motors` is your go-to Python package for seamless asynchronous MongoDB operations. Built on top of the `motor` library, it provides a robust and efficient way to manage MongoDB connections, ensuring thread-safe and high-performance interactions with your database.

---

| **Source Code** | **Website** |
|:-----------------|:------------|
| <a href="https://github.com/deepmancer/mongo-motors" target="_blank">github.com/deepmancer/mongo-motors</a> | <a href="https://deepmancer.github.io/mongo-motors/" target="_blank">deepmancer.github.io/mongo-motors</a> |

---

## ✨ Features

- **⚡ Asynchronous MongoDB Connections:** Leverages the power of `motor` for non-blocking database operations.
- **🔄 Singleton Design Pattern:** Manages MongoDB connections with a singleton, ensuring efficient and thread-safe usage.
- **🔧 Easy Configuration:** Configure your MongoDB client effortlessly using `MongoConfig`.
- **📜 Context Manager Support:** Simplifies MongoDB session management with context managers.
- **🔗 Fully Compatible with `motor`:** Seamlessly integrates with the `motor` library for all your MongoDB needs.

## 📦 Installation

Get started quickly by installing `mongo-motors` using pip:

```sh
pip install git+https://github.com/yourusername/mongo-motors.git
```

## 🛠️ Quick Start

### 🔧 Configuration

Start by creating a configuration object using `MongoConfig`:

```python
from mongo_motors import MongoConfig

config = MongoConfig(
    host='localhost',
    port=27017,
    db='mydatabase',
)
```

### 🏗️ Creating an AsyncMongo Instance

Next, create an instance of `AsyncMongo` using your configuration:

```python
from mongo_motors import AsyncMongo

async def main():
    mongo_client = await AsyncMongo.create(config=config)
    print(f"Connected to MongoDB at: {mongo_client.url}")
```

### ⚙️ Managing MongoDB Sessions

Interact with your MongoDB server using the context manager from `get_or_create_session`:

```python
from mongo_motors import AsyncMongo

async def main():
    mongo_client = await AsyncMongo.create(config=config)

    async with mongo_client.get_or_create_session() as session:
        # Perform MongoDB operations
        result = await session.collection_name.insert_one({'key': 'value'})
        document = await session.collection_name.find_one({'_id': result.inserted_id})
        print(f"Inserted document: {document}")

    await mongo_client.disconnect()
```

### 🔍 Example Usage

Here's a complete example to demonstrate how `mongo-motors` works:

```python
import asyncio
from mongo_motors import AsyncMongo, MongoConfig

async def main():
    config = MongoConfig(
        host='localhost',
        port=27017,
        db='mydatabase',
    )
    client = await AsyncMongo.create(config=config)

    async with client.get_or_create_session() as session:
        # Insert a document
        await session.collection_name.insert_one({'key': 'value'})
        
        # Retrieve the document
        document = await session.collection_name.find_one({'key': 'value'})
        print(f"Document found: {document}")
        
        # Delete documents based on a condition
        keys = [{'key': 'value1'}, {'key': 'value2'}, {'key': 'value3'}]
        for key in keys:
            await session.collection_name.delete_many(key)
        
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```

### 🛡️ Error Handling

`mongo-motors` provides custom exceptions to handle various MongoDB-related issues:

- `MongoConnectionError`
- `MongoSessionCreationError`

### 🔌 Disconnecting

Gracefully disconnect from your MongoDB server when you're done:

```python
await mongo_client.disconnect()
```

## 📄 License

This project is licensed under the Apache License 2.0. For more details, see the [LICENSE](https://github.com/yourusername/mongo-motors/blob/main/LICENSE) file.

---

**Supercharge your MongoDB operations with `mongo-motors` today!** 🌱
