import re

import setuptools

with open("localdb/__init__.py", "rt", encoding="utf8") as x:
    version = re.search(r'__version__ = "(.*?)"', x.read()).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="localdb.json",
    version=version,
    author="Amit Sharma",
    author_email="amitsharma123234@gmail.com",
    description="A helper script for easily handling of JSON file as database in local storage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/buddhhu/localdb.json",
    license="GNU AFFERO GENERAL PUBLIC LICENSE (v3)",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
