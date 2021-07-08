This is a simple page to get feedbacks for an application called MuseByte. It is created with flask and Postgres.
To start, open pgAdmin4. 
In the VScode terminal, open python, import the db method in app.py, then db.create_all() to create a database in Postgres. Exit python
Run $python app.py to start the server. The production database in app.py hasn't been filled because it depends on the cloud (aws, heroku etc)
