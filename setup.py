"""Python setup.py for windows_temp_file_destroyer package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("windows_temp_file_destroyer", "VERSION")
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
    name="windows_temp_file_destroyer",
    version=read("windows_temp_file_destroyer", "VERSION"),
    description="Awesome windows_temp_file_destroyer created by m-310101",
    url="https://github.com/m-310101/windows-temp-file-destroyer/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="m-310101",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["windows_temp_file_destroyer = windows_temp_file_destroyer.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
