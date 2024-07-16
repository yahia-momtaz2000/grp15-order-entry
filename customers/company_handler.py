from customers.company import Company
from db_connection.db_connection_factory import DbConnectionFactory
import mysql.connector


class CompanyHandler:

    @staticmethod
    def insert_company(company):
        db_conn = None
        try:
            # 1- Create db Connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement
            sql_statement = ('insert into customers'
                             ' (CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE,'
                             ' CUSTOMER_CONTACT, CUSTOMER_DISCOUNT, CUSTOMER_TYPE_ID)'
                             ' values'
                             ' (%s, %s, %s, %s, %s, 1)')
            # 3- set parameters ( data ) %s
            values_tuple = (company.get_customer_name(), company.get_customer_address(), company.get_customer_phone(),
                            company.get_contact(), company.get_discount())

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # 5- commit changes
            db_conn.commit()
        except mysql.connector.Error as ex:
            print('There is Error', ex)
        finally:
            if db_conn is not None:
                db_conn.close()

    @staticmethod
    def update_company(company):
        db_conn = None
        try:
            # 1- Create db Connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement ( insert )
            sql_statement = ('update customers'
                             ' set CUSTOMER_NAME = %s,'
                             ' CUSTOMER_ADDRESS = %s,'
                             ' CUSTOMER_PHONE = %s,'
                             ' CUSTOMER_CONTACT = %s,'
                             ' CUSTOMER_DISCOUNT = %s'
                             ' where CUSTOMER_ID = %s')

            # 3- set parameters ( data ) %s
            values_tuple = (company.get_customer_name(), company.get_customer_address(), company.get_customer_phone(),
                            company.get_contact(), company.get_discount(), company.get_customer_id())

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # 5- commit changes
            db_conn.commit()
        except mysql.connector.Error as ex:
            print('There is Error', ex)
        finally:
            if db_conn is not None:
                db_conn.close()

    @staticmethod
    def delete_company(company_id):
        db_conn = None
        try:
            # 1- Create db Connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement ( insert )
            sql_statement = ('delete from customers'
                             ' where customer_id = %s')

            # 3- set parameters ( data ) %s
            values_tuple = (company_id, )

            # 4- Create cursor and execute sql statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # 5- commit changes
            db_conn.commit()
        except mysql.connector.Error as ex:
            print('There is Error', ex)
        finally:
            if db_conn is not None:
                db_conn.close()

    @staticmethod
    def get_all_companies():
        db_conn = None
        companies_list = []
        try:
            # 1- create db connection
            db_conn = DbConnectionFactory.create_connection()

            # 2- prepare sql statement
            sql_statement = ('select CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE,'
                             ' CUSTOMER_CONTACT, CUSTOMER_DISCOUNT, CUSTOMER_TYPE_ID'
                             ' from customers'
                             ' where customer_type_id = 1')  # 1 company

            # 4- Create Cursor and execute statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement)

            # 5- Fetch all rows
            rows = my_cursor.fetchall()

            # 6- process ( loop ) each row and create company objects, append to List
            for row in rows:
                customer_id = row[0]
                customer_name = row[1]
                customer_address = row[2]
                customer_phone = row[3]
                customer_contact = row[4]
                customer_discount = row[5]
                # create object from Company
                company = Company(customer_id, customer_name, customer_phone,
                                  customer_address, customer_contact, customer_discount)
                companies_list.append(company)
        except mysql.connector.Error as ex:
            print('Error in get all companies function', ex)
        finally:
            if db_conn is not None:
                db_conn.close()

        return companies_list

    @staticmethod
    def get_company_by_id(customer_id):
        db_conn = None
        my_company = None
        try:
            # 1- create db connection
            db_conn = DbConnectionFactory.create_connection()
            # 2- prepare sql statement
            sql_statement = ('select CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE,'
                             ' CUSTOMER_CONTACT, CUSTOMER_DISCOUNT, CUSTOMER_TYPE_ID'
                             ' from customers'
                             ' where customer_type_id = 1'
                             ' and customer_id = %s')

            # 3- set parameters if found
            values_tuple = (customer_id, )

            # 4- Create Cursor and execute statement
            my_cursor = db_conn.cursor()
            my_cursor.execute(sql_statement, values_tuple)

            # 5- Fetch One Row
            row = my_cursor.fetchone()

            # 6- if row exists : create the object
            if row is not None:
                customer_name = row[1]
                customer_address = row[2]
                customer_phone = row[3]
                customer_contact = row[4]
                customer_discount = row[5]
                # create company object
                my_company = Company(customer_id, customer_name, customer_phone,
                                     customer_address, customer_contact, customer_discount)
        except mysql.connector.Error as ex:
            print('Error in get company by id function', ex)
        finally:
            if db_conn is not None:
                db_conn.close()

        return my_company

# main program

# test insert_company function
# my_company = Company(customer_name='Btech', customer_address='Cairo', customer_phone='01012312312',
#                      contact='Ahmed Hossam', discount=10)
# CompanyHandler.insert_company(my_company)


# test update_company function
# my_company = Company(customer_id=1, customer_name='Btech 2025', customer_address='Cairo - Maadi',
#                      customer_phone='01112312312',
#                      contact='Ibrahim Hossam', discount=20)
# CompanyHandler.update_company(my_company)

# test delete_company function
# CompanyHandler.delete_company(1)

# test get_all_companies
# companies_list = CompanyHandler.get_all_companies()
# for company in companies_list:
#     print('company id = ', company.get_customer_id())
#     print('company name = ', company.get_customer_name())
#     print('company address = ', company.get_customer_address())
#     print('company phone = ', company.get_customer_phone())
#     print('company contact = ', company.get_contact())
#     print('company discount = ', company.get_discount())
#     print('-----')

# test get_company_by_id
# company = CompanyHandler.get_company_by_id(6)
# print('company id = ', company.get_customer_id())
# print('company name = ', company.get_customer_name())
# print('company address = ', company.get_customer_address())
# print('company phone = ', company.get_customer_phone())
# print('company contact = ', company.get_contact())
# print('company discount = ', company.get_discount())