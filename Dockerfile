# # this an image 
FROM python:3.8
# # next is we have copy the entire file .
# # . points to the current directory.
# # within app  entire folder id copyed .
\
COPY . /flask_app
# # setting the working directory.

WORKDIR /flask_app
# This is the requirements.txt file 

RUN pip install -r requirements.txt
# setting the port numer 

EXPOSE $PORT

# setting the gunicorn and defalult ip address  and in app 
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:flask_app
# module: Flask application name