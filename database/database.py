import sqlite3

class Database:
    def __init__(self, db_name):
        """
        Initializes the database connection.
        :param db_name: Name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        """
        Creates a table with the given name and columns.
        :param table_name: Name of the table.
        :param columns: A string of column definitions.
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.connection.commit()

    def insert(self, table_name, data):
        """
        Inserts data into the specified table.
        :param table_name: Name of the table.
        :param data: A dictionary of column/value pairs to insert.
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data.values()))
        self.connection.commit()

    def query(self, query, parameters=None):
        """
        Executes a query and returns the results.
        :param query: SQL query to execute.
        :param parameters: Optional parameters for the query.
        """
        self.cursor.execute(query, parameters or [])
        return self.cursor.fetchall()

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()