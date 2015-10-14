## Music-Mecca

## Slack
https://musicmecca.slack.com/

## Database

On your local machine, run `psql -d postgres -f <music-mecca_root>/init_db.sql` to initialize the database. 

## Rackspace VM
104.239.228.125
user: mm
pass: hold shift and hit all the number keys from 1-0

## Using this repo

1. ONLY PUSH COMMITS TO DEV
2. A push to dev will initiate integration tests
3. Dev will automatically merge with Beta if the integration tests are successful
4. Once Dev merges with Beta, manually create a new pull request for your Beta changes
5. When another dev gives you a "ship it," manually merge your Beta changes to Master

Not all changes require a pull request. Specifically:
1. Cosmetic changes do not require a pull request
2. Pair-programmed code does not require a pull request (include who you worked with in the commit message)

Everything else should require a pull request.

