import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import unittest
from coverage import Coverage
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app, db
from app import blueprint

"""Das Profil ist festgeschrieben"""
app = create_app('dev')  # dev | postgres-dev | test

app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    if app.config['ENV'] == 'dev':
        db.create_all()
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def coverage():
    """Check coverage and generate reports"""
    # coverage run --source=./app/main -m unittest discover -s ./app
    try:
        cov = Coverage()
        print("Starte Ueberpruefung der Coverage")
        cov.start()
        test()
        cov.stop()
        print("Tests erfolgreich ausgefuehrt und gespeichert.")
        cov.save()
        print("Erstelle HTML Report")
        cov.html_report()
        return 0
    except Exception as e:
        print(f"Error beim erstellen der Coverage: {e}")
        return 1


if __name__ == '__main__':
    manager.run()
