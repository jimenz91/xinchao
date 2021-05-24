# XINCHAO

## Overview

This project contains the backend coding challenge for a finctional restaurant called Xin Chào. Every command mentioned below should be executed inside the project directory with a terminal.

## Setting up the environment

Python 3.8+ and any sort of virtual environment must be installed in order to run the system. With virtualenv, for example, create a virtual environment inside the project directory.

```
python -m venv [dir_name]
```

Activate it by typing:

```
source [dir_name]/bin/activate
```

## Installing dependencies

Once its activated, install all the dependencies:

```
python pip install -r requirements.txt
```

## Creating the database, tables and columns

Before starting the server, it is important to create and apply all the migrations to create the database:

```
python manage.py makemigrations
python manage.py migrate
```

## It is not mandatory to populate the database this way, but a set of json files have been supplied in order to fill the database with some dummy data automatically

```
python manage.py loaddata fixtures.json
```

## A superadmin user can be created by executing the following command, and following the instructions

```
python manage.py createsuperuser
```

## With everything setup, you should be able to start the server with by typing:

```
python manage.py runserver
```

The server is started by default on port 8000

## Applications & Endpoints

The system has one app, called "menu" which contains all the database interactions, business logic and API endpoints. This menu app has two sets of endpoints which can be consumed. The first set is available with the following URLs:

```
http://127.0.0.1:8000/api/v1/orders/    supports GET, POST methods
http://127.0.0.1:8000/api/v1/orders/id  supports GET, PUT, DELETE methods
```

This endpoints are used to interact with the orders API and its model. The table and dish API has a similar pattern, but changing "orders" for either "tables" or "dishes". All of these endpoints come with a GUI with detailed examples of how to interact create new instances of the model.

The second set of complementary URLs are:

```
http://127.0.0.1:8000/menu/model_name             supports GET method
http://127.0.0.1:8000/menu/model_name/id          supports GET method
http://127.0.0.1:8000/menu/model_name/filtered    supports GET method
```

"model_name" refers to the name of the moodel (or database table) that you want to consume. Since they are consumed dynamically, it can either be "dish", "table" or "order". The second endpoint works the same, although with an "id" which refers to the identifier (an integer) of a specific instance of a model in the database. The third endpoint retrieves items from the model by passing the filters as path parameters.
