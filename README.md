[![Emmanuel Kakaire](https://img.shields.io/badge/Emmanuel%20Kakaire-MyDiary-green.svg)]()
[![Coverage Status](https://coveralls.io/repos/github/kakaemma/MyDairy/badge.svg?branch=dev)](https://coveralls.io/github/kakaemma/MyDairy?branch=dev)
[![Build Status](https://travis-ci.org/kakaemma/MyDairy.svg?branch=dev)](https://travis-ci.org/kakaemma/MyDairy)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-blue.svg)]()

# MyDairy
MyDiary is an online journal where users can pen down their thoughts and feelings.
#
Follow this [link](https://kakaemma.github.io/MyDairy/ "My Diary UI demo") for project UI demo
# Features
A user can;
* Sign up
* Login
* Create a diary
* Add description to the diary
* View the diary items

### API resources

These are the endpoints available in My Diary API

Endpoint | Description| Access Rights
------------ | ------------- | ------------- 
POST /api/v1/register | Registers a user | All
POST /api/v1/login |Logs a user in | All
POST /api/v1/diary |Adds a diary entry | logged in user
GET /api/v1/diary |Retrieves all diary entries | logged in user
GET /api/v1/diary/<diary_id> |Retrieves a single diary entry | logged in user



### Requirements
`Python 3+, python-pip, virtualenv`

### Installation

Clone the repository

```
git clone https://github.com/kakaemma/MyDairy.
cd MyDiary
```
### Create a virtualenv, and activate it:
I am assuming you are using a windows machine

```
virtualenv env
cd env/Scripts/activate
```

### Then install all dependecies required to run the application

```
pip install requirements.txt
```
### Then, run the application:
```
$ python run.py
```
### To see the application running:
Install postman and access the application at:

```
http://localhost:5000
```
