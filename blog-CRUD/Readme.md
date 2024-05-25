# Blog-CRUD

Welcome to the Blog-CRUD repository. This project is a Django-based application with API endpoints documented below. The project uses Poetry for dependency management and a Makefile for common commands.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
  - [Authentication](#authentication)
  - [Blog Posts](#blog-posts)
    - [List Blog Posts](#list-blog-posts)
    - [Retrieve a Blog Post](#retrieve-a-blog-post)
    - [Create a Blog Post](#create-a-blog-post)
    - [Update a Blog Post](#update-a-blog-post)
    - [Delete a Blog Post](#delete-a-blog-post)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

   ```sh
   https://github.com/nasif-raihan/IntimationInc-Workshops.git
   cd blog-CRUD
   ```

2. Install Poetry if you haven't already:

   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:

   ```sh
   poetry install
   ```

4. Apply migrations:

   ```sh
   make migrate
   ```

5. Create a superuser:

   ```sh
   make superuser
   ```

6. Run the development server:

   ```sh
   make run
   ```

## Usage

Use the following commands to manage the project:

- **Migrate database**: `make migrate`
- **Create a superuser**: `make superuser`
- **Run the development server**: `make run`

## API Documentation

### Authentication

API endpoints for authentication are provided by Django Rest Framework's built-in views.

### Blog Posts

#### List Blog Posts

- **URL**: `/api/blogposts/`
- **Method**: GET
- **Description**: Retrieve a list of all blog posts.

  **Request**:

  ```sh
  GET /api/v1/
  ```

  **Response**:

  ```json
  [
      {
          "id": 1,
          "title": "First Blog Post",
          "content": "This is the content of the first blog post.",
          "created_at": "2024-05-18T12:34:56Z",
          "last_modified": "2024-05-18T12:34:56Z",
          "created_by": 1
      },
      ...
  ]
  ```

#### Retrieve a Blog Post

- **URL**: `/api/v1/{id}/`
- **Method**: GET
- **Description**: Retrieve details of a specific blog post by ID.

  **Request**:

  ```sh
  GET /api/v1/1/
  ```

  **Response**:

  ```json
  {
      "id": 1,
      "title": "First Blog Post",
      "content": "This is the content of the first blog post.",
      "created_at": "2024-05-18T12:34:56Z",
      "last_modified": "2024-05-18T12:34:56Z",
      "created_by": 1
  }
  ```

#### Create a Blog Post

- **URL**: `/api/v1/`
- **Method**: POST
- **Description**: Create a new blog post.

  **Request**:

  ```json
  POST /api/v1/
  {
      "title": "New Blog Post",
      "content": "This is the content of the new blog post.",
      "created_by": 1
  }
  ```

  **Response**:

  ```json
  {
      "id": 2,
      "title": "New Blog Post",
      "content": "This is the content of the new blog post.",
      "created_at": "2024-05-18T12:34:56Z",
      "last_modified": "2024-05-18T12:34:56Z",
      "created_by": 1
  }
  ```

#### Update a Blog Post

- **URL**: `/api/v1/{id}/`
- **Method**: PUT
- **Description**: Update an existing blog post by ID.

  **Request**:

  ```json
  PUT /api/v1/1/
  {
      "title": "Updated Blog Post",
      "content": "This is the updated content of the blog post.",
      "created_by": 1
  }
  ```

  **Response**:

  ```json
  {
      "id": 1,
      "title": "Updated Blog Post",
      "content": "This is the updated content of the blog post.",
      "created_at": "2024-05-18T12:34:56Z",
      "last_modified": "2024-05-18T12:45:00Z",
      "created_by": 1
  }
  ```

#### Delete a Blog Post

- **URL**: `/api/v1/{id}/`
- **Method**: DELETE
- **Description**: Delete a blog post by ID.

  **Request**:

  ```sh
  DELETE /api/v1/1/
  ```

  **Response**:

  ```json
  {
      "detail": "Blog post deleted."
  }


## Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

### Explanation:
- **Project Name**: Replace this with the actual name of your project.
- **Installation**: Instructions on how to set up the project, including cloning the repository, installing dependencies, applying migrations, creating a superuser, and running the server.
- **Usage**: Commands available in the Makefile.
- **API Documentation**: Detailed documentation of each API endpoint, including URL, method, description, request format, and example responses.
- **Contributing**: A placeholder for contribution guidelines.
- **License**: Information about the project's license.

Make sure to replace placeholders with your project's actual information.