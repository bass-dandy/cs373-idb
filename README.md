# Music-Mecca

## Slack
https://musicmecca.slack.com/

## Database

On your local machine, run `psql -d postgres -f <music-mecca_root>/init_db.sql` to initialize the database.
 
## Virtual Environment 

Create a new virtual by going into Pycharm/Settings/Project/Project Interpreter/ then click on the gear and select 'create new virtual environment' name it music-mecca_virtualenv. Make sure it's python 3.4


## Config 

On your local machine create/add to your ~/.profile this environmental variable CONFIG_PATH and set it equal to the location of config.py. Or if you're using Pycharm edit the configuration of manage and add CONFIG_PATH as well as the path. 

## Requirements

run pip install -r requirements.txt to install all flask modules needed 

## Rackspace VM

104.239.228.125<br>
user: mm<br>
pass: hold shift and hit all the number keys from 1-0

The public and private keys can be found in ~/.ssh if you want to use them instead.

## Using this repo

1. ONLY PUSH COMMITS TO DEV
2. A push to dev will initiate integration tests
3. Dev will automatically merge with Beta if the integration tests are successful
4. Once Dev merges with Beta, manually create a new pull request for your Beta changes
5. When another dev gives you a "ship it," manually merge your Beta changes to Master

Not all changes require a pull request. Specifically:<br>
* Cosmetic changes do not require a pull request
* Pair-programmed code does not require a pull request (include who you worked with in the commit message)

Everything else should require a pull request.

