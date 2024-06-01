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
        pass

    @staticmethod
    def get_company_by_id(customer_id):
        pass


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
CompanyHandler.delete_company(1)
