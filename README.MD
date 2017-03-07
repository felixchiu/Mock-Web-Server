# Mock Web Server
### Setup the application
```
pip install virtualenv
cd working_folder
virtualenv venv/bin/activate
pip install flask
pip install -U flask-cors
```
### Run the application
```
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=8277
```
