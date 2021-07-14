import pandas as pd
import sqlite3
import subprocess
import os
from zipfile import ZipFile
from pathlib import Path
from datetime import datetime

def get_datetime():
    return str(datetime.now())[0:16]

def create_folders():
    folders = ['data/','data/raw/','db/']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    return

def download_data():
    kaggleCommand = "kaggle competitions download -c home-credit-default-risk -p data/raw -q"
    download_files = subprocess.Popen(kaggleCommand.split(), stdout=subprocess.PIPE)
    download_files.wait()
    zipfile = os.listdir("data/raw/")[0]
    if 'home-credit' not in zipfile:
        print("Download failed. Please check if kaggle.json is placed correctly at .kaggle\ and make sure that you have accepted the rules on https://www.kaggle.com/c/home-credit-default-risk/rules")
        quit()
    files = ZipFile('data/raw/'+zipfile).namelist()[1:-1]
    ZipFile('data/raw/'+zipfile).extractall(path='data/raw/',members=files)
    os.remove("data/raw/"+zipfile)
    return

def create_db():
    Path('db/home_credit.db').touch()

def connect_db(path_db):
    return sqlite3.connect(path_db)

def create_tables(conn, csv_files):
    for file in csv_files:
        print(f'# {get_datetime()} - Insert {file} to db')
        pd.read_csv("data//raw//" + file).to_sql(file.split(".")[0], conn, if_exists='replace', index=False)
    return

def main():
    print(f'\n##### {get_datetime()} - START - Setup.py ##### \n')

    print(f"# {get_datetime()} - Creating accessory folders\n")
    create_folders()
    
    print(f"# {get_datetime()} - Downloading data... It may take a while...\n")
    download_data()
    
    print(f"# {get_datetime()} - Creating database\n")
    create_db()

    print(f"# {get_datetime()} - Connecting db\n")
    conn = connect_db('db/home_credit.db')

    print(f"# {get_datetime()} - Insert data to db\n")
    csv_files = os.listdir("data/raw/")
    create_tables(conn,csv_files)

    print(f'\n##### {get_datetime()} END - Setup.py ##### \n')

if __name__=="__main__":
    main()
