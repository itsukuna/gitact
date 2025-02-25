from setuptools import setup, find_packages

setup(
    name="gitact",
    version="0.1",
    install_requires=[
        "requests",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "gitact=gitact:main",
        ],
    },
    python_requires=">=3.10",
    author="Ayush Singh Arya",
    description="A CLI tool to fetch and display the latest GitHub events for a user.",
    url="https://github.com/itsukuna/gitact",
)
