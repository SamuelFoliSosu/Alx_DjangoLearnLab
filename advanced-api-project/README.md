Advanced API Development with Django REST Framework

This project is a hands-on exploration of advanced API development using Django REST Framework (DRF). It is designed to demonstrate key concepts such as custom serializers, generic views, and permissions to build a robust and efficient API.

Table of Contents
Getting Started
Prerequisites
Installation
Database Migrations
Running the Server
Project Structure
Models and Serializers
API Endpoints
Permissions
Future Enhancements

Getting Started
Follow these steps to get a local copy of the project up and running on your machine.

Prerequisites
Python 3.8 or higher
pip (Python package installer)

InstallationClone the repository:git clone https://github.com/Alx_DjangoLearnLab/advanced-api-project.git
cd advanced-api-project
Create and activate a virtual environment:python3 -m venv venv
source venv/bin/activate
Install project dependencies:pip install Django djangorestframework
Database MigrationsApply the database migrations to create the necessary tables for the Author and Book models.python manage.py makemigrations api
python manage.py migrate
Running the ServerStart the development server to access the API.python manage.py runserver
The API will be available at http://127.0.0.1:8000/.Project Structure.
├── advanced-api-project/       # Project root
│   ├── advanced_api_project/   # Django project settings
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── api/                    # Django app for the API
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── migrations/
│   │   ├── models.py           # Defines the Author and Book models
│   │   ├── serializers.py      # Defines custom serializers for models
│   │   ├── urls.py             # App-specific URL patterns
│   │   └── views.py            # Generic views for CRUD operations
│   └── manage.py
└── README.md
Models and SerializersThe project features two primary models and their corresponding serializers:Author Model: A simple model with a name field.Book Model: Includes title, publication_year, and a ForeignKey to Author.BookSerializer: Serializes the Book model and includes a custom validation method to ensure the publication_year is not in the future.AuthorSerializer: Serializes the Author model and demonstrates a nested relationship by including the related books using the BookSerializer.API EndpointsThe API currently provides CRUD functionality for the Book model. All endpoints are accessible under the /api/ prefix.MethodEndpointDescriptionGET/api/books/Retrieve a list of all book instances.POST/api/books/Create a new book instance.GET/api/books/<id>/Retrieve a single book instance by its ID.PUT/api/books/<id>/Update an existing book instance by its ID.DELETE/api/books/<id>/Delete a book instance by its ID.PermissionsThe API endpoints are configured with Django REST Framework's permission classes to control access:Read-only access (GET requests) is available to any user, authenticated or not.Creation, update, and deletion (POST, PUT, PATCH, DELETE requests) require an authenticated user.Future EnhancementsThis project will be further developed to include:Filtering, Searching, and Ordering: Adding advanced query capabilities to the API endpoints to provide more flexibility.Unit Testing: Implementing comprehensive unit tests to ensure the integrity and reliability of all API endpoints and logic.