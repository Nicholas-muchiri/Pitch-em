Pitche-em
===================

- - - -
Author: [Nicholas Muchiri](https://github.com/Nicholas-muchiri/Pitch-em)
## Description
[Pitche*em](https://github.com/Nicholas-muchiri/Pitch-em) is a web application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.
The pitches are organized by category. You can have different categories like pickup lines, interview pitch , product pitch, promotion pitch.

------------------------------------------------------------------------

## User Requirements

1. user should see the pitches other people have posted.
2. user should comment on the different pitches and leave feedback.
3. user should submit a pitch in any category.
4. user should view the different categories.

## Features

+ [x] Create and display pitches based on categories
+ [x] Create category for pitches
+ [x] Display trending pitches based on day, week, month, year.
+ [x] Display the latest pitches and comments.
+ [x] Create user accounts with roles 
+ [x] Send email verification to users 
+ [x] Editing user profiles

## Specifications
[Specifications file](https://github.com/Nicholas-muchiri/pitch-em/Specs.md)


## Setup

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python 3.6

### Cloning the repository
```bash
git clone https://github.com/Nicholas-muchiri/pitch-em.git && cd pitche*em
```

### Creating a virtual environment

```bash
python3.6 -m venv --without-pip virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
```bash
 export MAIL_USERNAME=YOUR EMAIL
 export MAIL_PASSWORD=EMAIL PASSWORD
 export DATABASE_URL=POSTGRESQL DATABASE PATH WITH DRIVER
```

### Database migrations

```bash
# first initialize the database if the migrations folder does not exist
python manage.py db init
# create  a migration
python manage.py db migrate -m "initial migration"
# upgrade
python manage.py db upgrade
# insert initial data
python manage.py insert_initial_data
```

### Running Tests
```bash
python manage.py test
```
 
#### Development mode
The following are enabled in development mode 
```python 
class DevConfig(Config):
    DEBUG = True
    TESTING = True

```

Run server
```bash 
# starting server by defaut will run it in development mode
python manage.py server
```
Run server
```bash
python start.sh 
```
### Deploying to heroku
Set the configuration to production mode
```bash
heroku create appname
heroku heroku addons:create heroku-postgresql
git push heroku master
heroku run python2.7 manage.py db upgrade
```

## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Contributing

- Git clone [https://github.com/jakhax/pitches.git](https://github.com/Nicholas-muchiri/pitch-em.git) 
- Make the changes.
- Write your tests on `tests/`
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Nicholas Muchiri](https://github.com/Nicholas-muchiri)