import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="sqlalchemy-sql-migrate",
    version="0.2",
    author="Daniel Nordberg",
    author_email="dnordberg@gmail.com",
    description=("Very simple manual sql or python migrations for SQLAlchemy."),
    license="BSD",
    install_requires=["docopt"],
    keywords="python sqlalchemy migrate migration",
    url="http://github.com/dnordberg/sqlalchemy-sql-migrate",
    packages=['sqlalchemysqlmigrate',],
    long_description=read('README.rst'),
    scripts=['sqlalchemysqlmigrate/sqlmigrate',],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: BSD License",
    ],
)
