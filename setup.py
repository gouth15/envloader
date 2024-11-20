from setuptools import find_packages, setup

with open("README.md", "r", encoding = "utf-8") as file:
    long_desc = file.read()

setup(
    name= "envloader",
    version = "0.1.1",
    author = "Goutham",
    author_email = "gouthams.330@gmail.com",
    description = "A simple package to load the env variables from the environment file",
    long_description = long_desc,
    long_description_content_type = "application/markdown",
    url = "https://github.com/gouth15/envloader.git",
    packages = find_packages(),
)