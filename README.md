# Blog API

---

This is a RESTful Blog API built using **FastAPI** that allows users to create, read, update and delete blog posts. The
API supports user authentication, ensuring that only authenticated users can manage their own blog posts.

## Features 🌟

- **Create a Blog Post**: Authenticated users can create blog posts with a title and body.
- **Read Blog Posts**: Retrieve all blog posts or get individual posts by ID.
- **Update a Blog Post**: Users can update their own blog posts.
- **Delete a Blog Post**: Users can delete their own blog posts.
- **User Authentication**: JWT-based authentication to secure access.

## Technologies Used 🛠️

- **FastAPI**: For building the API.
- **SQLite/PostgreSQL**: Database to store user and blog data.
- **JWT (JSON Web Token)**: For user authentication.
- **Pydantic**: For data validation.
- **Uvicorn**: ASGI server to run the application.

## Getting Started 🏁

Follow these instructions to set up and run the project locally.

### Prerequisites 📋

- **Python 3.8+**: Make sure Python is installed on your machine.
- **FastAPI**: Install FastAPI and Uvicorn by running the following command:

    ```bash
    pip install fastapi uvicorn
  ```

### Project Setup ⚙️

1. **Clone the Repository**:
    ```bash
   git clone
    cd blog-api
2. **Install Dependencies**: Install the required Python packages using `pip`:
    ```bash
   pip install -rm requirements.txt
    ```
3. **Database Setup**:
    - By default, the API uses SQLite for simplicity, but you can modify it to use PostgreSQL or any other database.
    - If using SQLite, the database will be created automatically when you run the app.

4. **Set Up Environment Variables**: Create a `.env` file in the project root to store sensitive data (like secret keys)
   and database configurations:
    ```bash
   SECRET_KEY=your_jwt_secret_key
   DATABASE_URL=sqlite:///./blog.db
   ```

### Running the Application ▶️

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

- The API will be available at: `http://127.0.0.1:8000`
- The interactive API docs will be accessible at: `http://127.0.0.1:8000/docs`

## API Endpoints 🔗

Here is a list of the core API endpoints:

### Authentication

- **POST /register**: Register a new user.

    - Request Body:
        ```json
      {
          "username": "your_username",
          "password": "your_password"
      }
      ```
- **POST /login**: Login and get a JWT token.

    - Request Body:
        ```json
        {
          "username": "your_username",
          "password": "your_password"
        }
        ```
    - Response: Returns a JWT token that must be used for authenticated requests.

### Blog Post

- **GET /blogs/**: Retrieve all blog posts
- **GET /blogs/{id}**: Retrieve a specific blog post by ID.
- **POST /blogs/**: Create a new blog post (Requires authentication).

  - Request Body:

    ```json
    {
      "title": "Blog Title",
      "body": "Blog content here"
    }
    ```
- **PUT /blogs/{id}**: Update an existing blog post (Requires authentication).

  - Request Body:

    ```json
    {
      "title": "Updated Title",
      "body": "updated blog content"
    }
    ```
- **DELETE /blogs/{id}**: Delete a blog post (Requires authentication).

## Authentication Flow 🔑

1. Register a new user by sending a `POST` request to `/register`.
2. Login to get a JWT token from `/login`.
3. Include the JWT token in the `Authorization` header as follows for all authenticated requests:

  ```makefile
  Authorization: Bearer <JWT_TOKEN>
  ```

## Database Models 🗄️

1. **User Model**:

    - `id`: Auto-generated user ID.
    - `username`: Unique username.
    - `password`: Hashed password.

2. **Blog Model**:

    - `id`: Auto-generated blog ID.
    - `title`: Title of the blog.
    - `body`: Content of the blog.
    - `author_id`: Foreign key to the User who created the blog.
    - `created_at`: Timestamp of when the blog was created.
    - `updated_at`: Timestamp of when the blog was last updated.
