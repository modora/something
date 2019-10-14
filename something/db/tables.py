import sqlite3

import pypika


class Column:
    """
    Table column
    """

    def __init__(self, name, type_, **kwargs):
        """
        :name:      column name
        :type_:     column type
        :kwargs:    column constraints
        """
        self.name = name
        self.type = type_
        self.constrants = _ColumnConstraints(**kwargs)

    def _create_sql(self):
        """
        Returns the substring required to create the table for this column e.g.
            CREATE TABLE some_table (column_sql) 
        """
        # TODO: foreign key support
        column_sql = f"{self.name} {self.type}"
        return column_sql


class _ColumnConstraints:
    """
    Constraints for table columns
    """

    def __init__(self, primary_key=None, not_null=None, foreign_key=None):
        pass


class ForeignKey:
    """
    Foreign key restraint

    :table:     reference table name
    :key:       reference key name
    """

    def __init__(self, table, key):
        self.table = table
        self.key = key


class Table:
    """
    Table base class
    """

    name = None

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        if not isinstance(value, list):
            raise TypeError("Expected a list of columns")
        elif not all(map(lambda v: isinstance(v, Column), value)):
            # if any of the values are not Column types
            raise TypeError("Expected a list of columns")
        self._columns = value

    def create(self, cursor, if_not_exists=True):
        """
        Creates the table
        """

        column_sql = ", ".join([column._create_sql for column in self.columns])
        sql_substring_list = [
            "CREATE TABLE",
            f"{self.name}",  # table name
            f"( {column_sql} )",
        ]
        if if_not_exists:
            sql_substring_list.insert("IF NOT EXISTS", 1)
        sql = " ".join(sql_substring_list)
        cursor.execute(sql)


class FileIndex(Table):
    """
    Contains all files in the archive
    """

    name = "Files"

    def __init__(self):
        self.columns = [Column("id", "TEXT", primary_key=True), Column("name", "TEXT")]


class FileMetadata(Table):
    """
    Contains the metadata for each file in the archive 
    """

    name = "FileMetadata"

    def __init__(self):
        self.columns = [
            Column("id", "INTEGER", primary_key=True),
            Column("fileId", "FOREIGN_KEY"),
            Column("key", "TEXT"),
            Column("value", "TEXT"),
        ]


class CollectionIndex(Table):
    """
    Contains all collections in the archive
    """

    name = "Collections"

    def __init__(self):
        self.columns = [Column("id", "TEXT", primary_key=True), Column("name", "TEXT")]


class CollectionMetadata(Table):
    """
    Contains the metadata for each collection in the archive
    """

    name = "CollectionMetadata"

    def __init__(self):
        self.columns = [
            Column("id", "INTEGER", primary_key=True),
            Column("collectionId", "FOREIGN_KEY"),
            Column("key", "TEXT"),
            Column("value", "TEXT"),
        ]


class ItemIndex(Table):
    """
    Contains all the items of a collection for all collections in the archive
    """

    name = "Items"

    def __init__(self):
        self.columns = [
            Column("id", "TEXT", primary_key=True),
            Column("collectionId", "FOREIGN_KEY"),
            Column("name", "TEXT"),  # item display name
        ]


class ItemMetadata(Table):
    """
    Contains the metadata for each item of a collection for all collections
    """

    name = "ItemMetadata"

    def __init__(self):
        self.columns = [
            Column("id", "INTEGER", primary_key=True),
            Column("collectionId", "FOREIGN_KEY"),
            Column("key", "TEXT"),
            Column("value", "TEXT"),
        ]


class Users(Table):
    """
    Contains a list of users in the database
    """

    name = "Users"

    def __init__(self):
        self.columns = [
            Column("id", "INTEGER", primary_key=True),
            Column("name", "TEXT"),
        ]


class Credentials(Table):
    """
    User credentials
    """

    name = "Credentials"

    def __init__(self):
        self.columns = [
            Column("userId", "FOREIGN_KEY", primary_key=True),
            Column("salt", "TEXT"),
            Column("hash", "TEXT"),
        ]


class Groups(Table):
    """
    User groups
    """

    name = "Groups"

    def __init__(self):
        self.columns = [
            Column("id", "INTEGER", primary_key=True),
            Column("name", "TEXT"),
        ]
