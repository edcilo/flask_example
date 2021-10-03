# Flask example project

This is a simple flask project

## Migrations

Create your model in ms/models/ path and registered on `__init__.py` file

From command line:

* Execute `flask db init` for create migrations folder
* `flask db migrate -m '[message]'` for create a migration
* `flask db upgrade` for apply migrations on database

For more information go to (https://flask-migrate.readthedocs.io/en/latest/#)[https://flask-migrate.readthedocs.io/en/latest/#]
