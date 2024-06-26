**This guide will walk you through setting up the arka-test project. Prerequisites**

- Git
- Docker
- Docker Compose
1. **Cloning the Repository**

   Open your terminal.

   Clone the repository using the following command:

   Bash

   git clone https://github.com/erpan011J/Take-Home-Test-Arka.git

   Bash

   cd arka-test

2. **Setting Up Docker Environment**

   **Make sure Docker and Docker Compose are installed on your system.**

1. **Building and Running Docker Containers**

   Build and run the Docker containers in detached mode (background) using this command:

   Bash

   docker-compose up --build -d

2. **Accessing Django Shell**

   Use the following command to enter the Django container shell:

   Bash

   docker exec -it arka-test-web-1 /bin/bash

3. **Creating a Superuser**

   Inside the container, run the following command to create a superuser:

   Bash

   python manage.py createsuperuser

4. **Running Migrations**

   While still inside the container, run this command to apply database migrations:

   Bash

   python manage.py migrate

5. **Running Test Cases**

   Execute the following command inside the container to run the test suite:

   Bash

   python manage.py test

6. **API Documentation**

   Once you've run the application, Swagger documentation should be accessible at:

   [http://localhost:8000/swagger/ ](http://localhost:8000/swagger/)<http://localhost:8000/redoc/>

   **Authentication**

   Use the following steps to obtain a token for authentication:

   Make a POST request to http://localhost:8000/login/ with the superuser credentials created earlier, or access the login API via Swagger to retrieve the token and use it for Swagger authorization.

   **These links will only work if the application is running.**
