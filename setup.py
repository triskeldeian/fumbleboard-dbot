# example from https://packaging.python.org/tutorials/packaging-projects/

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fumbleboard-dbot",
    version="1.0.0",
    author="triskeldeian, ypnoschris, kidpixo",
    author_email="triskeldeian@hotmail.com",
    description="A Discord bot to access the fumble board",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/triskeldeian/fumbleboard-dbot",
    packages=setuptools.find_packages(),
)