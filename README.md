# CETL_OSP_backend
 
##Introduction
The CMS is bulit by Django, one of the famous Python Web Framework.

##Anaconda Environment
Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. Django and other Python dependencies can be installed into Conda environment so that it would not interfere the OS environment. Please follow the instruction here to install Conda:
https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

##Procedures
1. Create and enter conda environment named "cetl_cms":
```
conda create --name cetl_cms
conda activate cetl_cms
```
1. Clone this repository from Github:
```
git clone https://github.com/wongcht/CETL_OSP_backend.git
```
2. Install packages and start the CMS process
```
cd */CETL_OSP_backend/cetl
pip install requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser #Create admin account in the CMS
python manage.py runserver
```

##Usage
1. The process is run in http://localhost:8000
2. Admin has to login first so as to CRUD the survey, click "Staff Login" in the main page and use your created admin account to login
3. Admin can do most of the functions in "Survey List and Edit"
4. Admin has to refresh the page to view the updated changes

##Remarks
1. It is by default using .sqlite3 file to store data, you can change to other database like MySQL. (https://docs.djangoproject.com/en/3.1/ref/settings/#databases)
2. RESTful API (partly completed) is in http://localhost:8000/api/surveys/
