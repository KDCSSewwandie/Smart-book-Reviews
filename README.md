# Smart-book-Reviews
for book review web


*CLI Command*
pip install django
cd Django
.\venv\Scripts\activate
cd .\Backend\api\
python .\manage.py runserver 127.0.0.1:80
python server.py


REST API Documentation
END Points
•	GET /reviews: Retrieve all book review 
•	POST /reviews: Create a new book review 
•	PUT /reviews/:id: Update an existing review
•	DELETE /reviews/:id: Delete a specific review
Return json  if every endpoints are successfully. (GET return Data or Error message another methods error or success message)
If API Function work correctly it give successful message in json. you can access that message by “message” key.
Example in js : console.debug(jsonData.message);
If API Function Error it give error message in json. you can access that message by “message” key.
Example in js : console.error(jsonData.error);

