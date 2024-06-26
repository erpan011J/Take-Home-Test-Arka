**This guide will walk you through setting up the arka-test project.**
### <a name="_nz7oski21x0b"></a>**Prerequisites**
- Git
- Docker
- Docker Compose

1. ### <a name="_i2xjelgezc5v"></a>**Cloning the Repository**
   Open your terminal.

   Clone the repository using the following command:

   ```bash
   git clone https://github.com/erpan011J/Take-Home-Test-Arka.git
   ```

   ```bash
   cd \Take-Home-Test-Arka
   ```
1. ### <a name="_tnui462pesne"></a>**Setting Up Docker Environment**
   **Make sure Docker and Docker Compose are installed on your system.**
1. ### <a name="_mdn1dsdojiu2"></a>**Building and Running Docker Containers**
   Build and run the Docker containers in detached mode (background) using this command:

   ```bash
   docker-compose up --build -d
   ```

1. ### <a name="_uk2nzudc6n8e"></a>**Accessing Django Shell**
   Use the following command to enter the Django container shell:
   
   ```bash
   docker exec -it take-home-test-arka-web-1 /bin/bash
   ```

1. ### <a name="_l62s91xz3iv5"></a>**Creating a Superuser**
   Inside the container, run the following command to create a superuser:
   
   ```bash
   python manage.py createsuperuser
   ```
1. ### <a name="_q6ifut7hnvo4"></a>**Running Migrations**
   While still inside the container, run this command to apply database migrations:

   ```bash
   python manage.py migrate
   ```
   
1. ### <a name="_i5b4ss80ehy1"></a>**Running Test Cases**
   Execute the following command inside the container to run the test suite:
   
   ```bash
   python manage.py test
   ```

1. ### <a name="_vkgfk9dm9nbs"></a>**API Documentation**
   Once you've run the application, Swagger documentation should be accessible at:

   <http://localhost:8000/swagger/>
   
   <http://localhost:8000/redoc/>
   
   #### <a name="_uwm97detslcd"></a>**Authentication**
   Use the following steps to obtain a token for authentication:
   **
   
   Make a POST request to http://localhost:8000/login/ with the superuser credentials created earlier, or access the login API via Swagger to retrieve the token and use it for Swagger authorization.
   
   **These links will only work if the application is running.**

