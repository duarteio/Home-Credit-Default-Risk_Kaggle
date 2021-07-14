import pandas as pd
import sqlalchemy
import os

def create_ABT(query_folder,db_path,on_key='SK_ID_CURR'):
    conn = sqlalchemy.create_engine('sqlite:///' + db_path)
    queries = os.listdir(query_folder)
    base = open(query_folder + '/' + queries[0], 'r').read()
    df = pd.read_sql(base,conn)
    for sql in queries[1:]:
        query = open(query_folder + '/' + sql, 'r').read()
        df = pd.merge(df,pd.read_sql(query, conn),how='left',on=on_key)
    return df

def main():
    df = create_ABT('.queries', 'db/home_credit.db')

if __name__=="__main__":
    main()
