# Smart-book-Reviews

This project is a Book Review REST API built using Django. It provides endpoints for managing book reviews, including retrieving, creating, updating, and deleting reviews. Responses are returned in JSON format, including success or error messages.



## Setup Guide

### Prerequisites
1. Install **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2. Install **pip**: Python's package manager (comes pre-installed with Python).
3. Install **Django** using pip:

   pip install django


### Project Setup

#### 1. Create a Virtual Environment
1. Navigate to your project directory:
 
   cd Django
 
2. Create and activate a virtual environment:
   - **Windows**:
    
     python -m venv venv
     .\venv\Scripts\activate
  
   - **macOS/Linux**:
 
     python3 -m venv venv
     source venv/bin/activate



#### 2. Navigate to Backend
1. Move into the `Backend/api` directory:
  
   cd .\Backend\api\

2. Install dependencies (if applicable):
  
   pip install -r requirements.txt




#### 3. Run the Server
Start the Django development server:

python .\manage.py runserver 127.0.0.1:80


Alternatively, you can also run the secondary `server.py` if required:

python server.py


## REST API Documentation

### Base URL
- `http://127.0.0.1:80`

### Available Endpoints

1. **Retrieve All Book Reviews**  
   **GET** `/reviews`  
   - **Response**: JSON array of all reviews or an error message.

2. **Create a New Book Review**  
   **POST** `/reviews`  
   - **Payload**: JSON object with `title`, `author`, `review`, `rating`.
   - **Response**: Success or error message in JSON.

3. **Update an Existing Review**  
   **PUT** `/reviews/:id`  
   - **Payload**: JSON object with updated `title`, `author`, `review`, `rating`.
   - **Response**: Success or error message in JSON.

4. **Delete a Specific Review**  
   **DELETE** `/reviews/:id`  
   - **Response**: Success or error message in JSON.


### Error Response

{
  "message": "An error occurred while retrieving the review."
}



## Usage Example in JavaScript

### Retrieve Message
javascript
fetch('http://127.0.0.1:80/reviews')
  .then(response => response.json())
  .then(jsonData => console.debug(jsonData.message)) // Access success message
  .catch(error => console.error(error.message));      // Handle error


### Error Handling
javascript
fetch('http://127.0.0.1:80/reviews/1', { method: 'DELETE' })
  .then(response => response.json())
  .then(jsonData => console.debug(jsonData.message)) // Handle success
  .catch(error => console.error(jsonData.error));     // Handle error


## Project Notes

- All endpoints return a `message` key in JSON format for easy status identification.
- Ensure the server is running before making API requests.
- For issues or questions, refer to the Django documentation: [Django Docs](https://docs.djangoproject.com/).

