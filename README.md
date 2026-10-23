# Django Demo Web Application

A demo project of a small web application illustrating the basic concepts of **Django**. This repository is designed to demonstrate:
* **Core Architecture:** Apps, URLs, views, models (including the extension of default models with custom functionality) and validations, forms (including standard forms and custom forms inheriting from default forms e.g., `CustomLoginForm`).
* **Security:** Authentication, authorization, and group-based permissions.
* **Testing:** Tests implemented within the `users` app.

Front-end is built using **Bootstrap**

## Functionality

The application manages two primary types of entities: **Books** and **Users**. Because login is required globally, users must authenticate to access any part of the application. 

Access and capabilities depend on the user's assigned group:
* **Medewerker** (=employee): Has full CRUD permissions for both **Books** and **Users**.
* **Lezer** (=reader): Has read-only permissions and can only view the list of books.


## Preset Accounts (For Testing)

For convenience and testing purposes, the repository includes two preset accounts:

| Username | Password | User Group | Permissions |
| :--- | :--- | :--- | :--- |
| `lezer` | `lezer` | Lezer | Read-only access to books |
| `medewerker` | `medewerker` | Medewerker | Full CRUD access to books and users |

## Deployment & Docker

The repository includes `Dockerfiles` and configuration files to easily build and run the application inside a **Docker container** if needed.

## ⚠️ Important Security Note

This repository is **not production-ready**, as settings.py of the project contains debug set to true, contains the secret_key, etc.

This setup was done intentionally, as the sole purpose of this project is to demonstrate the fundamentals of Django development.
