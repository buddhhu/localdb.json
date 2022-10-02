## [localdb.json](https://github.com/buddhhu/localdb.json)
**A helper script for easily handling of JSON file as database in local storage.**

---
### Installation
- `pip install localdb.json`

---
### Usage

#### Creating instance
```python
from localdb import Database

db = Database("example.json")
```

---
#### Saving some data
This creates a key with the given value. It will overwrite existing key's value. Always returns `True`.
```python
db.set("TEST", "VALUE")
>>> True
```

---
#### Getting saved data
Returns value of requested key if it exists or will return `None`.
```python
db.get("TEST")
>>> VALUE
```

---
#### Renaming a key
Renames an existing key to another. Returns `True` if it exists or will return `None`.
```python
db.rename("TEST", "Test")
>>> True
```

---
#### Deleting a key
Deletes key and value from database. Returns `True` if it exists or will return `None`.
```python
db.delete("Test")
>>> True
```

---
#### Database size
Size of database file is returned in bytes.
```python
db.size
>>> 42
```

---
### Issues ?
Open issues or ask [here](https://t.me/botsrealm)

### Contributing
Pull requests are welcome.

### License
Licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3.

### Credits
- [Me](https://github.com/buddhhu)
