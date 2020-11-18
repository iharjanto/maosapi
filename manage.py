import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.main import createApp
from app.main import db

from app.main.bp import exbp


app = createApp(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(exbp)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@app.route('/')
def index():
    return "Contoh"


if __name__ == '__main__':
    manager.run()