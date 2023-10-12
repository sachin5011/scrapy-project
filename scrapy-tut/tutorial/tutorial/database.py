import sqlite3

conn = sqlite3.connect("scrapper.db")
cursor = conn.cursor()
# cursor.execute("""
#     create table quote_tb(
#         quote text,
#         author text,
#         tags text
#     )
# """)

conn.commit()
conn.close()