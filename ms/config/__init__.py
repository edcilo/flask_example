from ms import app
from .app_config import app_config
from .db_config import db_config


app.config.update(**app_config)
app.config.update(**db_config)
