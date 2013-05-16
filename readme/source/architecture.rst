.. _architecture:


********************************
Structure 
********************************
This page will briefly describe the architecture behind the Parallel-Text Project. In addition for paragraph on Hosting I will briefly describe why we chose that particular company over the competitors. 


.. _deployment
Deployment
=========

Parallel-Text is hosted entirely on Heroku. Heroku used to be Ruby on Rails platform exclusively. Recently, they have added support for Python/Django, node.js, Java and many other languages and frameworks.

We chose Heroku because of how simple it is to deploy the application. Parallel-Text was up and running on the cloud in a matter of minutes. Although, initially there were some issures regarding the deployment; but we were able to fix it successfully. 

Google App Engine was out of the picture because it does not have a support for SQL database. There are workarounds by using ``django-nonrel`` but we thought it was too much of a hassle, especially hosting companies like Heroku lets you deploy your Django applications with almost zero modifications.

One gotcha we run into is the fact that Heroku uses *Git* for deployment process, whereas our project uses *Mercurial* version control system. This involves an extra-step of initializing a git directory in order to deploy the project to Heroku.

.. _visitng-our-site
Visitng our site
======================

If you dont want to see our site, just visit the following link::

	http://parallel-text.herokuapp.com/

Sign up to the and your account will be activated. Once your account is created you can enjoy our full site with ability of reading two versions of a text in parallel.

This account has already been created for you::

	Username: blah
	Password: blah

.. _django-packages
Django and Packages
======================

Django==1.5.1
argparse==1.2.1
beautifulsoup4==4.1.3
distribute==0.6.34
dj-database-url==0.2.1
gunicorn==0.17.2
logilab-astng==0.24.3
logilab-common==0.59.1
psycopg2==2.5
wsgiref==0.1.2

Prallel-Text is built on top of Django 1.5.1. 

In addition to the django packages provided by the Pinax we have used the following libraries and python packages:

	* Django==1.5.1
	* argparse==1.2.1
	* beautifulsoup4==4.1.3
	* distribute==0.6.34
	* dj-database-url==0.2.1
	* gunicorn==0.17.2
	* logilab-astng==0.24.3
	* logilab-common==0.59.1
	* psycopg2==2.5
	* wsgiref==0.1.2

.. _database-configuration
Database Configuration
==================

In development we use SQLite database. It's extremely easy to setup and use. SQLite provides a fairly simple database storage as a file. 

In production we use PostgreSQL mainly because Heroku enforces it. It replaces your existing Django database settings with the PostgreSQL settings provided by Heroku upon deployment of the project.