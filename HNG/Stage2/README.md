# Deploying a FastAPI Application with CI/CD Pipeline

- I forked [this repository](https://github.com/hngprojects/fastapi-book-project) repo as my starting point.

## What I worked on:

### 1. Implement the Missing Endpoint
- Added an endpoint to retrieve a book by its ID:
  - -  **Path:** `/api/v1/books/{book_id}`
  - - The endpoint returns a JSON response containing the book details.
  - - If the book does not exist, it returns a **404 Not Found** response.
  - - No books should be deleted from the database.


### 2. Set Up the CI Pipeline
 - Configured the CI pipeline to:
  - - Run `pytest` to execute existing tests.
  - - Trigger on pull requests to the `main` branch.
  - - Contain a job named exactly **test**.
  - - Fail if there are issues in the application.
  - - Succeed if all tests pass.


### 3. Set Up the Deployment Pipeline
- On merging a pull request to the `main` branch:
  - -  A workflow triggers a job named **deploy**.
  - - If successful, the site is automatically updated with the latest changes.


4. Dockerization Requirement:
- Created a `Dockerfile` to package the FastAPI application.
- The Dockerfile:
  - - Uses an official lightweight **Python** image as the base.
  - - Installs necessary dependencies for FastAPI.
  - - Exposes the required port and sets the appropriate FastAPI entry point.


### 5. Serve the Application Over Nginx
- Configured **Nginx** as a reverse proxy for the deployed application.
- Ensured API requests are correctly forwarded to the FastAPI backend.


### 6. Repository Access Requirement
- Before submitting your solution, invite the hng12-devbotops GitHub account as a collaborator to your repository.

-----

*Wanna check it out?*👉[Here's the implemented changes](https://github.com/Jepkor1r/fastapi-book-project)