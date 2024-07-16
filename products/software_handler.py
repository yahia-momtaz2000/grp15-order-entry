import mysql.connector

from db_connection.db_connection_factory import DbConnectionFactory
from products.software import Software


class SoftwareHandler:

    @staticmethod
    def insert_software(software):
        db_conn = None
        try:
            # 1- Create db Connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement
            sql_statement = ('insert into products'
                             ' (PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC)'
                             ' values'
                             ' (%s, %s, %s)')

            # 3- set parameters ( data ) %s
            values_tuple = (software.get_product_name(), software.get_product_retail_price(),
                            software.get_product_description())

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # Again insert into software table
            last_product_id = my_cursor.lastrowid
            sql_statement = ('insert into software'
                             ' (SOFTWARE_LICENCE, PRODUCT_ID)'
                             ' values'
                             ' (%s, %s)')
            values_tuple = (software.get_licence(), last_product_id)
            my_cursor.execute(sql_statement, values_tuple)

            # 5- commit changes
            db_conn.commit()

        except mysql.connector.Error as ex:
            print('Error in insert software function', ex)
        finally:
            if db_conn is not None:
                db_conn.close()

    @staticmethod
    def update_software(software):
        db_conn = None
        try:
            # 1- Create db Connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement
            sql_statement = ('update products'
                             ' set product_name = %s,'
                             ' PRODUCT_RETAIL_PRICE = %s,'
                             ' PRODUCT_DESC = %s'
                             ' where product_id = %s')

            # 3- set parameters ( data ) %s
            values_tuple = (software.get_product_name(), software.get_product_retail_price(),
                            software.get_product_description(), software.get_product_id())

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # Again update software table
            sql_statement = ('update software'
                             ' set SOFTWARE_LICENCE = %s'
                             ' where product_id = %s')

            values_tuple = (software.get_licence(), software.get_product_id())

            my_cursor.execute(sql_statement, values_tuple)

            # 5- Commit changes
            db_conn.commit()
        except mysql.connector.Error as ex:
            print('Error in update software function', ex)
        finally:
            if db_conn is not None:
                db_conn.close()
    @staticmethod
    def delete_software(product_id):
        db_conn = None
        try:
            # 1- Create db Connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement
            sql_statement = ('delete from software'
                             ' where product_id = %s')

            # 3- set parameters ( data ) %s
            values_tuple = (product_id, )

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # Again with products table
            sql_statement = ('delete from products'
                             ' where product_id = %s')
            my_cursor.execute(sql_statement, values_tuple)

            # 5- Commit changes
            db_conn.commit()
        except mysql.connector.Error as ex:
            print('Error in delete software function', ex)
        finally:
            if db_conn is not None:
                db_conn.close()

    @staticmethod
    def get_all_software():
        db_conn = None
        software_list = []
        try:
            # 1- Create db Connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement
            sql_statement = ('select products.PRODUCT_ID, PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC, '
                             ' SOFTWARE_LICENCE '
                             ' from products, software '
                             ' where products.product_id = software.product_id')

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement)

            # 5- Fetch all rows
            rows = my_cursor.fetchall()

            # 6- process ( loop ) each row and create software objects, append to List
            for row in rows:
                product_id = row[0]
                product_name = row[1]
                product_retail_price = row[2]
                product_description = row[3]
                software_licence = row[4]

                # create software object
                my_software = Software(product_id, product_name, product_retail_price, product_description, software_licence)
                software_list.append(my_software)
        except mysql.connector.Error as ex:
            print('Error in get_all_software function', ex)
        finally:
            if db_conn is not None:
                db_conn.close()
        return software_list

    @staticmethod
    def get_software_by_id(product_id):
        db_conn = None
        my_software = None
        try:
            # 1- Create db Connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement
            sql_statement = ('select products.PRODUCT_ID, PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC, '
                             ' SOFTWARE_LICENCE '
                             ' from products, software '
                             ' where products.product_id = software.product_id'
                             ' and products.product_id = %s')
            # 3- set parameters
            values_tuple = (product_id, )

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # 5- Fetch all rows
            row = my_cursor.fetchone()

            # 6- if row exists : create the object
            if row is not None:
                product_id = row[0]
                product_name = row[1]
                product_retail_price = row[2]
                product_description = row[3]
                software_licence = row[4]

                # create software object
                my_software = Software(product_id, product_name, product_retail_price, product_description, software_licence)

        except mysql.connector.Error as ex:
            print('Error in get_software_by_id function', ex)
        finally:
            if db_conn is not None:
                db_conn.close()
        return my_software


# main program

# test insert software
# software = Software(product_name='Java NetBeans', product_retail_price=500.0, product_description='Java IDEs',
#                     licence='zz-ttt-qqq')
# SoftwareHandler.insert_software(software)

# test update software function
# software = Software(product_id=10, product_name='Python IDE', product_retail_price=400.0,
#                     product_description='programming',
#                     licence='12-13-14-15')
# SoftwareHandler.update_software(software)

# test delete software function
# SoftwareHandler.delete_software(21)

# test get_all_software function
# software_list = SoftwareHandler.get_all_software()
# for software in software_list:
#     print('product id = ', software.get_product_id())
#     print('product name = ', software.get_product_name())
#     print('product retail price = ', software.get_product_retail_price())
#     print('product desc = ', software.get_product_description())
#     print('software licence = ', software.get_licence())
#     print('-------')

# test get_software_by_id function
software = SoftwareHandler.get_software_by_id(2)
print('product id = ', software.get_product_id())
print('product name = ', software.get_product_name())
print('product retail price = ', software.get_product_retail_price())
print('product desc = ', software.get_product_description())
print('software licence = ', software.get_licence())
