from setuptools import setup, find_packages

setup(
    name="mysql-flow",
    version="0.0",
    description="A Python manager for MySQL database..",
    author="Stephen Ka-Wah Ma",
    author_email="980907mjh@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mysql-connector-python",
    ],
    extras_require={"dev": []},
)
