import subprocess
import os

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
    lsCommand = "ls data//raw"
    ls = subprocess.Popen(lsCommand.split(), stdout=subprocess.PIPE)
    output, error = ls.communicate()
    dl_success = str(output)
    if 'home-credit' not in dl_success:
        print("Download failed. Please check if kaggle.json is placed correctly at .kaggle\ and make sure that you have accepted the rules on https://www.kaggle.com/c/home-credit-default-risk/rules")
        quit()
    unzipCommand = "unzip data//raw//* -d data//raw//"
    unzip = subprocess.Popen(unzipCommand.split(), stdout=subprocess.PIPE)
    unzip.wait()
    rmCommand = "rm data//raw//*.zip"
    subprocess.Popen(rmCommand.split(), stdout=subprocess.PIPE)
    return



def main():
    print("Creating accessory folders")
    create_folders()
    print("Downloading data... It may take a while...")
    download_data()
    print("The data was successfully downloaded!")

if __name__=="__main__":
    main()
