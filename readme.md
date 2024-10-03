# V8 Backend
This is a web application built with Django, a powerful and easy-to-use Python web framework. This readme helps you get started with Django by walking you through the setup.

## Requirements
Before you start, make sure you have the following installed:
* Python 3.*
* Django 4.* (or higher)
* pip (Python package manager)
* Git (to clone the repository and colab)

## Setup
1. Clone the repository
`git clone git@github.com:v8-senior-design/v8-backend.git
`
2. Create a virtual environment
`python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
`
3. Install dependencies
`pip install -r requirements.txt
`
4. Set up the database
`python manage.py migrate
`
5. Run the development server
`python manage.py runserver
`
6. Access the application
`Open your browser and go to http://127.0.0.1:8000/ to view the app.
`
