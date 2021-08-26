import os
import unittest

from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint     
from app.main.model.user import User   

from app.main import create_app, db   

app = create_app('dev')
CORS(app,resource={r"/":{"origins":"*"}})
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db, compare_type=True)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    db.create_all()
    app.run(port=80)


if __name__ == '__main__':
    manager.run()






#We create the app by running the create_app function and passing in the configuration name.
# We get this from the OS environment variable FLASK_CONFIG. 
# Because we are in development, we should set the environment variable to development.

#We have created a migrate object which will allow us to run migrations using Flask-Migrate. 
# We have also imported the models from the app package.

#Migrations allow us to manage changes we make to the models, and propagate these changes in the database. 
#For example, if later on we make a change to a field in one of the models, 
# all we will need to do is create and apply a migration, and the database will reflect the change.

#We’ll begin by installing Flask-Migrate, which will handle the database migrations using Alembic, 
# a lightweight database migration tool. Alembic emits ALTER statements to a database thus implememting changes made to the models. 
# It also auto-generates minimalistic migration scripts, which may be complex to write.