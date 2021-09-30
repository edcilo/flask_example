from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from ms import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:secret@flask_db/flask'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
