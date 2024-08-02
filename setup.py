from setuptools import setup, find_packages

setup(
    name="mongo_motors",
    version="0.4.0",
    description="Mongo Motors is an asynchronous, singleton-based connection pooling mechanism for MongoDB",
    author="Alireza Heidari",
    author_email="alirezaheidari.cs@gmail.com",
    url="https://github.com/alirezaheidari-cs/mongo-motors",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "motor",
        "python-decouple",
        "pydantic>=2",
    ],
    license='Apache License 2.0',
    keywords="mongodb async-mongodb motor async-client nosql nosql-database motor-client",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    python_requires='>=3.6',
    project_urls={
        "Documentation": "https://github.com/alirezaheidari-cs/mongo-motors#readme",
        "Source": "https://github.com/alirezaheidari-cs/mongo-motors",
        "Tracker": "https://github.com/alirezaheidari-cs/mongo-motors/issues",
    },
)
