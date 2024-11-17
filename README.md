
# DJANGO_Set up (Beginner) 
-----------------------

## How to start..
- create virtual environment ` python -m venv venv ` {venv}=>"Any name you can use"

- activate on Windows (cmd.exe)
` venv\Scripts\activate `

-  activate on Windows (PowerShell)
` venv\Scripts\Activate.ps1 `

-  activate on Unix or MacOS
` source venv/bin/activate `

- install django in the virtual environment
` pip install django `

- start your django project
` django-admin startproject mysite `


---------------------
## After creation of project

- create a new page on the project
` python manage.py startapp core ` {core:name of the app page}

 - run the project
` python manage.py runserver `

mysql terminal connection:c:\Windows\path>echo "" > file.py



-------------------

## Any problem face in environment or incase  python is updated/not working the Django projects You Just Do It This...

- `cd env2`
- `cd Scripts`
- `activate`

-----------------------
## Creating a Django environment on Ubuntu Linux is straightforward. Here’s a step-by-step guide to help you set it up:

### Step 1: Install Python and pip
Make sure you have Python and pip installed. You can check your Python version with:

bash
python3 --version
If not installed, you can install Python and pip using:

bash
sudo apt update
sudo apt install python3 python3-pip
### Step 2: Create a Virtual Environment
A virtual environment keeps your project’s dependencies isolated from other projects. Create a virtual environment in your project directory:

bash
mkdir myproject
cd myproject
python3 -m venv env
### Step 3: Activate the Virtual Environment
Activate the virtual environment:

bash
source env/bin/activate
Your command prompt should now show the name of your virtual environment.

### Step 4: Install Django
With the virtual environment activated, install Django using pip:

bash
pip install django
### Step 5: Create a Django Project
Create a new Django project:

bash
django-admin startproject myproject
This will create a new directory with the necessary files for your Django project.

### Step 6: Run the Development Server
Navigate to your project directory and start the development server:

bash
cd myproject
python manage.py runserver
You should now be able to access your Django project at http://127.0.0.1:8000/ in your web browser.

Optional: Install Code Editor or IDE
For writing and editing your Django code, you might want to install a code editor or IDE like Visual Studio Code, PyCharm, or Sublime Text.

# How to set admin
### Create a Superuser
- Run the following command to create a superuser (admin user):
`` python manage.py createsuperuser ``
### Register Models with the Admin
- Open the admin.py file in your app directory and register your models:
  ```
  from django.contrib import admin
  from .models import YourModel

  admin.site.register(YourModel)
```

