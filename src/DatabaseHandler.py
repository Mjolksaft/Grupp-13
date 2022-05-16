from mysql.connector import connect, Error

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

    def createAccount(self, firstName, password):
        """Creates a account to the database"""
        try:
            with connect(**self.dsn) as cnx:
                # Create a cursor object for prepared statements
                cursor = cnx.cursor(prepared=True)

                sql = """
                    INSERT INTO users
                        (userName, password)
                    VALUES
                        (%s, %s)
                """

                args = (firstName, password)
                cursor.execute(sql, args)

                cnx.commit()

        except Error as err:
            print(err)

    def login(self, userName, password):
        """Do example code."""
        try:
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
                if res[0] == password:
                    self.currentUser = res[1]
                    return True
                else:
                    return False
        except Error as err:
            print(err)

    def getTable(self):
        """get the schedule data from the database"""
        try:
            with connect(**self.dsn) as cnx:

                # Create a cursor object for prepared statements
                cursor = cnx.cursor(prepared=True)

                # Execute the query
                sql = """
                    SELECT subject, 
                        time,
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
        except Error as err:
            print(err)

    def addSubject(self, subject, time):
        """add to the schedule"""
        try:
            with connect(**self.dsn) as cnx:
                cursor = cnx.cursor(prepared = True)
                
                sql = """
                    INSERT INTO schedule
                        (userId, subject, time)
                    values(?, ?, ?)
                """
                
                args = (self.currentUser, subject, time)
                cursor.execute(sql, args)
                cnx.commit()
                # print(args+ "succesfully added to database")

        except Error as err:
            print(err)