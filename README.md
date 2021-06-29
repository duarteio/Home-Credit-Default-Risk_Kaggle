# Home-Credit-Default-Risk_Kaggle

# Setting environment
Clone this repository and follow the steps to configure environment.

## Create a python virtual environment
First, create a virtual environment for this project. To do this, install virtualenv package using pip and create an environment. After this, activate the virtual environment and install all required packages.
``` shell
  pip install virtualenv
  virtualenv venv
  venv/Scripts/activate # on windows, or venv/bin/activate on linux
  pip install -r requirements.txt
```

## Configuring Kaggle API
You need to download and authenticate the kaggle API using an API token, following the steps
described at https://www.kaggle.com/docs/api. Place the kaggle.json file in the location C:\Users\<Windows-username>\.kaggle\ (on Linux in the location ~/.kaggle/).

## Running setup code
Run 
```
python setup.py
```
This will do the following:
1. Create project folders
2. Download data into the data/ folder via kaggle API
3. 