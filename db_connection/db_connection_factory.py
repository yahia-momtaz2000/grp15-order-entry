import mysql.connector


class DbConnectionFactory:
    # static variables for db credentials [ configurations ]
    USER = 'root'
    PASSWORD = 'root'
    HOST = 'localhost'
    DATABASE = 'oe'
    # PORT

    @staticmethod
    def create_connection():
        db_conn = None
        try:
            db_conn = mysql.connector.connect(user=DbConnectionFactory.USER,
                                              password=DbConnectionFactory.PASSWORD,
                                              host=DbConnectionFactory.HOST,
                                              database=DbConnectionFactory.DATABASE)
            print('db connection successful')
            db_conn.autocommit = False
        except mysql.connector.Error as ex:
            print('DB Connection Failed', ex)
        return db_conn

# main program
# my_conn = DbConnectionFactory.create_connection()
# print(my_conn)
