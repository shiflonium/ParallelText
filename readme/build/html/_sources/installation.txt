.. _installation:


********************************
Installation and Getting Started
********************************

This guide will walk you through the installation process of Parallel-Text Project.

.. _installing-docdir:
Installation
============

Step 1: Visit the www.bitbucket.com  site:

.. figure:: visitBB.png
	:align: center

Step 2: You can sign up: 

.. figure:: signin.png
	:align: center

Step 3: Once you have create one, search Parallel-Text on the search bar.

.. figure:: searchBar.png
	:align: center
	
Step 4: After that you have to visit our master repo:

.. figure:: visitMasterRepo.png
	:align: center

Step 5: This time you have to fork the master repo:

.. figure:: forkingTheMaster.png
	:align: center	
	
Step 6: Forking the repo: 

.. figure:: forking.png
	:align: center
	
Step 7: Cloning the repo:

.. figure:: clone.png
	:align: center

Step 8: Cloning the repo to the local machine:

.. figure:: colning on the local machine.png
	:align: center

Step 9: Installing Pip:

.. figure:: pipInstall.png
	:align: center


Step 10: Open the terminal and navigate to parallelText directory:

Change the directory to the parallelText directory:

.. figure:: cdToParallelText.png
	:align: center

Step 11: Once you there please type the the following::

  > virtualenv .

Step 12: This will instantiate the virtual environment in the current directory. Now that we have a virtual environment, let's activate it::
  
  > source bin/activate

Step 13: Next naviate to the ``parallelText/requirements`` directory and execute the following command to install project dependencies inside the current virtual environment::

  > pip install -r requirements.txt

Step 14: Now you are ready to run the django server and start using the application. *But first you must navigate back to the project root folder*::

  > python manage.py runserver
	
.. figure:: runServer.png
	:align: center

Step 15: Visit the localhost: 

Open any browser and type http://127.0.0.1:8000/

Congratulations! That was pretty simple, wasn't it? In the next paragraph you can see the project structure in a tree-style format.

Done! Now you can start implementing additional stuff to the project.

.. _project-tree-structure
Project tree structure
======================

Our project uses structure looked like this::

  
  ├── acceptanceTest
  │   ├── deleteaccount.py
  │   ├── dictionary.py
  │   ├── ......
  │   └── invalidSignin.py
  ├── books
  │   ├── __init__.py
  │   ├── models.py
  │   ├── tests.py
  │   └── views.py
  ├── bs4
  │   ├── __init__.py
  │   ├── builder
  │   │   └── __init_.py
  │   │   └── _html5lib
  │   │   └── _htmlparser.py
  │   │   └── _lxml.py
  │   ├── dammit.py
  │   ├── element.py
  │   ├── testing.py
  │   └── tests
  │   │   └── __init__.py
  │   │   └── test_builder_registry.py
  │   │   └── test_docs.py
  │   │   └── ........
  │   │   └── test_tree.py
  ├── content_mgmt
  │   ├── __init__.py
  │   ├── forms.py
  │   ├── models.py
  │   ├── README.txt
  │   ├── scripts
  │   │   └── __init__.py
  │   │   └── ......
  │   │   └── parse_text_to_html.py
  │   ├── templates
  │   │   └── content_mgmt
  │   ├── test.py
  │   └── views.py
  ├── dajax
  │   ├── __init__.py
  │   ├── core.py
  │   ├── models.py
  │   └── static
  │   │   └── dajax
  ├── dataxice
  │   ├── __init__.py
  │   ├── core
  │   │   └── __init__.py
  │   │   └── Dajaxice.py
  │   ├── decorators.py
  │   ├── exceptions.py
  │   ├── finders.py
  │   ├── models.py
  │   ├── templates
  │   │   └── dajaxice
  │   ├── templatestags
  │   │   └── __init__.py
  │   │   └── dajaxice_templatetags.py
  │   ├── urls.py
  │   ├── utils.py
  │   └──  views.py
  ├── DATABASE
  │   ├── book_translation_populate.py
  │   ├── bookinfo_populate.py
  │   ├── languages_populate.py
  │   ├── POPULATE_ALL_TABLES.py
  │   ├── users_populate.py
  │   └── word_translation_populate.py
  ├── dictionary
  │   ├── __init__.py
  │   ├── forms.py
  │   ├── models.py
  │   ├── templates
  │   │   └── dictionary
  │   ├── tests.py
  │   └── views.py
  ├── documentation
  │   ├── code_samples
  │   │   └── dictionaryGrabber.py
  │   └── lint
  │   │   └── ADMIN_LINT
  │   │   └── GLOBAL_LINT
  │   │   └── KEVIN_LINT
  │   │   └── lint.sh
  │   │   └── LIRON_LINT
  │   │   └── YOHATAN_LINT
  ├── help
  │   ├── __init__.py
  │   ├── models.py
  │   ├── templates
  │   │   └── help
  │   ├── tests.py
  │   └── views.py
  ├── home
  │   ├── __init__.py
  │   ├── models.py
  │   ├── README.txt
  │   ├── templates
  │   │   └── home
  │   ├── tests.py
  │   └── views.py
  ├── languages
  │   ├── __init__.py
  │   ├── models.py
  │   ├── tests.py
  │   └── views.py
  ├── manage.py
  ├── parallel_display
  │   ├── __init__.py
  │   ├── ajax.py
  │   ├── forms.py
  │   ├── models.py
  │   ├── README.txt
  │   ├── templates
  │   │   └── parallel_display
  │   ├── test.py
  │   └── views.py
  ├── pt_main
  │   ├── __init__.py
  │   ├── book1.db
  │   ├── README.txt
  │   ├── settings.py
  │   ├── static
  │   │   └── home
  │   │   └── parallel_display
  │   ├── templates
  │   │   └── pt_main
  │   ├── urls.py
  │   └── wsgi.py
  ├── ptext
  │   ├── __init__.py
  │   ├── models.db
  │   ├── READM
  │   ├── templates
  │   ├── templatestags
  │   ├── test.py
  │   └── views.py
  ├── readme
  │   ├── build
  │   ├── Makefile
  │   └── source
  ├── search
  │   ├── __init__.py
  │   ├── models.py
  │   ├── README.txt
  │   ├── templates
  │   ├── tests.py
  │   └── views.py
  ├── texts
  │   ├── Bible_Genesis
  │   └── Quran
  ├── users
  │   ├── __init__.py
  │   ├── forms.py
  │   ├── models.py
  │   ├── README.txt
  │   ├── templates
  │   ├── tests.py
  │   └── views.py
  ├── dataxice
  │   ├── deleteaccount.py
  │   ├── dictionary.py
  │   ├── ......
  │   └── invalidSignin.py
  ├── dataxice						
  │   ├── media
  │   │   └── products
  │   └── static
  │       ├── admin
  │       │   ├── css
  │       │   ├── img
  │       │   │   ├── admin
  │       │   │   └── gis
  │       │   └── js
  │       │       └── admin
  │       ├── css
  │       ├── images
  │       │   ├── misc
  │       │   └── orbit
  │       ├── img
  │       ├── js
  │       ├── pinax
  │       │   └── js
  │       └── products
  ├── static
  │   ├── css
  │   ├── img
  │   └── js
  └── templates
      ├── about
      ├── outfits
      └── profiles

All django applications are stored in the apps folder. Note that none of the applications use app-specific templates or static files. Templates, javascript, css, and images are located in the project-level ``templates`` and ``static`` directories respectively.

Static folder is pretty self-explanatory. It contains project-wide stylesheets, javascripts and images, e.g. site logo. 

Last but not least, templates folder contains Django templates. Global templates are located at the root of the ``templates`` folder, while app-specific templates are located in the their respective folder inside the ``templates`` directory.