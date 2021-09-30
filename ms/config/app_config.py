import os

app_config = {
    'SECRET_KEY': os.getenv('SECRET_KEY', None),
}
