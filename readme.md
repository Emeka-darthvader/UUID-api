# Hi There, this is my simple API for generating timestamp & UUID pairs
## How to run
1. Should work fine if you have Flask installed, if not, *run pip install -r requirements.txt* to install the dependencies.
2. Run the app.py file, using **python app.py**

Note: This project was written using Python 3
## My thought process 
 I implemented this simple version using the python date-time and  UUID library. Also, to store the newly generated pairs, I made use of a dictionaries. The dictionary is then sorrted and reversed order to get the latest entry.

 I tried to make the app as modular as possible

 I also included a requirements.txt file to  help install all the dependencies.

 The API was hosted using Flask. 

 I also tried to maintain the usual python naming conventions of lower case for function names and seperating terms with underscore

 I tested with postman and it works so far!

## Improvements / added features for the future
1. Adding a database for improved persistence. I would create models. I also  use SQLAlchemy as my ORM and a postgresql for my database.
2. Hosting on a onine service. Heroku is really easy to pull off. Connect to GitHub as some for of CI, then create a Procfile to specify how and which file to run. Finally, provision a postgres service for the db
3. Writing unit tests for functions

Thanks and have a nice day :smile: !