# Django Article Website

This is a Django-based web application for managing articles. The application includes functionalities for user authentication, creating, updating, listing, and liking articles.


## Features

- User Authentication
  - Login
  - Session management
- Article Management
  - Create, Update, and List articles
  - Like articles

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Virtualenv (optional but recommended)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/GeorgV87/django_article_website.git
    cd django_article_website
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000` to see the application.

## Usage

1. **Login:**
   - Navigate to the login page (`/login`) and log in using your credentials.

2. **Home Page:**
   - Once logged in, you will be redirected to the home page which displays user-specific information.

3. **Create Article:**
   - Navigate to the article creation page (`/article/create`) to create a new article.

4. **List Articles:**
   - Navigate to the articles list page (`/articles`) to view all articles.

5. **Like an Article:**
   - You can like an article by navigating to its detail page and clicking the "Like" button.

6. **Update Article:**
   - Navigate to the article update page (`/article/update/<article_id>`) to edit an existing article.


## Endpoints

- `/login` - Login page
- `/` - Home page
- `/article/create` - Create a new article
- `/articles` - List all articles
- `/article/update/<article_id>` - Update an existing article
- `/article/like/<article_id>` - Like an article