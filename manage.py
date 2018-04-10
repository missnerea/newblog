from app import create_app,db
from flask_script import Manager,Server
from  app.models import User,Posts,Comments
from flask_migrate import Migrate,MigrateCommand

app=create_app('development')
app.secret_key = "super secret key"

manager=Manager(app)
manager.add_command('server',Server)
migrate =   Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def  make_shell_context():
    return dict(app=app,db=db,User=User,Posts=Posts,Comments=Comments)
if __name__ == '__main__':
    manager.run()
