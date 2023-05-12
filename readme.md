Amazonia
Amazonia is a web application that allows users to inform the drone's origin position, the object pickup position, and the delivery destination on a chessboard-like grid. The application then calculates the fastest path to pick up the package and deliver it to the destination, as well as the time elapsed by this path. It also lists the last 10 trips previously calculated by the application.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
What things you need to install the software and how to install them:

Python 3.7 or higher
pipenv (for dependency management)
Installing
A step by step series of examples that tell you how to get a development environment running:

Clone the repository
Install dependencies with pipenv: pipenv install
Run the application: pipenv run start
Usage
To use the application, follow these steps:

Access the web interface at http://localhost:8000/
Enter the drone's origin position, the object pickup position, and the delivery destination
The application will calculate the fastest path and display it on the screen, along with the time elapsed by this path. It will also list the last 10 trips previously calculated by the application.
Running the tests
Explain how to run the automated tests for this system

Break down into end to end tests
Explain what these tests test and why

Copy code
Give an example
And coding style tests
Explain what these tests test and why

Copy code
Give an example
Deployment
Add additional notes about how to deploy this on a live system

Built With
FastAPI - Web framework used
Pydantic - Data validation and settings management library
SQLAlchemy - SQL toolkit and ORM
Alembic - Database migration tool
Uvicorn - ASGI server
Authors
Mariano Cimino
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Hat tip to anyone whose code was used
Inspiration
etc
Feel free to customize this template as needed for your project. Good luck!
