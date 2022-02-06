# © Amit Sharma <https://github.com/buddhhu>

from os.path import getsize

__version__ = "1.0"
__author__ = "Amit Sharma (GitHub: buddhhu)"


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
