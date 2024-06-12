
# django_article_website

# Session_management_article_app

## Description
In this task, you will create a simple Django web application for managing articles. The application will have two types of users: admin and regular users. Admin users can create and edit articles, while regular users can like articles. Each user can only like an article once. You will implement session management to handle user roles.

## Requirements
Create a Django project and an app within the project.
Set up models for Article and Like (you can use sqlite3).
Create custom login view. 
Create views and templates to:
- Display a list of articles.
- Allow admins (superuser) to create and edit articles. (option should be shown only for superuser(admin))
- Allow regular users to like articles (like button will be shown only if user do not like this article before and only if he logged in).

Use session management.

