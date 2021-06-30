# Home Credit Default Risk
A Kaggle competition

This project was created to participate in a Kaggle prediction competition. Go to https://www.kaggle.com/c/home-credit-default-risk/overview for more information on the background of the competition and the data.

To be able to access the data, you will need to log into Kaggle website, to go to https://www.kaggle.com/c/home-credit-default-risk/rules and to click on the "I Understand and Accept" button to gain access.

# Requirements
The execution of all programs require the following programs:
1. python3 (required modules are listed in requirements.txt)
2. SQLite


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
2. Download and uncompress the data into the data/raw/ folder via kaggle API
3. Create SQLite database tables