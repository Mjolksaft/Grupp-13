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
                        password
                    FROM users
                    WHERE 
                        userName = ?
                """

                args = (userName,)
                cursor.execute(sql, args) # måste ha argument i en tuple eller en list så om du ska ha ett arugment gör (arg,)

                # Fetch the resultset
                res = cursor.fetchone()
                if res[0] == password:
                    return True
                else:
                    return False
        except Error as err:
            print(err)

    def getTable(self, userId):
        """asd"""
        try:
            with connect(**self.dsn) as cnx:
                # Create a cursor object for prepared statements
                cursor = cnx.cursor(prepared=True)

                # Execute the query
                sql = """
                    SELECT
                        subject,
                        time
                    FROM schema
                    WHERE userId = ?
                """
                
                args = (userId,)
                print(f"# The SQL is:\n{sql}")
                print(f" the args are: {args}")
                cursor.execute(sql,args)

                # Fetch the resultset
                res = cursor.fetchall()
                print("\n# Printing out the resultset")
                print(res)

                # print("{0:<5} {1:<20} {2:<20}".format(*cursor.column_names))
                # print("-" * 60)
                # for row in res:
                #     print(f"{row[0]:<5} {row[1]:<20} {row[2]:<20}")

        except Error as err:
            print(err)
    

