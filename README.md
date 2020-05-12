
## Masks Application
<p align="center">
 <kbd><img width="75" height="75" src="readme_assets/face_mask.gif"></kbd>

<p>&nbsp;</p>

* Masks is a content management system built on Django's "high-level Python web framework."
* The application uses Django's Administration module to manage digital information in a dashboard format.
* Sources to DIY "do-it-yourself" face masks or coverings found on public sites are displayed in the dashboard.

<p>&nbsp;</p>
<p align="center">
    <img width="80%" src="readme_assets/masks.gif" alt="Masks Slideshow">
</p>
<p>&nbsp;</p>

## Motivation

Project for Udemy's "Complete Python Bootcamp" course 2020 during the Coronavirus (COVID-19) lockdown and manditory wearing of face masks in public.

## DB Features

* Mask Title
* Materials
* Link to Source
* Date Published
* Thumbnail

## Commands

Commands   | Notes
---------- | ---------
http://127.0.0.1:8000/admin/login/?next=/admin/ | #clone git repo, login: admin/diymask
https://docs.djangoproject.com/en/3.0/ | #Django documentation
mysite>python manage.py runserver |	#start server
mysite>python manage.py makemigrations | #record changes to db
mysite>python manage.py migrate |	#migrate changes to db
https://sqlite.org/cli.html |	#sqlite3 command line shell
mysite>sqlite3 db.sqlite3 |	#open sqlite3 shell
sqlite>.help	|	#show sqlite3 commnds
sqlite>.schema |	#show database schema
sqlite>select * from masks_title; |	#run sql-like commands
sqlite>.exit |	#exit command line shell

## Installation and Documentation

Clone this repository or create your own CMS project by following the [Django documentation and tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/).

## Requirements

Masks CMS requires Python, Django and SQLite3 > 3.0.

Built with | Version
---------- | ---------
Python  | 3.7.4
Django  | 3.0.4
SQLite3 | 3.29.0


## License
Masks uses Django released under the under terms of the [MIT License](LICENSE).
