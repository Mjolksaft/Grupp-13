"""
Welcome to the Database Handler.

"""
import hashlib

from mysql.connector import connect, Error



class DatabaseHandler():
    """Handles the data from the database MySql. """
    def __init__(self):
        self.current_user = "none"
        self.dsn = {
            "user": "John",
            "password": "P@ssw0rd",
            "host": "localhost",
            "port": "3306",
            "database": "grupp13",
            "raise_on_warnings": True,
        }

    def hash_password(self, password):
        """Hashes the password."""
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed_password

    def create_account(self, first_name, password):
        """Creates a account to the database"""
        try:
            with connect(**self.dsn) as cnx:
                # Create a cursor object for prepared statements
                cursor = cnx.cursor(prepared=True)

                sql = """
                    INSERT INTO users
                        (userName, password)
                    VALUES
                        (?, ?)
                """

                args = (first_name, self.hash_password(password))
                cursor.execute(sql, args)

                cnx.commit()

        except (Error) as err:
            print(err)

    def login(self, user_name, password):
        """Do example code."""
        with connect(**self.dsn) as cnx:

            # Create a cursor object for prepared statements
            cursor = cnx.cursor(prepared=True)

            # Execute the query
            sql = """
                SELECT
                    password,
                    userId
                FROM users
                WHERE 
                    userName = ?
            """

            args = (user_name,)
            cursor.execute(sql, args)

            # Fetch the resultset
            res = cursor.fetchone()

            if res is None:
                return False
            if res[0] == self.hash_password(password):
                self.current_user = res[1]
                return True
            return False

    def get_table(self, spinBoxValue):
        """get the schedule data from the database"""
        with connect(**self.dsn) as cnx:

            # Create a cursor object for prepared statements
            cursor = cnx.cursor(prepared=True)

            # Execute the query
            sql = """
                SELECT subject, 
                    time,
                    timeEnd,
                    users.userId
                FROM schedule 
                JOIN users 
                ON schedule.userID = users.userId
                WHERE users.userId = ? AND template = ?
                ORDER BY time;
            """

            args = (self.current_user, spinBoxValue, )
            cursor.execute(sql, args)

            # Fetch the resultset
            res = cursor.fetchall()
            return res

    def add_subject(self, item_list, scheduleId):
        """add to the schedule"""
        try:
            with connect(**self.dsn) as cnx:
                cursor = cnx.cursor(prepared = True)

                sql = """
                    INSERT INTO schedule
                        (template, userId, subject, time, timeEnd)
                    values(?, ?, ?, ?, ?)
                """

                args = (scheduleId, self.current_user, item_list[0], item_list[1], item_list[2])
                cursor.execute(sql, args)
                cnx.commit()
        except Exception as err:
            print(err)

    def delete_content(self, template):
        """deletes content from the database"""
        try:
            with connect(**self.dsn) as cnx:
                cursor = cnx.cursor(prepared = True)

                sql = """
                DELETE FROM schedule
                WHERE userId = ? AND template = ?;
                """

                args = (self.current_user, template, )
                cursor.execute(sql, args)
                cnx.commit()
        except Error as err:
            print(err)
