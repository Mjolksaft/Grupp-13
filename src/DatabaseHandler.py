from mysql.connector import connect, Error

class DatabaseHandler():
    def __init__(self):
        self.dsn = {
            "user": "John",
            "password": "P@ssw0rd",
            "host": "localhost",
            "port": "3306",
            "database": "grupp13",
            "raise_on_warnings": True,
        }

    def getPassword(self, userName):
        """hämtar lösenord hashen från användarnamn"""
        try:
            with connect(**self.dsn) as cnx:
                cursor = cnx.cursor()
                cursor.execute("SELECT password FROM users WHERE username = %s", (userName,))
                password = cursor.fetchone()[0]
                return password
        except Error as e:
            print(e)

    def getSalt(self, userName):
        """Hämtar salt från användarnamn"""
        try:
            with connect(**self.dsn) as cnx:
                cursor = cnx.cursor()
                cursor.execute("SELECT salt FROM users WHERE username = %s", (userName,))
                salt = cursor.fetchone()[0]
                return salt
        except Error as e:
            print(e)

    def createAccount(self, firstName, password, salt):
        """Creates a account to the database"""
        try:
            with connect(**self.dsn) as cnx:

                # Create a cursor object for prepared statements
                cursor = cnx.cursor(prepared=True)

                sql = """
                    INSERT INTO users
                        (userName, password, salt)
                    VALUES
                        (%s, %s, %s)
                """

                print(f"# The SQL is:\n{sql}")

                args = (firstName, password, salt)
                print(f" the args are: {args}")
                cursor.execute(sql, args)

                print(f"Rows affected. {cursor.rowcount}")

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
                        *
                    FROM users
                    WHERE 
                        userName = ?
                        AND password = ?
                """

                args = (userName, password)
                print(f"# The SQL is:\n{sql}")
                print(f" the args are: {args}")
                cursor.execute(sql, args) # måste ha argument i en tuple eller en list så om du ska ha ett arugment gör (arg,)

                # Fetch the resultset
                res = cursor.fetchall()
                print("\n# Printing out the resultset")
                print(res)

                print("{0:<3} {1:<8} {2:<8}".format(*cursor.column_names))
                print("-" * 53)
                for row in res:
                    print(f"|{row[0]:<5} | {row[1]:<20} | {row[2]:<20}|")

        except Error as err:
            print(err)

    
