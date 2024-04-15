import psycopg2


# from colorama import Fore as color

class DatabaseManager:
    def __init__(self, database, user, password, host="localhost", port=5432):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.conn = psycopg2.connect(database=self.database,
                                         user=self.user,
                                         password=self.password,
                                         host=self.host,
                                         port=self.port)
            print("Connected to database successfully")
        except psycopg2.Error as e:
            print("Error while connecting to PostgreSQL", e)

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data
            (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """)
            self.conn.commit()
            print("Table created successfully")
        except psycopg2.Error as e:
            print("Error while creating table:", e)

    def close_connection(self):
        try:
            self.conn.close()
            print("Connection closed successfully")
        except psycopg2.Error as e:
            print("Error while closing connection:", e)


if __name__ == "__main__":
    db_manager = DatabaseManager(database="mydatabase",
                                 user="postgres",
                                 password="your_password")
    db_manager.connect()
    db_manager.create_table()
    db_manager.close_connection()

# def table_create():
#     try:
#         conn = psycopg2.connect(database="users",
#                                 user="postgres",
#                                 password="pgadmin",
#                                 host="localhost",
#                                 port="5432")
#         print(color.LIGHTBLUE_EX + "Connection established")
#         cursor = conn.cursor()
#         cursor.execute("""CREATE TABLE IF NOT EXISTS user_data(
#             id SERIAL PRIMARY KEY,
#             name TEXT NOT NULL,
#             email VARCHAR UNIQUE NOT NULL)""")
#         conn.commit()
#         print(color.LIGHTGREEN_EX + "Table created successfully")
#     except psycopg2.Error as er:
#         print(color.LIGHTRED_EX, "Error while connecting to PostgreSQL", er)
#     finally:
#         if conn is not None:
#             conn.close()
#
#
# if __name__ == "__main__":
#     table_create()

# conn = psycopg2.connect(database="users",
#                         user="postgres",
#                         password="pgadmin",
#                         host="localhost",
#                         port=5432)
#
# cursor = conn.cursor()
# cursor.execute("""select * from users""")
# for i in cursor.fetchall():
#     print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]}")
#
# conn.commit()
# conn.close()
