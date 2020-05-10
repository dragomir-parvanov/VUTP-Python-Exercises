Combined excercise 09-10-11-12 into one project. **If you wish to run this project for the first time, remember to execute "db_creator.py" first.**

Exercise 09

Exercise:

Write a program for personal contact book using Flask micro web framework.

Menu based interface for creating, updating, searching and removing records.  

The information needs to be stored in a semi-column(;) separated text file in the location where the server application is.

Following fields need to be used:

Name, Address, Birthday, Phone number, Email, Profession, Interests



Find attached the main structure of the flask web app. 


Exercise 10
The same exercise from last time, but this time use templates. 

And optionally cookies, sessions ids, create a login page, etc. 

Exercise 11
You can find the web application from previous exercises almost done - attached. 

It includes:

contactsbookwebapp.py - the Flask application itself 

/templates  - in templates folder different templates used from the webapp to visualize and get data 

/static  - static content of a web app as CSS 

mycontacts.db - this is the DB file which holds all saved contacts records which have been added.  All the APIs and functions are manipulating data residing in this file. 



Needs to be fulfilled: 

1. Complete /update route path and corresponding functions  - it is 50 % done . You need to complete the part which makes modification in the db file.

2. In order to increase the security of data and the web app itself by adding login functionality.

- There should be a username and password form when the first application has been loaded 

- A session mechanism needs to be used via 'session' object. ( You can find about it in previous materials or  search on Internet ) 

- The direct API call to other routes of an API of this web app should not be allowed unless the user first authenticated via username and password. 

Exercise 12
Refactor 'electronic contact book' Webapp with using SQLite python module and functionality for storing and working with the contact data. Use attached below file as base and rework it further. 
