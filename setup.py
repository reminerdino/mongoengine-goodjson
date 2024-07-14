#!/usr/bin/env python
# coding=utf-8
"""Setup script."""

import sys
from setuptools import setup, find_packages

dependencies = ["mongoengine", "dateutils"]
desc = "More human readable JSON serializer/de-serializer for MongoEngine"
version = "0.0.0"

# For compatibility with py2
file_not_found_err = None
try:
    file_not_found_err = FileNotFoundError
except NameError:
    file_not_found_err = IOError

try:
    with open("VERSION") as v:
        version = v.read()
except file_not_found_err:
    version = "0.0.0"

if sys.version_info < (2, 7):
    raise RuntimeError("Not supported on earlier then python 2.7.")

try:
    from functools import singledispatch  # noqa
except ImportError:
    dependencies.append("singledispatch")

try:
    with open('README.md') as readme:
        long_desc = readme.read()
except Exception:
    long_desc = None

setup(
    name="mongoengine_goodjson_v2",
    version="2.0.2",
    description=desc,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=dependencies,
    zip_safe=False,
    author="Hiroaki Yamamoto, edited by Iman Ashoori",
    author_email="imanashoorii.77@gmail.com",
    license="MIT",
    keywords="json mongoengine mongodb",
    url="https://github.com/reminerdino/mongoengine-goodjson",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5"
    ]
)
