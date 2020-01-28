import pandas as pd
import sqlalchemy
import pymysql


#dialect+driver://username:password@host:port/database
#mysql:pymysql://root:root@localhost:3306/dressmaker01'
engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost:3306/dressmaker01")
print(engine)
print(type(engine))
df = pd.read_sql_table('tailor_tags', engine)
print(df)

df = pd.read_sql_query("select tailor_tailor_id, tags from tailor_tags where tailor_tailor_id=2", engine)
print(df)

userid = input("Input id: (1, 2, 6, 7): ")

df = pd.read_sql_query("select tailor_tailor_id, tags from tailor_tags where tailor_tailor_id='%s'" %(userid), engine)
print(df)