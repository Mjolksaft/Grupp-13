from mysql.connector import connect, Error
import hashlib

class DatabaseHandler():
    def __init__(self):
        self.currentUser = "none"
        self.dsn = {
            "user": "John",
            "password": "P@ssw0rd",
            "host": "localhost",
            "port": "3306",
            "database": "grupp13",
            "raise_on_warnings": True,
        }

    def hashPassword(self, password):
        """hashes the password"""
        hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashedPassword

    def createAccount(self, firstName, password):
        """Creates a account to the database"""
        # try:
        with connect(**self.dsn) as cnx:
            # Create a cursor object for prepared statements
            cursor = cnx.cursor(prepared=True)

            sql = """
                INSERT INTO users
                    (userName, password)
                VALUES
                    (?, ?)
            """

            args = (firstName, self.hashPassword(password))
            cursor.execute(sql, args)

            cnx.commit()

        # except Error as err:
        #     print(err)
        #     pass

    def login(self, userName, password):
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

            args = (userName,)
            cursor.execute(sql, args) # måste ha argument i en tuple eller en list så om du ska ha ett arugment gör (arg,)

            # Fetch the resultset
            res = cursor.fetchone()

            if res == None:
                return False
            elif res[0] == self.hashPassword(password):
                self.currentUser = res[1]
                return True
            else:
                return False

    def getTable(self):
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
                WHERE users.userId = ?
                ORDER BY time;
            """

            args = (self.currentUser,)
            cursor.execute(sql, args) # måste ha argument i en tuple eller en list så om du ska ha ett arugment gör (arg,)

            # Fetch the resultset
            res = cursor.fetchall()
            return res

    def addSubject(self, itemList):
        """add to the schedule"""
        try:
            with connect(**self.dsn) as cnx:
                cursor = cnx.cursor(prepared = True)
                
                sql = """
                    INSERT INTO schedule
                        (userId, subject, time, timeEnd)
                    values(?, ?, ?, ?)
                """

                args = (self.currentUser, itemList[0], itemList[1], itemList[2])
                cursor.execute(sql, args)
                cnx.commit()
        except Exception as err:
            print(err)

    def deleteContent(self):
        """deletes content from the database"""
        try:
            with connect(**self.dsn) as cnx:
                cursor = cnx.cursor(prepared = True)

                sql = """
                DELETE FROM schedule 
                WHERE userId = ?;
                """

                args = (self.currentUser, )
                cursor.execute(sql, args)
                cnx.commit()
        except Error as err:
            print(err)