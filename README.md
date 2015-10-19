# Music-Mecca

## Using this repo
1. Create a branch for whatever feature you're working on (You can have multiple)
2. <span style="color:red"><b>ONLY PUSH COMMITS TO YOUR PERSONAL BRANCHES</b></span>
3. When your branch is feature-complete, create a pull request to merge it with Dev
4. When another group member gives you a "ship it," merge your branch with Dev. Changes to Dev will initiate integration testing.
5. Dev will automatically merge into Beta if the integration tests are successful
6. Once Dev merges into Beta we'll all monitor the status of the Beta server
7. If we agree the Beta server looks stable we'll merge Beta into Master

Not all changes require a pull request. Specifically:
* Cosmetic changes do not require a pull request
* Pair-programmed code does not require a pull request (include who you worked with in the commit message)

Everything else should require a pull request.

## Useful Links
* Slack: https://musicmecca.slack.com/
* Travis: https://travis-ci.org/naughtyfiddle/music-mecca
* Rackspace VM: 104.239.228.125
  * user: mm
  * pass: hold shift and hit all the number keys from 1-0

The public and private keys can be found in ~/.ssh if you want to use them instead.

## Running the Project

### Database
On your local machine, run `psql -d postgres -f <music-mecca_root>/init_db.sql` to initialize the database.
 
### Virtual Environment 
Create a new virtual by going into Pycharm/Settings/Project/Project Interpreter/ then click on the gear and select 'create new virtual environment' name it music-mecca_virtualenv. Make sure it's python 3.4

### Config 
On your local machine create/add to your ~/.profile this environmental variable CONFIG_PATH and set it equal to the location of config.py. Or if you're using Pycharm edit the configuration of manage and add CONFIG_PATH as well as the path. 

### Requirements
run pip install -r requirements.txt to install all python modules needed 
