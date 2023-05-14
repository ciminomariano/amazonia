Amazonia
Amazonia is a web application that calculates the fastest path for a drone to pick up an object and deliver it to a destination on a chessboard-like grid.
The app also displays the time elapsed by the calculated path and lists the last 10 trips previously calculated by the application.

Deployed App
Frontend: https://amazoniafrontend.herokuapp.com/
Backend Swagger: https://amazoniaback.herokuapp.com/docs

Git Repositories
Frontend: https://github.com/ciminomariano/amazonia_front
Backend: https://github.com/ciminomariano/amazonia

Getting Started
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
To run this application, you need to have the following software installed:

Python 3.7 or higher
Pipenv (for dependency management)
Installing
To install and run the application, follow these steps:

Clone the repository
Install dependencies with Pipenv: pipenv install
Run the application: pipenv run start
Usage
To use the application, follow these steps:

Access the web interface at http://localhost:8000/
Enter the drone's origin position, the object pickup position, and the delivery destination
The application will calculate the fastest path and display it on the screen, along with the time elapsed by this path. It will also list the last 10 trips previously calculated by the application.

Built With

FastAPI - Web framework used
Pydantic - Data validation and settings management library
MongoDB - Database
Uvicorn - ASGI server
Author
Mariano Cimino

License
This project is licensed under the MIT License - see the LICENSE file for details.
