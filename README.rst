SQLAlchemy SQL Migrate
======================

Very simple manual sql migrations for SQLAlchemy.

The following should be defined in SQLAlchemy

.. code-block::

    class DBVersion(Base):
        '''Store db version for manual migrations.
        '''
        __tablename__ = 'db_version'
        __table_args__ = table_args
        version = Column(Integer, primary_key=True)

SQLAlchemy doesn't have many options for database migrations.

Alembic assumes that the full schema was defined accurately by SQLAlchemy and
that SQLAlchemy was used to create the initial schemas (which would have
stamped the database with the most current alembic migration version at the
time of creation).

When this is the case, its easy to use alembic to manage further migrations
since alembic will only migrate changes from the initial schema. However,
SQLAlchemy doesn't create an accurate representation of the schema because some
schema changes cannot be defined in SQLAlchemy, e.g. uniqueindexes with lengths
defined in columns, and using sqlachemy relationships without corresponding
foreign keys defined in the database.

This script aims to provide an easy method of migrating a SQLAlchemy database
that doesn't rely on the API but on manual SQL.

All calls to create the schema using SQLAlchemy (Calls to
`Base.metadata.create_all(config.db_engine)`) should be replaced will calls to
this python library (`import migrate; migrate.up()`) which will maintain
migration status (To provide an easy migration path from Alembic and
SQLAlchemy).

Note: If version aren't incremental they are skipped or ignored for the
purposes of this script.

This is to make customization of a database as easy as possible and not to
modify the state of the database except as intended by the user.

The API is simple

Create a file migrations.env.

Set migrations.engine and db_session to a SQLAlchemy engine and session.

.. code-block::

    >> import migrations.migrate
    >> migrate.up(version)
    >> migrate.down(version)

To generate the first version of the schema, dump your db schema using the
command 'schema_dump' or create a schema dump manually and place it
in 'up/1.sql'. No corresponding 'down/1.sql' file should exist.

If you want to create the initial schema using SQLAlchemy run

.. code-block::

    >> Base = declarative_base()
    >> Base.metadata.create_all(config.db_engine)

Usage:
------

.. code-block::

    sqlmigrate [-v] migrations_env
    sqlmigrate [-v] schema_dump
    sqlmigrate [-v] version
    sqlmigrate [-v] new [MIGRATION_TYPE]
    sqlmigrate [-v] up [VERSION]
    sqlmigrate [-v] down VERSION
    sqlmigrate [-v] create_db [--initial]
    sqlmigrate [-v] drop_db
    sqlmigrate [-v] load FILE
    sqlmigrate [-v] remove VERSION
    sqlmigrate [-v] stamp [VERSION]
    sqlmigrate --version

    Arguments:
        migrations_env        Create directory structure holding migrations
        schema_dump           Create first migration by dumping database
        new                   Add a new migration (Default MIGRATION TYPE=sql)
        MIGRATION_TYPE        Migration type, 'sql' or 'py'
        up                    Migrate up (If no VERSION is specified, migrate to
                                latest)
        down                  Migrate down
        VERSION               Version to migrate to
        create_db             Recreate the database
        drop_db               Drop database
        load                  Load database from file
        FILE                  Database file to load
        remove                Removes a entry from the db_version table so that the
                                migration can be reapplied (Provided it is in a highest
                                current version)
        stamp                 Stamp a migration as already having taken place
                                (If no VERSION is specified, stamp to latest)

        Options:
        -h --help
        -v --verbose          verbose mode
        --version             Show version
        --initial             Load migration 0
