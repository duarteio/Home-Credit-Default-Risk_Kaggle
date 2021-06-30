import pandas as pd
import sqlite3
import subprocess
import os
from zipfile import ZipFile
from pathlib import Path


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
    ZipFile('data/raw/'+zipfile).extractall(path='data/raw/')
    os.remove("data/raw/"+zipfile)
    return


def connect_db():
    Path('db/home_credit.db').touch()
    return sqlite3.connect('db/home_credit.db')


def create_tables(conn,csv_files):
    for file in csv_files:
        pd.read_csv("data//raw//" + file).to_sql(file.split(".")[0], conn, if_exists='replace', index=False)
    return


def main():
    print("Creating accessory folders")
    create_folders()
    print("Downloading data... It may take a while...")
    download_data()
    print("The data were successfully downloaded!")
    print("")

    print("Creating database")
    conn = connect_db()
    c = conn.cursor()
    csv_files = os.listdir("data/raw/")
    create_tables(conn,csv_files)


if __name__=="__main__":
    main()
