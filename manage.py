#!/user/bin/env python
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from blog import create_app, db
from blog.model import Boke, Users
from config import config


app = create_app(config["testing"])
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=Users, Boke=Boke)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()