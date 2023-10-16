"""Python setup.py for myfastapi package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("myfastapi", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="myfastapi",
    version=read("myfastapi", "VERSION"),
    description="Awesome myfastapi created by qinlu1024",
    url="https://github.com/qinlu1024/myfastapi/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="qinlu1024",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["myfastapi = myfastapi.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
