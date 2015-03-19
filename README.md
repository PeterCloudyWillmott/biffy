##biffy
###The missing editor for B1if

A Django/Python 2.7 web application to make editing and testing B1if XSL and XML fast and fun.

This is a work in progress, considered unstable alpha.

![Biffy in action](/../screenshots/screens/BiffyScreen.jpg?raw=true "Biffy in action")

####Todo
* Improve UI
* Save file version history
* Password protect the whole app
* Test XSLT in browser against local changes
* Save XML to use for XSLT testing
* Lint or PrettyPrint XML contents
* Loads of testing
* Install Documentation

####Complete
* Save B1if server details
* List Scenarios
* List Flows
* List Files
* Show file contents
* Makup XML content
* Save file function

####Dependencies
* widget_tweaks

#### Install

Instructions coming soon, but this is a Django app, so something like:
* [Install Django](https://docs.djangoproject.com/en/1.7/topics/install/)
* Clone this repository locally
* Run the following setup commands
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
* Add B1if servers at /admin
* Use the editor at /
