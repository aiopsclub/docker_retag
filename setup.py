#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py
import os
import re
import sys

from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ["docker_retag"]

requires = ["requests==2.23.0"]
test_requirements = []

about = {}
with open(os.path.join(here, "docker_retag", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=packages,
    package_dir={"docker_retag": "docker_retag"},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    project_urls={"Source": "https://github.com/aiopsclub/docker_retag",},
)
