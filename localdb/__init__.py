# © Amit Sharma <https://github.com/buddhhu>

from os.path import getsize
import asyncio, asyncio
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps

__version__ = "1.0"
__author__ = "Amit Sharma (GitHub: buddhhu)"


def run_async(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        return await asyncio.get_event_loop().run_in_executor(
            ThreadPoolExecutor(max_workers=multiprocessing.cpu_count() * 5),
            partial(function, *args, **kwargs),
        )
    return wrapper

class Database:
    def __init__(self, database_name="database"):
        self._cache = {}  # Why to read file again and again?
        self.name = database_name
        if self.name.endswith("/"):
            self.name += "database.json"
        elif not self.name.endswith(".json"):
            self.name += ".json"
        self._data()

    def _raw_data(self):
        """Returns raw data from database file"""
        try:
            with open(self.name, "r") as data:
                return data.read()
        except FileNotFoundError:
            self._create_database(self.name)
        return self._raw_data()

    def _data(self):
        """Converts raw data into dict"""
        if inspect.isawaitable(self._raw_data()):
            self._cache = eval(asyncio.get_event_loop().run_until_complete(self._raw_data()))
            return
        self._cache = eval(self._raw_data())

    def get(self, key):
        """Get the requested key, uses cache before reading database file."""
        if key in self._cache:
            return self._cache.get(key)

    def set(self, key=None, value=None, delete_key=None):
        """Set key with given value, delete_key delete from database."""
        data = self._cache
        if delete_key:
            try:
                del data[delete_key]
            except KeyError:
                pass
        if key and value:
            data.update({key: value})
        if not key and not value:
            return
        with open(self.name, "w") as dbfile:
            dbfile.write(str(data))
        self._data()
        return True

    def rename(self, key1, key2):
        """Rename a key with different name."""
        if key1 in self._cache:
            return self.set(key2, self.get(key1), key1)

    def delete(self, key):
        """Delete a key from database."""
        if key in self._cache:
            return self.set(delete_key=key)

    def _create_database(self, database_name: str = None):
        """Create database file. Default name is 'database.json'"""
        if not database_name:
            database_name = self.name
        with open(database_name, "w") as db:
            db.write(str({}))

    @property
    def size(self):
        """Size of database file."""
        try:
            return getsize(self.name)
        except FileNotFoundError:
            return 0


class AsyncDatabase(Database):
    def __init__(self, database_name="database"):
        self.name = database_name
        if self.name.endswith("/"):
            self.name += "database.json"
        elif not self.name.endswith(".json"):
            self.name += ".json"
        asyncio.get_event_loop().run_until_complete(self._data())

    @run_async
    def _raw_data(self):
        return super()._raw_data()

    @run_async
    def _data(self):
        return super()._data()

    @run_async
    def get(self, key):
        return super().get(key)

    @run_async
    def set(self, key=None, value=None, delete_key=None):
        return super().set(key=key, value=value, delete_key=delete_key)

    @run_async
    def delete(self, key):
        return super().delete(key)

    @run_async
    def rename(self, key1, key2):
        return super().rename(key1, key2)
