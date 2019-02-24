from flask import Flask
from werkzeug.utils import secure_filename

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config.from_object(__name__)
from app import views

app.config['UPLOAD FOLDER'] = './app/static/uploads'